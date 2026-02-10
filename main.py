import streamlit as st
from app.responder import analyze_and_reply

st.set_page_config(page_title="Customer Sentianl", layout="centered")

# --- 헤더 ---
st.title("CS 감정 분석 & 자동 답변 봇")
st.divider()

# --- 입력 섹션 ---
st.subheader("고객의 소리 (VOC) 입력")
customer_text = st.text_area(
    "고객이 보낸 카톡, 이메일, 게시글을 복사해서 넣으세요.",
    height=150,
    placeholder="예시: 야! 주문한 지가 언젠데 아직도 안 와? 장난하냐? 당장 환불해줘! 다신 여기서 안 사!"
)

analyze_btn = st.button("분석 및 답변 생성", type="primary", width="stretch")

# --- 결과 섹션 ---
if analyze_btn:
    if not customer_text:
        st.warning("고객 문의 내용을 입력해주세요")
    else:
        with st.spinner("CS 팀장이 고객의 심리를 분석 중입니다..."):
            result = analyze_and_reply(customer_text)

            if "error" in result:
                st.error(result["error"])
            else:
                score = result.get("sentiment_score", 0)
                intent = result.get("intent", "")
                summary = result.get("summary", "")
                responses = result.get("responses", {})

                st.divider()
                st.subheader("분석 리포트")

                # 감정 온도계
                # 점수에 따른 색상 및 이모지
                if score >= 80:
                    color = "red"
                    icon = "🤬 극대노 (위험)"
                elif score >= 50:
                    color = "orange"
                    icon = "😠 화남 (주의)"
                else:
                    color = "green"
                    icon = "🙂 평온 (안전)"

                st.metric("감정 온도", f"{score}℃", icon)
                st.progress(score / 100, text=f"현재 고객 상태: {icon}")

                # 의도 및 요약
                st.info(f"**파악된 의도:** {intent}")
                st.caption(f"**오약:** {summary}")

                st.divider()

                # 답변 제안
                st.subheader("추천 답변 (골라서 쓰세요)")
                
                tab1, tab2, tab3 = st.tabs(["공감형 (부드럽게)", "보상형 (해결책)", "원칙형 (단호하게)"])

                with tab1:
                    st.success("진심 어린 사과와 공감이 필요할 때 쓰세요.")
                    st.text_area("답변 A", value=responses.get("type_a", ""), height=200)
                    
                with tab2:
                    st.warning("구체적인 보상이나 대안을 제시할 때 쓰세요.")
                    st.text_area("답변 B", value=responses.get("type_b", ""), height=200)
                    
                with tab3:
                    st.error("무리한 요구를 정중하게 거절하거나 규정을 안내할 때 쓰세요.")
                    st.text_area("답변 C", value=responses.get("type_c", ""), height=200)