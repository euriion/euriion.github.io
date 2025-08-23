import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
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

def create_ggplot_style_chart():
    # ggplot2 스타일의 차트 생성
    
    # seaborn의 whitegrid 스타일 사용 (ggplot과 유사)
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # 스타일 적용 후 폰트 다시 설정
    for font in font_candidates:
        try:
            plt.rcParams['font.family'] = font
            break
        except:
            continue
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. 산점도 with regression line (ggplot 스타일)
    np.random.seed(42)
    x1 = np.random.normal(50, 15, 100)
    y1 = 2 * x1 + np.random.normal(0, 10, 100)
    
    ax1.scatter(x1, y1, alpha=0.6, s=40, color='#3498db')
    z = np.polyfit(x1, y1, 1)
    p = np.poly1d(z)
    ax1.plot(x1, p(x1), color='#e74c3c', linewidth=2)
    ax1.set_title('산점도 + 회귀선', fontweight='bold')
    ax1.set_xlabel('X 변수')
    ax1.set_ylabel('Y 변수')
    
    # 2. 박스플롯 (카테고리별)
    categories = ['A', 'B', 'C', 'D']
    data = [np.random.normal(50, 10, 50), 
            np.random.normal(55, 12, 50),
            np.random.normal(48, 8, 50),
            np.random.normal(52, 15, 50)]
    
    box_plot = ax2.boxplot(data, labels=categories, patch_artist=True)
    colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
    for patch, color in zip(box_plot['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    
    ax2.set_title('카테고리별 분포', fontweight='bold')
    ax2.set_xlabel('카테고리')
    ax2.set_ylabel('값')
    
    # 3. 히스토그램 with density curve
    data3 = np.random.normal(100, 20, 1000)
    ax3.hist(data3, bins=30, alpha=0.7, color='#9b59b6', density=True, edgecolor='white')
    
    # 밀도 곡선 추가
    x_density = np.linspace(data3.min(), data3.max(), 100)
    y_density = (1/np.sqrt(2*np.pi*20**2)) * np.exp(-0.5*((x_density-100)/20)**2)
    ax3.plot(x_density, y_density, color='#34495e', linewidth=3)
    
    ax3.set_title('분포 히스토그램 + 밀도곡선', fontweight='bold')
    ax3.set_xlabel('값')
    ax3.set_ylabel('밀도')
    
    # 4. 그룹별 바 차트
    groups = ['그룹1', '그룹2', '그룹3']
    values_a = [23, 17, 35]
    values_b = [20, 25, 30]
    
    x = np.arange(len(groups))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, values_a, width, label='시리즈 A', 
                    color='#e74c3c', alpha=0.8)
    bars2 = ax4.bar(x + width/2, values_b, width, label='시리즈 B', 
                    color='#3498db', alpha=0.8)
    
    ax4.set_title('그룹별 비교', fontweight='bold')
    ax4.set_xlabel('그룹')
    ax4.set_ylabel('값')
    ax4.set_xticks(x)
    ax4.set_xticklabels(groups)
    ax4.legend()
    
    # 전체 제목
    plt.suptitle('ggplot2 스타일: Grammar of Graphics\n"체계적이고 일관된 시각화 문법"', 
                fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout()
    plt.savefig('images/ggplot-style-chart.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # 스타일 초기화
    plt.style.use('default')

if __name__ == "__main__":
    create_ggplot_style_chart()
    print("ggplot 스타일 차트 생성 완료")