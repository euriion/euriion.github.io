import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_bar_chart():
    plt.figure(figsize=(10, 6))
    categories = ['서울', '부산', '대구', '인천', '광주']
    values = [9776, 3413, 2438, 2955, 1463]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    bars = plt.bar(categories, values, color=colors)
    plt.title('지역별 인구수 (단위: 천명)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('지역', fontsize=12)
    plt.ylabel('인구수 (천명)', fontsize=12)
    
    # 막대 위에 값 표시
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50, 
                f'{value:,}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('images/bar_chart_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_bar_chart()
    print("막대 차트 생성 완료")