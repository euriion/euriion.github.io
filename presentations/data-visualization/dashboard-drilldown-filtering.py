import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
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

def create_drilldown_filtering():
    fig = plt.figure(figsize=(14, 10))
    gs = fig.add_gridspec(3, 3, height_ratios=[1, 2, 2], width_ratios=[1, 1, 1])
    
    # 상단: 필터 인터페이스
    ax_filter = fig.add_subplot(gs[0, :])
    ax_filter.text(0.1, 0.7, '필터 옵션:', fontsize=12, fontweight='bold')
    
    # 필터 박스들 그리기
    filter_boxes = [
        {'pos': (0.2, 0.3), 'text': '지역: 전체', 'color': '#e8f4fd'},
        {'pos': (0.35, 0.3), 'text': '기간: 2024년', 'color': '#e8f4fd'},
        {'pos': (0.5, 0.3), 'text': '제품: 전체', 'color': '#e8f4fd'},
        {'pos': (0.65, 0.3), 'text': '채널: 전체', 'color': '#e8f4fd'},
        {'pos': (0.8, 0.3), 'text': '초기화', 'color': '#ffebee'}
    ]
    
    for box in filter_boxes:
        filter_box = FancyBboxPatch((box['pos'][0]-0.06, box['pos'][1]-0.15), 0.12, 0.3,
                                   boxstyle="round,pad=0.01", 
                                   facecolor=box['color'], 
                                   edgecolor='#1976d2',
                                   linewidth=1)
        ax_filter.add_patch(filter_box)
        ax_filter.text(box['pos'][0], box['pos'][1], box['text'], 
                      ha='center', va='center', fontsize=9)
    
    ax_filter.set_xlim(0, 1)
    ax_filter.set_ylim(0, 1)
    ax_filter.axis('off')
    
    # 중간: 지역별 개요 (클릭 가능한 맵 스타일)
    ax_overview = fig.add_subplot(gs[1, :])
    
    regions = ['서울', '경기', '부산', '대구', '인천', '광주', '대전']
    values = [250, 180, 120, 90, 80, 70, 65]
    positions = [(0.2, 0.8), (0.3, 0.6), (0.2, 0.2), (0.4, 0.3), 
                (0.15, 0.7), (0.1, 0.3), (0.35, 0.45)]
    
    # 선택된 지역 표시
    selected_region = '서울'
    
    for i, (region, value, pos) in enumerate(zip(regions, values, positions)):
        # 지역 박스
        size = 0.08 + (value / max(values)) * 0.05
        color = '#ff7f0e' if region == selected_region else '#1f77b4'
        alpha = 1.0 if region == selected_region else 0.7
        
        region_box = FancyBboxPatch((pos[0]-size/2, pos[1]-size/2), size, size,
                                   boxstyle="round,pad=0.01",
                                   facecolor=color, 
                                   edgecolor='white',
                                   linewidth=2,
                                   alpha=alpha)
        ax_overview.add_patch(region_box)
        
        # 지역명과 값
        ax_overview.text(pos[0], pos[1], region, ha='center', va='center', 
                        fontsize=9, fontweight='bold', color='white')
        ax_overview.text(pos[0], pos[1]-0.08, f'₩{value}M', ha='center', va='top', 
                        fontsize=8, color='black')
    
    ax_overview.set_title('지역별 매출 현황 (클릭하여 상세 보기)', fontweight='bold', fontsize=12)
    ax_overview.text(0.7, 0.8, f'선택된 지역: {selected_region}', 
                    bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.7),
                    fontsize=11, fontweight='bold')
    ax_overview.set_xlim(0, 1)
    ax_overview.set_ylim(0, 1)
    ax_overview.axis('off')
    
    # 하단: 상세 분석 (선택된 지역의 세부 데이터)
    ax_detail1 = fig.add_subplot(gs[2, 0])
    ax_detail2 = fig.add_subplot(gs[2, 1])
    ax_detail3 = fig.add_subplot(gs[2, 2])
    
    # 서울 지역 월별 매출
    months = ['1월', '2월', '3월', '4월', '5월', '6월']
    seoul_sales = [20, 22, 25, 28, 30, 35]
    ax_detail1.bar(months, seoul_sales, color='#ff7f0e', alpha=0.8)
    ax_detail1.set_title(f'{selected_region} 월별 매출', fontweight='bold', fontsize=11)
    ax_detail1.set_ylabel('매출 (백만원)')
    ax_detail1.tick_params(axis='x', rotation=45)
    
    # 서울 지역 제품별 분포
    products = ['전자제품', '의류', '가전', '기타']
    seoul_products = [100, 80, 50, 20]
    ax_detail2.pie(seoul_products, labels=products, autopct='%1.1f%%', 
                  colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99'])
    ax_detail2.set_title(f'{selected_region} 제품별 비중', fontweight='bold', fontsize=11)
    
    # 서울 지역 채널별 성과
    channels = ['온라인', '매장', '모바일']
    seoul_channels = [120, 80, 50]
    bars = ax_detail3.barh(channels, seoul_channels, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    ax_detail3.set_title(f'{selected_region} 채널별 매출', fontweight='bold', fontsize=11)
    ax_detail3.set_xlabel('매출 (백만원)')
    
    plt.suptitle('대시보드: 드릴다운 필터링\n"전체에서 상세로, 인터랙티브 데이터 탐색"', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/dashboard-drilldown-filtering.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_drilldown_filtering()
    print("대시보드 드릴다운 필터링 생성 완료")