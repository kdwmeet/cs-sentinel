# Customer Sentinel (CS 감정 분석 및 자동 응대 솔루션)

## 1. 프로젝트 개요

Customer Sentinel은 고객의 문의 내용(VOC)을 분석하여 감정 상태를 진단하고, 상황에 적합한 응대 스크립트를 자동으로 생성하는 AI 기반의 CRM(Customer Relationship Management) 솔루션입니다.

감정 노동의 강도가 높은 CS 업무 환경에서 상담원의 정신적 스트레스를 경감하고, 악성 민원에 대한 대응 품질을 표준화하기 위해 개발되었습니다. OpenAI의 **gpt-5-mini** 모델을 활용하여 고객 텍스트의 뉘앙스를 정밀하게 분석하고, 분노 수준을 수치화하며, 공감형, 보상형, 원칙형 등 다각적인 답변 전략을 제안합니다.

### 주요 기능
* **Sentiment Analysis:** 고객 문의 텍스트를 분석하여 감정 온도(Sentiment Score)를 0~100점 척도로 정량화.
* **Intent Recognition:** 환불 요구, 단순 불만, 정보 문의 등 고객의 핵심 의도를 파악.
* **Multi-Persona Response:** * **Type A (공감형):** 고객의 감정을 어루만지는 사과와 위로 중심의 답변.
    * **Type B (보상형):** 포인트 지급, 교환 등 실질적인 해결책을 제시하는 답변.
    * **Type C (원칙형):** 회사의 규정과 약관을 정중하고 단호하게 안내하는 답변.
* **Automated Drafting:** 상담원이 즉시 사용할 수 있는 완성된 문장 형태의 스크립트 제공.

## 2. 시스템 아키텍처

본 시스템은 텍스트 분석 및 자연어 생성(NLG) 파이프라인을 통해 비정형 고객 데이터를 처리합니다.

1.  **Input Layer:** 사용자가 이메일, 채팅 로그, 게시판 글 등 고객의 문의 내용을 입력.
2.  **Profiling Layer:** '20년 경력의 위기 관리 전문가' 페르소나를 시스템 프롬프트에 적용하여 분석 기준 설정.
3.  **Inference Layer:** **gpt-5-mini** 모델이 입력된 텍스트의 감정 강도와 의도를 추론하고, 3가지 전략에 따른 답변 생성.
4.  **Presentation Layer:** 분석 결과(감정 점수, 요약, 답변 스크립트)를 JSON으로 구조화하여 UI에 시각화.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI **gpt-5-mini**
* **Web Framework:** Streamlit
* **Configuration:** python-dotenv

## 4. 프로젝트 구조

비즈니스 로직과 분석 설정을 분리하여 확장성을 고려한 모듈형 구조입니다.

```text
cs-sentinel/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 및 분석 대시보드 UI
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # CS 전문가 페르소나 및 감정 분석 프롬프트 정의
    └── responder.py      # OpenAI API 통신 및 JSON 데이터 파싱 로직
```

## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python 환경이 설치되어 있어야 합니다. 터미널에서 저장소를 복제하고 프로젝트 디렉토리로 이동하십시오.

```Bash
git clone [레포지토리 주소]
cd cs-sentinel
```
### 5.2. 의존성 설치
필요한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 경로에 .env 파일을 생성하고, 유효한 OpenAI API 키를 입력하십시오.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 실행
Streamlit 애플리케이션을 실행합니다.

```Bash
streamlit run main.py
```
## 6. 출력 데이터 사양 (JSON Schema)
AI 모델은 분석 결과를 다음과 같은 JSON 구조로 반환합니다. 이를 통해 기존의 CS 관리 시스템(Zendesk, Salesforce 등)과 API 연동이 가능합니다.

```JSON
{
  "sentiment_score": 85,
  "intent": "배송 지연에 대한 불만 및 환불 요구",
  "summary": "주문 후 일주일이 경과하였으나 배송이 시작되지 않아 고객의 불만이 극에 달한 상태임.",
  "responses": {
    "type_a": "고객님, 오랫동안 기다리시게 하여 진심으로 죄송합니다. 배송이 늦어져 얼마나 답답하셨을지 충분히 이해합니다.",
    "type_b": "불편을 드려 죄송합니다. 우선 발송 처리와 함께 보상의 의미로 적립금 3,000원을 즉시 지급해 드리겠습니다.",
    "type_c": "현재 주문량 폭주로 인해 배송이 지연되고 있습니다. 당사 배송 약관 제5조에 의거하여 순차 발송 중임을 양해 부탁드립니다."
  }
}
```

## 7. 실행 화면
<img width="708" height="829" alt="스크린샷 2026-02-10 113747" src="https://github.com/user-attachments/assets/41e04687-6d96-4cc4-bce4-efa59a44abf5" />

