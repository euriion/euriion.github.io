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

def create_gapminder_style_chart():
    # Gapminder 스타일의 버블 차트 생성
    np.random.seed(42)
    
    # 가상의 국가 데이터 생성
    countries = ['한국', '미국', '중국', '독일', '브라질', '인도', '일본', '영국', 
                '프랑스', '러시아', '캐나다', '호주', '멕시코', '이탈리아', '스페인']
    
    # 대륙별 색상
    continent_colors = {
        '아시아': '#FF6B6B',
        '유럽': '#4ECDC4', 
        '북미': '#45B7D1',
        '남미': '#96CEB4',
        '오세아니아': '#FFEAA7'
    }
    
    continents = ['아시아', '북미', '아시아', '유럽', '남미', '아시아', '아시아', '유럽',
                 '유럽', '유럽', '북미', '오세아니아', '북미', '유럽', '유럽']
    
    # 데이터 생성
    gdp_per_capita = np.random.lognormal(9, 1, len(countries))  # GDP per capita
    life_expectancy = 50 + 30 * (gdp_per_capita / gdp_per_capita.max()) + np.random.normal(0, 3, len(countries))
    population = np.random.lognormal(15, 2, len(countries))  # Population
    
    # 버블 크기 정규화 (인구 기준)
    bubble_sizes = 100 + 2000 * (population / population.max())
    
    plt.figure(figsize=(14, 10))
    
    # 각 대륙별로 다른 색상으로 플롯
    for continent in continent_colors.keys():
        mask = np.array(continents) == continent
        if np.any(mask):
            plt.scatter(gdp_per_capita[mask], life_expectancy[mask], 
                       s=bubble_sizes[mask], alpha=0.6, 
                       c=continent_colors[continent], 
                       label=continent, edgecolors='white', linewidth=2)
    
    # 몇 개 국가 레이블 추가
    highlight_countries = ['한국', '미국', '중국', '독일', '브라질']
    for i, country in enumerate(countries):
        if country in highlight_countries:
            plt.annotate(country, (gdp_per_capita[i], life_expectancy[i]),
                        xytext=(5, 5), textcoords='offset points', 
                        fontsize=10, fontweight='bold')
    
    plt.xlabel('1인당 GDP (USD)', fontsize=14, fontweight='bold')
    plt.ylabel('기대수명 (년)', fontsize=14, fontweight='bold')
    plt.title('Gapminder 스타일: 소득과 건강의 관계\n(버블 크기 = 인구)', 
              fontsize=16, fontweight='bold', pad=20)
    
    # 로그 스케일 적용
    plt.xscale('log')
    plt.grid(True, alpha=0.3)
    
    # 범례
    plt.legend(title='대륙', loc='lower right', fontsize=12, title_fontsize=12)
    
    # 축 포맷팅
    plt.gca().set_xlim(500, 100000)
    plt.gca().set_ylim(45, 85)
    
    # x축 눈금 포맷
    from matplotlib.ticker import FuncFormatter
    def thousands(x, pos):
        if x >= 1000:
            return f'${x/1000:.0f}k'
        else:
            return f'${x:.0f}'
    plt.gca().xaxis.set_major_formatter(FuncFormatter(thousands))
    
    # 텍스트 박스 추가
    plt.text(0.02, 0.98, '"소득이 높을수록 수명이 길어진다"\n- Hans Rosling의 통찰', 
             transform=plt.gca().transAxes, fontsize=11, 
             verticalalignment='top', bbox=dict(boxstyle='round', 
             facecolor='wheat', alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('images/gapminder-style-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_gapminder_style_chart()
    print("Gapminder 스타일 차트 생성 완료!")