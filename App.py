import streamlit as st
import datetime

# Настройки страницы для iPad
st.set_page_config(page_title="Life Manager", page_icon="🧠", layout="centered")

st.title("🧠 Мой Менеджер Жизни")

# --- БЛОК 1: СОСТОЯНИЕ ---
st.subheader("Как дела сегодня?")
energy = st.select_slider("Уровень энергии", options=range(1, 11), value=5)
mood = st.selectbox("Настроение", ["Спокойное", "Бодрое", "Тревожное", "Уставшее", "Продуктивное"])

# --- БЛОК 2: ЗАМЕТКИ ---
st.subheader("Что на уме?")
note = st.text_area("Запиши мысль или достижение...", placeholder="Сегодня я выучил, как работает вайб-кодинг...")

if st.button("Сохранить прогресс"):
    # Здесь мы позже добавим сохранение в базу данных
    st.success(f"Записано! Энергия: {energy}, Настроение: {mood}")
    st.balloons()

# --- БЛОК 3: AI-СОВЕТНИК ---
st.divider()
st.subheader("🤖 AI-Советник")
if st.button("Проанализировать мой вайб"):
    st.info("Я вижу, что ты настроен решительно! Твой уровень энергии 5/10 — самое время для короткой фокусировки.")
    # Тут будет запрос к Gemini API
