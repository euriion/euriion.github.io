import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap

# 한글 폰트 설정 - 여러 옵션 시도
font_candidates = ['Malgun Gothic', 'NanumGothic', 'Batang', 'Gulim']
for font in font_candidates:
    try:
        plt.rcParams['font.family'] = font
        break
    except:
        continue

plt.rcParams['axes.unicode_minus'] = False

def create_washington_post_style():
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 1], width_ratios=[1, 1], 
                         hspace=0.4, wspace=0.3)
    
    # 1. 실시간 선거 여론조사 (스택 영역 차트)
    ax1 = fig.add_subplot(gs[0, 0])
    
    dates = pd.date_range('2024-02-01', '2024-03-01', freq='D')
    np.random.seed(42)
    
    # 후보별 지지율 데이터
    candidate_a = 40 + 15 * np.sin(np.linspace(0, 4*np.pi, len(dates))) + np.random.normal(0, 2, len(dates))
    candidate_b = 35 + 10 * np.cos(np.linspace(0, 3*np.pi, len(dates))) + np.random.normal(0, 2, len(dates))
    candidate_c = 100 - candidate_a - candidate_b
    
    ax1.fill_between(dates, 0, candidate_a, alpha=0.8, color='#4472C4', label='Candidate A')
    ax1.fill_between(dates, candidate_a, candidate_a + candidate_b, alpha=0.8, color='#E97132', label='Candidate B')
    ax1.fill_between(dates, candidate_a + candidate_b, 100, alpha=0.8, color='#70AD47', label='Candidate C')
    
    ax1.set_title('Real-time Election Polling', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Support (%)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. 주별 COVID-19 케이스 (히트맵)
    ax2 = fig.add_subplot(gs[0, 1])
    
    states = ['CA', 'TX', 'FL', 'NY', 'PA', 'IL', 'OH', 'GA', 'NC', 'MI']
    weeks = ['W1', 'W2', 'W3', 'W4', 'W5', 'W6']
    
    # 가상의 COVID 데이터
    covid_data = np.random.exponential(2000, (len(states), len(weeks)))
    covid_data[3, 3] = 8000  # NY W4에 핫스팟
    
    im = ax2.imshow(covid_data, cmap='Reds', aspect='auto')
    ax2.set_xticks(range(len(weeks)))
    ax2.set_xticklabels(weeks)
    ax2.set_yticks(range(len(states)))
    ax2.set_yticklabels(states)
    ax2.set_title('COVID-19 Cases by State', fontsize=14, fontweight='bold')
    
    # 컬러바
    cbar = plt.colorbar(im, ax=ax2, shrink=0.8)
    cbar.set_label('Daily Cases')
    
    # 3. 지구 온도 이상 (막대 차트)
    ax3 = fig.add_subplot(gs[1, :])
    
    years = np.arange(1900, 2025)
    np.random.seed(42)
    temp_anomaly = np.random.normal(0, 0.3, len(years))
    
    # 1980년 이후 온난화 트렌드 추가
    warming_trend = np.where(years >= 1980, (years - 1980) * 0.02, 0)
    temp_anomaly += warming_trend
    
    colors = ['blue' if x < 0 else 'red' for x in temp_anomaly]
    bars = ax3.bar(years, temp_anomaly, color=colors, alpha=0.7, width=0.8)
    
    ax3.axhline(y=0, color='black', linewidth=1)
    ax3.set_title('Global Temperature Anomaly', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Year')
    ax3.set_ylabel('Temperature Anomaly (°C)')
    ax3.grid(True, alpha=0.3)
    
    # 4. 도시별 총기 폭력 사건 (버블 차트)
    ax4 = fig.add_subplot(gs[2, :])
    
    cities = ['NYC', 'LA', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio']
    np.random.seed(42)
    
    geographic_dist = np.random.normal(0, 1, len(cities))
    regional_clusters = np.random.normal(0, 0.5, len(cities))
    incidents = np.random.exponential(15, len(cities))
    
    # 버블 크기와 색상
    bubble_sizes = incidents * 50
    scatter = ax4.scatter(geographic_dist, regional_clusters, s=bubble_sizes, 
                         c=incidents, cmap='Reds', alpha=0.7, edgecolors='black')
    
    # 도시 라벨
    for i, city in enumerate(cities):
        ax4.annotate(city, (geographic_dist[i], regional_clusters[i]), 
                    xytext=(5, 5), textcoords='offset points', fontsize=10)
    
    ax4.set_title('Gun Violence Incidents by City', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Geographic Distribution')
    ax4.set_ylabel('Regional Clusters')
    
    # 컬러바
    cbar2 = plt.colorbar(scatter, ax=ax4, shrink=0.8)
    cbar2.set_label('Incidents')
    
    # 전체 제목
    plt.suptitle('Washington Post Style: Data Journalism Visualization\n데이터 저널리즘 시각화', 
                fontsize=18, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('images/washington-post-dataviz.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_washington_post_style()
    print("워싱턴 포스트 스타일 차트 생성 완료")