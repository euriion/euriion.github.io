import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_scatter_plot():
    plt.figure(figsize=(10, 8))
    np.random.seed(42)
    x = np.random.normal(50, 15, 100)
    y = 2 * x + np.random.normal(0, 10, 100)
    
    plt.scatter(x, y, alpha=0.6, s=60, color='#1f77b4')
    
    # 추세선 추가
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x, p(x), "r--", alpha=0.8, linewidth=2, label='추세선')
    
    plt.title('학습시간과 시험점수 관계', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('학습시간 (시간)', fontsize=12)
    plt.ylabel('시험점수', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/scatter_plot_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_scatter_plot()
    print("산점도 생성 완료")