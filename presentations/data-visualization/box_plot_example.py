import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_box_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 데이터 생성
    np.random.seed(42)
    data1 = np.random.normal(100, 15, 100)
    data2 = np.random.normal(110, 12, 100)
    data3 = np.random.normal(95, 18, 100)
    data4 = np.random.normal(105, 10, 100)
    
    data = [data1, data2, data3, data4]
    labels = ['A팀', 'B팀', 'C팀', 'D팀']
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    
    # 박스플롯 그리기
    box_plot = ax.boxplot(data, labels=labels, patch_artist=True)
    
    # 박스 색상 설정
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    # 제목과 레이블 설정
    ax.set_title('팀별 성과 분포', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('팀', fontsize=12)
    ax.set_ylabel('성과 점수', fontsize=12)
    
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/box_plot_example.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    create_box_plot()
    print("박스 플롯 생성 완료")