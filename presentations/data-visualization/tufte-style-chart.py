import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_tufte_style_chart():
    # Tufte 스타일의 미니멀한 차트 생성
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # 데이터
    years = [2019, 2020, 2021, 2022, 2023, 2024]
    values = [85, 72, 90, 105, 118, 135]
    
    # 선 그래프 (미니멀)
    ax.plot(years, values, 'k-', linewidth=1.5, marker='o', markersize=4, 
            markerfacecolor='white', markeredgecolor='black', markeredgewidth=1)
    
    # Tufte 스타일: 불필요한 요소 제거
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('gray')
    ax.spines['bottom'].set_linewidth(0.5)
    
    # 격자 제거
    ax.grid(False)
    
    # Y축 눈금 제거, X축만 유지
    ax.tick_params(left=False, right=False, top=False, bottom=True)
    ax.set_yticks([])
    
    # 데이터 포인트에 직접 라벨링 (data-ink ratio 최대화)
    for year, value in zip(years, values):
        ax.annotate(f'{value}', (year, value), textcoords="offset points", 
                   xytext=(0,8), ha='center', fontsize=9)
    
    # 제목과 설명
    ax.set_title('Tufte 스타일: 데이터-잉크 비율 최대화\n"불필요한 요소 제거로 데이터에 집중"', 
                fontsize=14, fontweight='bold', pad=20)
    ax.set_xlabel('연도', fontsize=11)
    
    # Y축 레이블을 오른쪽에 표시 (Tufte 스타일)
    ax.text(max(years) + 0.1, max(values), '매출 지수', 
            rotation=90, va='top', ha='left', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('images/tufte-style-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_tufte_style_chart()
    print("Tufte 스타일 차트 생성 완료")