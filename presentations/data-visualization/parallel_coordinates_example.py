import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_parallel_coordinates():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 데이터 생성
    np.random.seed(42)
    
    # 3개 고객 그룹의 다차원 데이터
    premium_customers = np.random.multivariate_normal([80, 85, 90, 75, 85], np.eye(5) * 50, 70)
    regular_customers = np.random.multivariate_normal([60, 65, 70, 60, 65], np.eye(5) * 40, 80)
    budget_customers = np.random.multivariate_normal([40, 45, 50, 45, 50], np.eye(5) * 30, 50)
    
    # 데이터 결합
    all_data = np.vstack([premium_customers, regular_customers, budget_customers])
    labels = ['프리미엄'] * 70 + ['일반'] * 80 + ['절약형'] * 50
    
    # 데이터프레임 생성
    columns = ['구매빈도', '평균구매액', '충성도', '서비스만족도', '추천의향']
    df = pd.DataFrame(all_data, columns=columns)
    df['고객유형'] = labels
    
    # 데이터 정규화 (0-100 범위)
    for col in columns:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min()) * 100
    
    # 색상 설정
    colors = {'프리미엄': 'red', '일반': 'blue', '절약형': 'green'}
    
    # 평행 좌표 그리기
    for customer_type in df['고객유형'].unique():
        subset = df[df['고객유형'] == customer_type]
        
        for idx, row in subset.iterrows():
            values = [row[col] for col in columns]
            ax.plot(range(len(columns)), values, 
                   color=colors[customer_type], alpha=0.6, linewidth=1)
    
    # 범례용 더미 라인
    for customer_type, color in colors.items():
        ax.plot([], [], color=color, label=customer_type, linewidth=2)
    
    # 축 설정
    ax.set_xticks(range(len(columns)))
    ax.set_xticklabels(columns, rotation=45, fontsize=11)
    ax.set_ylabel('표준화된 점수 (0-100)', fontsize=12)
    
    # 제목 설정
    ax.set_title('평행 좌표를 활용한 고객 세그멘테이션\n"다차원 고객 특성 패턴 분석"', 
                fontsize=16, fontweight='bold', pad=20)
    
    # 범례 설정
    legend = ax.legend(title='고객 유형', fontsize=12, title_fontsize=12, loc='upper right')
    
    # 격자 설정
    ax.grid(True, alpha=0.3)
    
    # 레이아웃 조정
    plt.tight_layout()
    
    # 저장
    plt.savefig('images/parallel_coordinates_example.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    plt.close()

if __name__ == "__main__":
    create_parallel_coordinates()
    print("평행 좌표 그래프 생성 완료")