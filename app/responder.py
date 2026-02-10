from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from app.config import MODEL_NAME, SYSTEM_PROMPT

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_and_reply(customer_text):
    """고객 문의를 분석하여 감정 점수와 답변 3종 세트 생성"""

    if not customer_text:
        return {"error": "내용을 입력해주세요."}
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"고객 문의 내용:\n{customer_text}"}
            ],
            reasoning_effort="medium",
            response_format={"type": "json_object"}
        )

        result_json = json.loads(response.choices[0].message.content)
        return result_json
    
    except Exception as e:
        return {"error": f"분석 중 오류 발생: {str(e)}"}