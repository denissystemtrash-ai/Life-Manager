import streamlit as st
import google.generativeai as genai
import os

# Настройка ИИ с "умным" подбором модели
api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Используем актуальное имя модели
    model = genai.GenerativeModel('gemini-1.5-flash') 
else:
    st.error("Ключ API не найден!")

# 2. Настройка интерфейса для iPad
st.set_page_config(page_title="Life Manager", page_icon="🧘", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007AFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Менеджер Жизни")

# 3. Блок ввода данных
with st.container():
    st.subheader("Что произошло?")
    user_input = st.text_area("", placeholder="Опиши свои успехи, мысли или затык...", label_visibility="collapsed")
    
    col1, col2 = st.columns(2)
    with col1:
        energy = st.select_slider("Энергия", options=range(1, 11), value=7)
    with col2:
        mood = st.select_slider("Вайб", options=["😴", "😐", "🙂", "🔥"], value="🙂")

# 4. Логика ИИ-советника
if st.button("Сохранить и получить совет"):
    if not user_input:
        st.warning("Сначала напиши что-нибудь!")
    else:
        with st.spinner('ИИ обдумывает твой вайб...'):
            try:
                prompt = f"""
                Ты — персональный менеджер жизни и коуч. 
                Пользователь пишет: "{user_input}"
                Его энергия: {energy}/10, настроение: {mood}.
                Дай один конкретный совет, поддержи или задай важный вопрос. 
                Отвечай кратко, мотивирующе и по делу.
                """
                response = model.generate_content(prompt)
                
                st.success("Прогресс сохранен!")
                st.markdown("---")
                st.subheader("🤖 Твой AI-советник:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Ошибка ИИ: {e}")

# 5. Секция прогресса (пока временная)
st.divider()
st.caption("Подсказка: чтобы приложение было на iPad как родное, нажми 'Поделиться' -> 'На экран Домой'")
