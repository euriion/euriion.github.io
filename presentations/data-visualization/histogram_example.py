import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_histogram():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 데이터 생성
    np.random.seed(42)
    data = np.random.normal(75, 10, 1000)
    
    # 히스토그램 그리기
    n, bins, patches = ax.hist(data, bins=30, color='#9467bd', alpha=0.7, edgecolor='black')
    
    # 제목과 레이블 설정
    ax.set_title('시험점수 분포', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlabel('점수', fontsize=12)
    ax.set_ylabel('빈도', fontsize=12)
    
    # 평균선 추가
    mean_val = np.mean(data)
    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2)
    
    # 범례 추가 (한글 포함)
    ax.text(mean_val + 2, max(n) * 0.9, f'평균: {mean_val:.1f}', 
            fontsize=12, color='red', fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/histogram_example.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    create_histogram()
    print("히스토그램 생성 완료")