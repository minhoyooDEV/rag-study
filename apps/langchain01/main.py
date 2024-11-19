import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# .env 파일 로드
load_dotenv()

# 환경변수 가져오기
endpoint = os.getenv("LANGCHAIN_ENDPOINT")
api_key = os.getenv("LANGCHAIN_API_KEY")
project_name = os.getenv("LANGCHAIN_PROJECT")

# 환경변수를 출력해 확인 (테스트용)
print(f"Endpoint: {endpoint}")
print(f"API Key: {api_key}")
print(f"Project: {project_name}")


# # LangChain 사용 예시
# llm = ChatOpenAI(api_key=api_key, endpoint=endpoint)
# response = llm.invoke("Hello, world!")
# print(response)
llm = ChatOpenAI()
response = llm.invoke("how about today weather in seoul?")
print(response)