import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_radar_chart():
    plt.figure(figsize=(10, 10))
    categories = ['속도', '품질', '가격', '서비스', '디자인', '기능성']
    
    # 제품 A와 B의 점수
    product_a = [8, 7, 6, 9, 8, 7]
    product_b = [6, 9, 8, 7, 6, 8]
    
    # 각도 계산
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]  # 원을 닫기 위해
    
    product_a += product_a[:1]
    product_b += product_b[:1]
    
    ax = plt.subplot(111, projection='polar')
    
    # 제품 A
    ax.plot(angles, product_a, 'o-', linewidth=2, label='제품 A', color='#1f77b4')
    ax.fill(angles, product_a, alpha=0.25, color='#1f77b4')
    
    # 제품 B
    ax.plot(angles, product_b, 'o-', linewidth=2, label='제품 B', color='#ff7f0e')
    ax.fill(angles, product_b, alpha=0.25, color='#ff7f0e')
    
    # 카테고리 레이블 추가
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10)
    ax.grid(True)
    
    plt.title('제품 비교 분석', fontsize=16, fontweight='bold', pad=30)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0), fontsize=12)
    
    plt.tight_layout()
    plt.savefig('images/radar_chart_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_radar_chart()
    print("레이더 차트 생성 완료")