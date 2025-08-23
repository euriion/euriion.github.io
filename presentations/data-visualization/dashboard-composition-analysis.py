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

def create_composition_analysis():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. 매출 채널별 비중 (파이 차트)
    channels = ['온라인몰', '매장', '모바일앱', '전화주문', '기타']
    channel_values = [35, 28, 22, 10, 5]
    colors1 = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    
    wedges, texts, autotexts = ax1.pie(channel_values, labels=channels, colors=colors1, 
                                      autopct='%1.1f%%', startangle=90)
    ax1.set_title('매출 채널별 구성 비율', fontweight='bold', fontsize=12)
    
    # 2. 제품 카테고리별 수익 (도넛 차트)
    categories = ['전자제품', '의류', '가전', '도서', '기타']
    category_values = [180, 150, 120, 80, 70]
    colors2 = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    wedges, texts, autotexts = ax2.pie(category_values, labels=categories, colors=colors2,
                                      autopct='%1.1f%%', startangle=90, 
                                      pctdistance=0.85)
    
    # 도넛 차트를 위한 중앙 원
    from matplotlib.patches import Circle
    centre_circle = Circle((0,0), 0.70, fc='white')
    ax2.add_artist(centre_circle)
    ax2.text(0, 0, f'총 수익\n₩{sum(category_values)}M', ha='center', va='center', 
            fontsize=12, fontweight='bold')
    ax2.set_title('제품 카테고리별 수익', fontweight='bold', fontsize=12)
    
    # 3. 지역별 성과 (수평 막대 차트)
    regions = ['서울', '경기', '부산', '대구', '인천']
    region_values = [250, 180, 120, 90, 80]
    colors3 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    
    bars = ax3.barh(regions, region_values, color=colors3, alpha=0.8)
    ax3.set_title('지역별 매출 성과', fontweight='bold', fontsize=12)
    ax3.set_xlabel('매출 (백만원)')
    
    # 막대 위에 값 표시
    for bar, value in zip(bars, region_values):
        ax3.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, 
                f'₩{value}M', va='center', fontsize=10)
    
    # 4. 시간별 매출 구성 (스택 차트)
    months = ['1월', '2월', '3월', '4월', '5월', '6월']
    online = [40, 45, 50, 55, 60, 65]
    offline = [35, 38, 40, 42, 45, 48]
    mobile = [25, 28, 32, 35, 38, 42]
    
    ax4.bar(months, online, label='온라인', color='#ff9999', alpha=0.8)
    ax4.bar(months, offline, bottom=online, label='오프라인', color='#66b3ff', alpha=0.8)
    ax4.bar(months, mobile, bottom=np.array(online) + np.array(offline), 
           label='모바일', color='#99ff99', alpha=0.8)
    
    ax4.set_title('월별 채널 구성 변화', fontweight='bold', fontsize=12)
    ax4.set_ylabel('매출 (백만원)')
    ax4.legend()
    
    plt.suptitle('대시보드: 구성 비율 분석\n"전체 대비 각 부분의 기여도 시각화"', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/dashboard-composition-analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_composition_analysis()
    print("대시보드 구성 비율 분석 생성 완료")