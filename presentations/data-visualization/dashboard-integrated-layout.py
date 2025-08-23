import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Rectangle
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

def create_integrated_dashboard():
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(4, 4, height_ratios=[1, 1, 1.5, 1.5], hspace=0.3, wspace=0.3)
    
    # 상단: KPI 카드들
    kpi_positions = [(0, 0), (0, 1), (0, 2), (0, 3)]
    kpi_data = [
        {'title': '총 매출', 'value': '₩2.4B', 'change': '+15.3%', 'color': '#4CAF50'},
        {'title': '신규고객', 'value': '1,247', 'change': '+8.7%', 'color': '#2196F3'},
        {'title': '전환율', 'value': '12.3%', 'change': '+5.2%', 'color': '#FF9800'},
        {'title': '만족도', 'value': '4.6/5', 'change': '-2.1%', 'color': '#F44336'}
    ]
    
    for pos, kpi in zip(kpi_positions, kpi_data):
        ax = fig.add_subplot(gs[pos[0], pos[1]])
        
        # KPI 카드 배경
        ax.add_patch(Rectangle((0, 0), 1, 1, facecolor='white', 
                              edgecolor='lightgray', linewidth=1))
        
        # 내용
        ax.text(0.1, 0.8, kpi['title'], fontsize=10, fontweight='bold', color='gray')
        ax.text(0.1, 0.5, kpi['value'], fontsize=14, fontweight='bold', color='black')
        ax.text(0.1, 0.2, kpi['change'], fontsize=10, fontweight='bold', color=kpi['color'])
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    # 중간 왼쪽: 트렌드 차트
    ax_trend = fig.add_subplot(gs[1:3, 0:2])
    dates = pd.date_range('2024-01-01', '2024-06-30', freq='D')
    trend_data = 100 + np.cumsum(np.random.normal(0.2, 1, len(dates)))
    ax_trend.plot(dates, trend_data, color='#2196F3', linewidth=2)
    ax_trend.fill_between(dates, trend_data, alpha=0.3, color='#2196F3')
    ax_trend.set_title('매출 트렌드 (6개월)', fontweight='bold', fontsize=12)
    ax_trend.set_ylabel('매출 (백만원)')
    ax_trend.grid(True, alpha=0.3)
    ax_trend.tick_params(axis='x', rotation=45)
    
    # 중간 오른쪽: 구성 비율
    ax_pie = fig.add_subplot(gs[1:3, 2:4])
    labels = ['온라인', '매장', '모바일', '기타']
    sizes = [35, 30, 25, 10]
    colors = ['#FF9800', '#4CAF50', '#2196F3', '#9E9E9E']
    
    wedges, texts, autotexts = ax_pie.pie(sizes, labels=labels, colors=colors,
                                         autopct='%1.1f%%', startangle=90)
    ax_pie.set_title('채널별 매출 비중', fontweight='bold', fontsize=12)
    
    # 하단 왼쪽: 지역별 성과
    ax_region = fig.add_subplot(gs[3, 0:2])
    regions = ['서울', '경기', '부산', '대구', '인천']
    region_values = [250, 180, 120, 90, 80]
    bars = ax_region.bar(regions, region_values, color='#4CAF50', alpha=0.8)
    ax_region.set_title('지역별 매출', fontweight='bold', fontsize=12)
    ax_region.set_ylabel('매출 (백만원)')
    
    # 막대 위에 값 표시
    for bar, value in zip(bars, region_values):
        ax_region.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                      f'{value}M', ha='center', va='bottom', fontsize=9)
    
    # 하단 오른쪽: 최근 활동
    ax_activity = fig.add_subplot(gs[3, 2:4])
    
    # 테이블 형태의 최근 활동
    activities = [
        '신규 프로모션 시작',
        '모바일 앱 업데이트',
        '고객 만족도 조사',
        '신제품 출시 예정',
        '마케팅 캠페인 론칭'
    ]
    
    for i, activity in enumerate(activities):
        y_pos = 0.9 - i * 0.15
        ax_activity.text(0.05, y_pos, f'• {activity}', fontsize=9, va='center')
        ax_activity.text(0.85, y_pos, '방금', fontsize=8, va='center', color='gray')
    
    ax_activity.set_title('최근 활동', fontweight='bold', fontsize=12)
    ax_activity.set_xlim(0, 1)
    ax_activity.set_ylim(0, 1)
    ax_activity.axis('off')
    
    # 전체 제목
    fig.suptitle('비즈니스 대시보드: 통합 관제판\n"모든 핵심 지표를 한 화면에"', 
                fontsize=18, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('images/dashboard-integrated-layout.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_integrated_dashboard()
    print("대시보드 통합 레이아웃 생성 완료")