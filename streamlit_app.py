import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_numbers(n=6, min_val=1, max_val=45):
    return random.sample(range(min_val, max_val + 1), n)

def get_color(number):
    if 1 <= number <= 10:
        return '#F7C600'  # 부드러운 노란색
    elif 11 <= number <= 20:
        return '#4A90E2'  # 부드러운 파란색
    elif 21 <= number <= 30:
        return '#E94E77'  # 부드러운 빨간색
    elif 31 <= number <= 40:
        return '#9B9B9B'  # 부드러운 회색
    elif 41 <= number <= 45:
        return '#4CAF50'  # 부드러운 녹색
    return '#000000'  # 기본 색상 (검은색)

def plot_numbers_with_colors(numbers):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_aspect('equal')  # 축의 비율을 같게 설정

    for i, number in enumerate(numbers):
        color = get_color(number)
        circle = plt.Circle((i * 1.5 + 1, 2), 0.8, color=color, ec='black', linewidth=2)
        ax.add_artist(circle)
        ax.text(i * 1.5 + 1, 2, str(number), fontsize=20, ha='center', va='center', color='white', weight='bold')

    return fig

st.title('랜덤 로또 번호 생성기')

if st.button('번호 생성하기'):
    numbers = generate_random_numbers()

    fig = plot_numbers_with_colors(numbers)
    st.pyplot(fig)
