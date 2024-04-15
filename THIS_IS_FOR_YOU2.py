import numpy as np
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.patches import PathPatch
from matplotlib.font_manager import FontProperties
# 주어진 함수 정의
def f1(x):
    return np.sqrt(0.25-(x-(abs(x)/x)*0.5)**2)

def f2(x):
    return -((1 + x**0.2) * (1 - x**0.2))**0.4



def make_for_you():
    # x 범위 설정
    x = np.linspace(-1, 1, 51)
    # 함수 적용하여 y 값 계산
    y1 = f1(x)
    y2 = f2(x)
    y3 = f2(-x)
    fp = FontProperties(family="DejaVu Sans")
    heart_path = TextPath((0, 0), "♥", size=1, prop=fp)
    scalar = 1000
    # 그래프 설정
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y1, s=scalar, color='r', marker=heart_path)
    plt.scatter(x, y2, s=scalar, color='r', marker=heart_path)
    plt.scatter(x, y3, s=scalar, color='r', marker=heart_path)
    plt.title('THIS IS FOR YOU!!♥')
    plt.grid(False)
    plt.xticks([], [])
    plt.yticks([], [])
    plt.savefig('heart.png')
    plt.show()

make_for_you()