import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
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

def create_eda_correlation_heatmap():
    np.random.seed(42)
    
    # 상관관계가 있는 데이터 생성
    n_samples = 500
    
    # 기본 변수
    x1 = np.random.normal(0, 1, n_samples)
    x2 = 0.7 * x1 + np.random.normal(0, 0.5, n_samples)  # x1과 강한 양의 상관
    x3 = -0.5 * x1 + np.random.normal(0, 0.8, n_samples)  # x1과 중간 음의 상관
    x4 = np.random.normal(0, 1, n_samples)  # 독립적
    x5 = 0.3 * x2 + 0.4 * x4 + np.random.normal(0, 0.6, n_samples)  # 복합 상관
    
    # 데이터프레임 생성
    data = pd.DataFrame({
        'Revenue': x1 * 100 + 500,
        'Marketing_Spend': x2 * 50 + 200,
        'Customer_Satisfaction': -x3 * 10 + 75,
        'Employee_Count': x4 * 20 + 100,
        'Market_Share': x5 * 5 + 25
    })
    
    # 상관관계 계산
    correlation_matrix = data.corr()
    
    plt.figure(figsize=(10, 8))
    
    # 히트맵 생성
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, 
                mask=mask,
                annot=True, 
                cmap='RdBu_r', 
                center=0,
                square=True,
                linewidths=0.5,
                cbar_kws={"shrink": .8},
                fmt='.2f',
                annot_kws={'size': 12, 'weight': 'bold'})
    
    plt.title('EDA: 상관관계 히트맵\n"변수 간 선형 관계를 한눈에 파악"', 
              fontsize=16, fontweight='bold', pad=20)
    
    # 해석 가이드 추가
    plt.figtext(0.02, 0.02, 
               '해석 가이드:\n'
               '• 1에 가까우면 강한 양의 상관\n'
               '• -1에 가까우면 강한 음의 상관\n'
               '• 0에 가까우면 상관관계 없음',
               fontsize=10, bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgray"))
    
    plt.tight_layout()
    plt.savefig('images/eda-correlation-heatmap.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_eda_correlation_heatmap()
    print("EDA 상관관계 히트맵 생성 완료")