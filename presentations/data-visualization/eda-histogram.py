import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 한글 폰트 설정 - 여러 옵션 시도
font_candidates = ['Malgun Gothic', 'NanumGothic', 'Batang', 'Gulim']
for font in font_candidates:
    try:
        plt.rcParams['font.family'] = font
        break
    except:
        continue

plt.rcParams['axes.unicode_minus'] = False

def create_eda_histogram():
    np.random.seed(42)
    
    # 다양한 분포 생성
    normal_data = np.random.normal(100, 15, 1000)
    skewed_data = np.random.exponential(2, 1000) * 10 + 80
    bimodal_data = np.concatenate([
        np.random.normal(85, 8, 500),
        np.random.normal(115, 8, 500)
    ])
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 정규분포
    ax1.hist(normal_data, bins=30, alpha=0.7, color='skyblue', edgecolor='black')
    ax1.axvline(np.mean(normal_data), color='red', linestyle='--', linewidth=2, label=f'평균: {np.mean(normal_data):.1f}')
    ax1.axvline(np.median(normal_data), color='orange', linestyle='--', linewidth=2, label=f'중앙값: {np.median(normal_data):.1f}')
    ax1.set_title('정규분포 (Normal Distribution)', fontweight='bold', fontsize=12)
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 왜곡분포
    ax2.hist(skewed_data, bins=30, alpha=0.7, color='lightcoral', edgecolor='black')
    ax2.axvline(np.mean(skewed_data), color='red', linestyle='--', linewidth=2, label=f'평균: {np.mean(skewed_data):.1f}')
    ax2.axvline(np.median(skewed_data), color='orange', linestyle='--', linewidth=2, label=f'중앙값: {np.median(skewed_data):.1f}')
    ax2.set_title('우편향 분포 (Right-skewed)', fontweight='bold', fontsize=12)
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 이봉분포
    ax3.hist(bimodal_data, bins=30, alpha=0.7, color='lightgreen', edgecolor='black')
    ax3.axvline(np.mean(bimodal_data), color='red', linestyle='--', linewidth=2, label=f'평균: {np.mean(bimodal_data):.1f}')
    ax3.axvline(np.median(bimodal_data), color='orange', linestyle='--', linewidth=2, label=f'중앙값: {np.median(bimodal_data):.1f}')
    ax3.set_title('이봉분포 (Bimodal Distribution)', fontweight='bold', fontsize=12)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 전체 비교
    ax4.hist(normal_data, bins=20, alpha=0.5, label='정규분포', color='skyblue')
    ax4.hist(skewed_data, bins=20, alpha=0.5, label='우편향분포', color='lightcoral')
    ax4.hist(bimodal_data, bins=20, alpha=0.5, label='이봉분포', color='lightgreen')
    ax4.set_title('분포 비교', fontweight='bold', fontsize=12)
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('EDA: 히스토그램으로 데이터 분포 탐색\n"분포 형태가 분석 전략을 결정한다"', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/eda-histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_eda_histogram()
    print("EDA 히스토그램 생성 완료")