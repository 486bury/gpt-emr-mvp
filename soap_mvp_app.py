import streamlit as st
from openai import OpenAI

# 🔐 API 키 설정
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None)

# 🧠 SOAP 전용 파인튜닝 모델 ID
FINETUNED_SOAP_MODEL_ID = "ft:gpt-3.5-turbo-0125:black-scarecrow::BJyf4XqP"

# 🎯 GPT 호출 함수
def generate_soap_note(user_input):
    response = client.chat.completions.create(
        model=FINETUNED_SOAP_MODEL_ID,
        messages=[{"role": "user", "content": user_input}],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

# 🖥️ Streamlit 앱 구성
st.set_page_config(page_title="GPT SOAP 생성기 (MVP)", layout="wide")
st.title("📋 GPT 기반 SOAP 자동 생성기 (지훈 버전 MVP)")
st.markdown("자유 진료 메모를 기반으로 SOAP 형식으로 정리된 경과기록을 생성합니다.")

# 사용자 입력 영역
user_input = st.text_area("📝 자유 진료 메모 입력", height=250, placeholder="예: 피부 가려움 악화되어 내원, 약 복용 불규칙, scratch marks 관찰됨")

# 실행 버튼
if st.button("🪄 SOAP 자동 생성"):
    if not user_input.strip():
        st.warning("입력값을 먼저 작성해주세요.")
    else:
        with st.spinner("GPT가 SOAP을 생성 중입니다..."):
            result = generate_soap_note(user_input)
            st.success("✅ SOAP 생성 완료!")
            st.text_area("📄 GPT 출력 결과", value=result, height=400, label_visibility="collapsed")
