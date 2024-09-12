import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_numbers(n=6, min_val=1, max_val=45):
    return random.sample(range(min_val, max_val + 1), n)

def get_color(number):
    if 1 <= number <= 10:
        return 'yellow'
    elif 11 <= number <= 20:
        return 'blue'
    elif 21 <= number <= 30:
        return 'red'
    elif 31 <= number <= 40:
        return 'gray'
    elif 41 <= number <= 45:
        return 'green'
    return 'black'  # 기본 색상

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
    st.write('생성된 번호:', numbers)

    fig = plot_numbers_with_colors(numbers)
    st.pyplot(fig)
