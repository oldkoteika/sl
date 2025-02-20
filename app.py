import streamlit as st
from datetime import datetime

# Список пользователей (можно заменить на загрузку из БД)
users = ["Иванов И.И.", "Петров П.П.", "Сидоров С.С."]

# Заголовок
st.title("Выбор даты и пользователя")

# Контейнер для формы
with st.container():
        # Выбор даты
    selected_date = st.date_input("Выберите дату", datetime.today().date())

    # Выбор времени
    selected_time = st.time_input("Выберите время", datetime.now().time())
    
    # Выбор пользователя
    selected_user = st.selectbox("Выберите пользователя", users)
    
    # Кнопки
    col1, col2 = st.columns(2)
    with col1:
        save_button = st.button("Сохранить", type="primary")
    with col2:
        cancel_button = st.button("Отмена")
    
    # Обработчик сохранения
    if save_button:
        st.success("Сохранено!")
    
    # Обработчик отмены (сбрасывать состояние здесь не требуется, просто игнорируем)