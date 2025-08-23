import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_area_chart():
    plt.figure(figsize=(14, 8))
    dates = pd.date_range('2023-01-01', '2024-12-01', freq='M')
    n_months = len(dates)
    np.random.seed(42)
    
    # 각 디바이스별로 시간에 따른 변동이 있는 데이터 생성
    # 모바일: 상승 트렌드 + 계절성 + 노이즈
    mobile_trend = np.linspace(25, 45, n_months)
    mobile_seasonal = 8 * np.sin(2 * np.pi * np.arange(n_months) / 12)
    mobile_noise = np.random.normal(0, 3, n_months)
    mobile = mobile_trend + mobile_seasonal + mobile_noise
    mobile = np.clip(mobile, 15, 60)
    
    # 데스크톱: 하락 트렌드 + 반대 계절성 + 노이즈
    desktop_trend = np.linspace(55, 35, n_months)
    desktop_seasonal = -5 * np.sin(2 * np.pi * np.arange(n_months) / 12)
    desktop_noise = np.random.normal(0, 4, n_months)
    desktop = desktop_trend + desktop_seasonal + desktop_noise
    desktop = np.clip(desktop, 25, 65)
    
    # 태블릿: 완만한 변화 + 작은 변동
    tablet_base = np.linspace(20, 15, n_months)
    tablet_noise = np.random.normal(0, 2, n_months)
    tablet = tablet_base + tablet_noise
    tablet = np.clip(tablet, 8, 25)
    
    # 비율 정규화 (합이 100이 되도록)
    total = mobile + desktop + tablet
    mobile = (mobile / total) * 100
    desktop = (desktop / total) * 100
    tablet = (tablet / total) * 100
    
    # 누적 영역 차트
    plt.fill_between(dates, 0, mobile, alpha=0.8, color='#ff6b6b', label='모바일')
    plt.fill_between(dates, mobile, mobile + desktop, alpha=0.8, color='#4ecdc4', label='데스크톱')
    plt.fill_between(dates, mobile + desktop, mobile + desktop + tablet, alpha=0.8, color='#45b7d1', label='태블릿')
    
    # 각 영역의 경계선 추가
    plt.plot(dates, mobile, color='#d63031', linewidth=2, alpha=0.8)
    plt.plot(dates, mobile + desktop, color='#00b894', linewidth=2, alpha=0.8)
    plt.plot(dates, mobile + desktop + tablet, color='#0984e3', linewidth=2, alpha=0.8)
    
    plt.title('월별 디바이스별 트래픽 비율 변화 (2년간)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('비율 (%)', fontsize=12)
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, alpha=0.3)
    
    # x축 포맷팅
    plt.xticks(dates[::3], [f"{m.year}-{m.month:02d}" for m in dates[::3]], rotation=45)
    plt.ylim(0, 100)
    
    plt.tight_layout()
    plt.savefig('images/area_chart_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_area_chart()
    print("에어리어 차트 생성 완료")