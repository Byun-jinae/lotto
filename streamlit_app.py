import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_random_numbers(n=6, min_val=1, max_val=45):
    return random.sample(range(min_val, max_val + 1), n)

def plot_numbers_with_colors(numbers):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    colors = np.random.rand(6, 3)  # 랜덤 색상 생성
    for i, (number, color) in enumerate(zip(numbers, colors)):
        circle = plt.Circle((5, 9 - i * 2), 0.8, color=color, ec='black')
        ax.add_artist(circle)
        ax.text(5, 9 - i * 2, str(number), fontsize=16, ha='center', va='center', color='black')

    return fig

st.title('랜덤 로또 번호 생성기')

if st.button('번호 생성하기'):
    numbers = generate_random_numbers()
    st.write('생성된 번호:', numbers)

    fig = plot_numbers_with_colors(numbers)
    st.pyplot(fig)
