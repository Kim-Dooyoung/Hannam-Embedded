import google.generativeai as genai
import os
from dotenv import load_dotenv
from save_material import MaterialHandler

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY가 설정되지 않았습니다.")

genai.configure(api_key=api_key)

file_name = "임베디드_재료.xlsx"

# 재료 핸들러 인스턴스 생성
material_handler = MaterialHandler(file_name)
material_handler.load_or_create()

materials = input("재료 목록을 입력하세요 (예: 재료1 재료2 재료3)(입력 후 엔터 클릭): ").split()

# 재료 추가
material_handler.add_materials(materials)

# 엑셀 파일 저장
material_handler.save()

# 재료 목록을 prompt에 넣기
prompt = f"재료 목록: {', '.join(materials)}. 이 재료들에 대한 간단한 설명을 작성해주세요."


generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    'gemini-pro', generation_config=generation_config)

response = model.generate_content(prompt)
print(response.text)
