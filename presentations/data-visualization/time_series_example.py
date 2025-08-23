import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_time_series():
    plt.figure(figsize=(12, 6))
    dates = pd.date_range('2023-01-01', '2024-12-31', freq='D')
    np.random.seed(42)
    
    # 트렌드와 계절성이 있는 데이터 생성
    trend = np.linspace(100, 200, len(dates))
    seasonal = 30 * np.sin(2 * np.pi * np.arange(len(dates)) / 365.25)
    noise = np.random.normal(0, 10, len(dates))
    values = trend + seasonal + noise
    
    plt.plot(dates, values, linewidth=1.5, color='#1f77b4', alpha=0.8)
    
    # 6개월 이동평균 추가
    moving_avg = pd.Series(values).rolling(window=180, center=True).mean()
    plt.plot(dates, moving_avg, linewidth=3, color='#ff7f0e', label='6개월 이동평균')
    
    plt.title('일일 웹사이트 방문자 수 (2년간)', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('날짜', fontsize=12)
    plt.ylabel('방문자 수', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('images/time_series_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_time_series()
    print("시계열 그래프 생성 완료")