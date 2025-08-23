import matplotlib.pyplot as plt
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

def create_trend_analysis_chart():
    # 데이터 생성
    dates = pd.date_range('2024-01-01', '2024-12-31', freq='D')
    np.random.seed(42)
    
    # 매출 데이터 (계절성 + 트렌드 + 노이즈)
    base_trend = np.linspace(100, 150, len(dates))
    seasonal = 20 * np.sin(2 * np.pi * np.arange(len(dates)) / 365.25)
    weekly = 10 * np.sin(2 * np.pi * np.arange(len(dates)) / 7)
    noise = np.random.normal(0, 5, len(dates))
    revenue = base_trend + seasonal + weekly + noise
    
    # 고객 수 데이터
    customer_base = np.linspace(80, 120, len(dates))
    customer_seasonal = 15 * np.sin(2 * np.pi * np.arange(len(dates)) / 365.25 + np.pi/4)
    customer_noise = np.random.normal(0, 3, len(dates))
    customers = customer_base + customer_seasonal + customer_noise
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # 매출 트렌드
    ax1.plot(dates, revenue, color='#1f77b4', linewidth=2, label='일일 매출')
    
    # 7일 이동평균
    revenue_ma = pd.Series(revenue).rolling(window=7, center=True).mean()
    ax1.plot(dates, revenue_ma, color='#ff7f0e', linewidth=3, label='7일 이동평균')
    
    # 목표선
    ax1.axhline(y=125, color='red', linestyle='--', linewidth=2, alpha=0.7, label='목표 매출')
    
    # 주요 이벤트 마커
    event_dates = ['2024-03-15', '2024-07-01', '2024-11-15']
    event_labels = ['신제품 출시', '여름 프로모션', '블랙프라이데이']
    
    for date, label in zip(event_dates, event_labels):
        event_date = pd.to_datetime(date)
        if event_date in dates:
            idx = dates.get_loc(event_date)
            ax1.annotate(label, (event_date, revenue[idx]), 
                        xytext=(10, 10), textcoords='offset points',
                        bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.7),
                        arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    
    ax1.set_title('매출 트렌드 분석 (2024년)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('매출 (백만원)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 고객 수 트렌드
    ax2.fill_between(dates, customers, alpha=0.6, color='#2ca02c', label='신규 고객')
    ax2.plot(dates, customers, color='#2ca02c', linewidth=2)
    
    # 30일 이동평균
    customers_ma = pd.Series(customers).rolling(window=30, center=True).mean()
    ax2.plot(dates, customers_ma, color='#d62728', linewidth=3, label='30일 이동평균')
    
    ax2.set_title('신규 고객 획득 트렌드', fontsize=14, fontweight='bold')
    ax2.set_ylabel('신규 고객 수')
    ax2.set_xlabel('날짜')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.suptitle('대시보드: 트렌드 분석 차트\n"시간 흐름에 따른 핵심 지표 변화 추적"', 
                fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('images/dashboard-trend-analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_trend_analysis_chart()
    print("대시보드 트렌드 분석 차트 생성 완료")