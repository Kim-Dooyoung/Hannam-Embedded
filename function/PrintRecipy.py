import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY가 설정되지 않았습니다.")

genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    'gemini-pro', generation_config=generation_config)

prompt = """
- 날짜: 2024-01-09
- 회사: 삼성전자
- 5-20 골든크로스: 매수 신호
- 등락률: -2.35%
위 내용만 사용해서 보고서 형식으로 요약해줘.
이 외에 다른 내용은 사용하지 말아줘.
"""

response = model.generate_content(prompt)
print(response.text)
