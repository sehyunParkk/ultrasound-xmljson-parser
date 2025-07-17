# Ultrasound Data Analysis Automation

본 프로젝트는 심장초음파 데이터(XML/JSON)의 구조를 분석하고, 주요 파라미터를 자동 추출하여 CSV 형식으로 변환하는 도구입니다.
GE, Siemens 등 의료기기별 데이터 구조 차이를 파악하고, 정형 분석에 활용 가능한 형태로 재구성하는 데 목적이 있습니다.

-----

# 📌 Features

- ✅ XML / JSON 포맷 자동 파싱
- ✅ 주요 파라미터(ScanMode, ParameterName, DisplayValue 등) 추출
- ✅ Redirect 구조가 포함된 JSON의 중첩 데이터 처리
- ✅ 결과물 CSV 자동 저장
- ✅ GE / Siemens 기기 데이터 비교 및 분석 대응 가능

-----

# 📂 File Structure

Project Root
- ↳ organizing_data.py
- ↳ organized_xml.csv
- ↳ organized_json.csv
- ↳ XML_JSON_데이터대조비교분석.pdf
- ↳ 데이터 분석 결론.pdf
- ↳ 2025-06-02_16740.xml
- ↳ 20250515110924ReportExport.json
- ↳ README.md

-----

# 📖 Documentation

분석 결과 및 데이터 구조 해석에 대한 문서는 다음 파일에서 확인할 수 있습니다.

- 'XML_JSON_데이터대조비교분석.pdf'
- '데이터 분석 결론.pdf'

파일 포맷 별 구조 차이, Redirect 구조의 불규칙성 등 실무적인 이슈를 상세히 정리하였습니다.

-----

# 💬 Remarks

본 프로젝트는 의료 데이터를 자동 분석하고 구조화하는 툴로, 인턴십 기간 중 수행한 실제 업무 기반 프로젝트입니다.

-----

# 📩 Contact

- Author : Sehyun Park
- Email : manywish6431@naver.com
