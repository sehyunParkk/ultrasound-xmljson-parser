import xml.etree.ElementTree as ET
import csv
import os
import json

xml_data = []
fxml_data = []
json_data = []
new_mode = None
new_tag = None
new_val = None
tree = None
root = None
lavel = None
java_val = None
java_item = None
data = []

filename = input("불러올 JSON 또는 XML 파일명을 입력하세요: ").strip()
name, ext = os.path.splitext(filename)

if ext.lower() == ".xml":
    tree = ET.parse(filename)
    root = tree.getroot()
    for e in root.iter():
        if len(e) == 0:
            if e.tag == "ParameterName":
                new_tag = e.text.strip() if e.text else None
            elif e.tag == "DisplayValue":
                if e.text:
                    try:
                        rounded_val = round(float(e.text.strip()), 2)
                        new_val = str(rounded_val)
                    except ValueError:
                        new_val = e.text.strip()
                else:
                    new_val = None
            elif e.tag == "ScanMode":
                new_mode = e.text.strip() if e.text else None
        # 두 값이 모두 준비된 경우에만 쌍으로 저장
        if new_tag is not None and new_val is not None:
            xml_data.append((new_mode, new_tag, new_val))
            new_mode = None
            new_tag = None
            new_val = None

elif ext.lower() == ".json":
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    measurement_values = data.get("MeasurmentValues", {})

    # 1. Calculations 항목 처리
    calculations = measurement_values.get("Calculations", {})
    for label_name, value_dict in calculations.items():
        if isinstance(value_dict, dict):
            java_val = value_dict.get("DoubleValue")
            if java_val is not None:
                json_data.append((label_name, java_val))

    # 2. Tools + Redirected 항목 처리
    tools = measurement_values.get("Tools", [])
    for item in tools:
        # 기본 항목 처리
        label_name = item.get("LabelName")
        formatted_elements = item.get("FormattedElements", [])
        if label_name and formatted_elements:
            for element in formatted_elements:
                if "RoundedValue" in element:
                    java_val = element["RoundedValue"]
                elif "DoubleValue" in element:
                    java_val = element["DoubleValue"]
                else:
                    java_val = None

                if java_val is not None:
                    json_data.append((label_name, java_val))

        # Redirected 항목 처리
        redirected = item.get("Redirected") or []
        for redir in redirected:
            java_item = redir.get("Item2")
            if java_item:
                redirected_label = java_item.get("LabelName")
                redirected_elements = java_item.get("FormattedElements", [])
                if redirected_label and redirected_elements:
                    for element in redirected_elements:
                        if "RoundedValue" in element:
                            java_val = element["RoundedValue"]
                        elif "DoubleValue" in element:
                            java_val = element["DoubleValue"]
                        else:
                            java_val = None

                        if java_val is not None:
                            json_data.append((redirected_label, java_val))


with open("output_value2.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    if ext.lower() == ".xml":
        writer.writerow(["mode", "key", "value"])
        for item in xml_data:
            writer.writerow(item)
    elif ext.lower() == ".json":
        writer.writerow(["label", "value"])
        for item in json_data:
            writer.writerow(item)

print("CSV 파일로 저장 완료!")