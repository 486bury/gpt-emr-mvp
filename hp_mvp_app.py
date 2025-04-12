import streamlit as st
from openai import OpenAI

# 🔐 OpenAI API 키 입력
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else None)

# 🧠 지훈의 파인튜닝 모델 ID
FINETUNED_MODEL_ID = "ft:gpt-3.5-turbo-0125:black-scarecrow::BJyAMO2F"

# 🎯 GPT 호출 함수r
def generate_hp_note(user_input):
    response = client.chat.completions.create(
        model=FINETUNED_MODEL_ID,
        messages=[{"role": "user", "content": user_input}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# 🖥️ Streamlit 앱
st.set_page_config(page_title="GPT H&P 생성기 (MVP)", layout="wide")
st.title("🧠 GPT 기반 H&P 자동 생성기 (지훈 버전 MVP)")
st.markdown("자연어 진료 메모를 H&P 형식으로 자동 정리합니다.")

user_input = st.text_area("📝 자유 진료 메모 입력", height=250, placeholder="예: 약 1년 전부터 양쪽 팔에 가려움. 긁으면 붉어짐. 피부 건조함 동반.")

if st.button("🪄 H&P 자동 생성"):
    if not user_input.strip():
        st.warning("입력값을 먼저 작성해주세요.")
    else:
        with st.spinner("GPT가 정리 중입니다..."):
            result = generate_hp_note(user_input)
            st.success("✅ 정리 완료!")
            st.text_area("🧾 GPT 출력 결과", value=result, height=400, label_visibility="collapsed")
