import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
from matplotlib.patches import Rectangle, FancyBboxPatch

# 한글 폰트 설정
font_list = [f.name for f in fm.fontManager.ttflist]
if 'Malgun Gothic' in font_list:
    plt.rcParams['font.family'] = 'Malgun Gothic'
    print("Using Malgun Gothic font")
else:
    # 대안 폰트들 시도
    alternatives = ['맑은 고딕', 'Microsoft YaHei', 'SimHei', 'Apple SD Gothic Neo']
    for alt in alternatives:
        if alt in font_list:
            plt.rcParams['font.family'] = alt
            print(f"Using alternative font: {alt}")
            break
    else:
        print("Warning: No Korean font found, using default")

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

def create_r_ecosystem():
    """R 생태계 시각화 이미지 생성"""
    
    # 프로그래밍 언어 이미지 저장 디렉토리 생성
    os.makedirs('images/programming-languages', exist_ok=True)
    
    print('Creating R ecosystem visualization...')
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. ggplot2 스타일 산점도
    np.random.seed(42)
    n_points = 100
    x = np.random.normal(50, 15, n_points)
    y = 2 * x + np.random.normal(0, 10, n_points)
    categories = np.random.choice(['그룹A', '그룹B', '그룹C'], n_points)
    
    colors_map = {'그룹A': '#E74C3C', '그룹B': '#3498DB', '그룹C': '#2ECC71'}
    
    for group in ['그룹A', '그룹B', '그룹C']:
        mask = categories == group
        ax1.scatter(x[mask], y[mask], c=colors_map[group], alpha=0.7, 
                   s=50, label=group, edgecolors='black', linewidth=0.5)
    
    ax1.set_title('ggplot2 스타일\nGrammar of Graphics', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax1.set_xlabel('X 변수', family='Malgun Gothic')
    ax1.set_ylabel('Y 변수', family='Malgun Gothic')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 추세선 추가
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    ax1.plot(x, p(x), "k--", alpha=0.8, linewidth=2)
    
    # 2. R 패키지 네트워크 시뮬레이션
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    
    # 중앙의 ggplot2
    center = (5, 5)
    ax2.add_patch(plt.Circle(center, 1, facecolor='#E74C3C', alpha=0.8, edgecolor='black'))
    ax2.text(center[0], center[1], 'ggplot2', ha='center', va='center', 
            fontweight='bold', fontsize=11, family='Malgun Gothic')
    
    # 주변 패키지들
    packages = [
        ('dplyr', (2, 7), '#3498DB'),
        ('tidyr', (8, 7), '#9B59B6'),
        ('patchwork', (2, 3), '#F39C12'),
        ('ggthemes', (8, 3), '#1ABC9C'),
        ('shiny', (5, 8.5), '#E67E22'),
        ('plotly', (5, 1.5), '#34495E')
    ]
    
    for pkg_name, pos, color in packages:
        ax2.add_patch(plt.Circle(pos, 0.7, facecolor=color, alpha=0.7, edgecolor='black'))
        ax2.text(pos[0], pos[1], pkg_name, ha='center', va='center', 
                fontweight='bold', fontsize=9, family='Malgun Gothic')
        # 연결선
        ax2.plot([center[0], pos[0]], [center[1], pos[1]], 'k-', alpha=0.5, linewidth=2)
    
    ax2.set_title('R 패키지 생태계\n상호 연결성', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_aspect('equal')
    
    # 3. Shiny 대시보드 시뮬레이션
    # 대시보드 레이아웃 시뮬레이션
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    
    # 헤더
    header = Rectangle((0.5, 8.5), 9, 1, facecolor='#2C3E50', alpha=0.8)
    ax3.add_patch(header)
    ax3.text(5, 9, 'Shiny 대시보드', ha='center', va='center', 
            color='white', fontweight='bold', fontsize=12, family='Malgun Gothic')
    
    # 사이드바
    sidebar = Rectangle((0.5, 2), 2, 6.5, facecolor='#34495E', alpha=0.6)
    ax3.add_patch(sidebar)
    ax3.text(1.5, 6, '입력\\n패널', ha='center', va='center', 
            color='white', fontweight='bold', fontsize=10, family='Malgun Gothic')
    
    # 메인 패널 - 차트들
    chart1 = Rectangle((3, 5.5), 6, 3, facecolor='#3498DB', alpha=0.6)
    ax3.add_patch(chart1)
    ax3.text(6, 7, '인터랙티브 차트', ha='center', va='center', 
            fontweight='bold', fontsize=11, family='Malgun Gothic')
    
    chart2 = Rectangle((3, 2), 2.8, 3, facecolor='#E74C3C', alpha=0.6)
    ax3.add_patch(chart2)
    ax3.text(4.4, 3.5, '표', ha='center', va='center', 
            fontweight='bold', fontsize=10, family='Malgun Gothic')
    
    chart3 = Rectangle((6.2, 2), 2.8, 3, facecolor='#2ECC71', alpha=0.6)
    ax3.add_patch(chart3)
    ax3.text(7.6, 3.5, 'KPI', ha='center', va='center', 
            fontweight='bold', fontsize=10, family='Malgun Gothic')
    
    ax3.set_title('Shiny 웹 애플리케이션\n인터랙티브 대시보드', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax3.set_xticks([])
    ax3.set_yticks([])
    
    # 4. R 생태계 특징 요약
    ax4.axis('off')
    
    # R 생태계의 특징들
    features = [
        ('통계 중심', 'Statistical Focus', '#E74C3C'),
        ('Grammar of Graphics', 'Layered Approach', '#3498DB'),
        ('CRAN 패키지', '15,000+ packages', '#2ECC71'),
        ('Tidyverse', 'Data Science Workflow', '#9B59B6'),
        ('Reproducible Research', 'R Markdown', '#F39C12'),
        ('Academic Community', 'Research Oriented', '#1ABC9C')
    ]
    
    y_positions = np.linspace(0.9, 0.1, len(features))
    
    for i, (feature_ko, feature_en, color) in enumerate(features):
        # 색상 박스
        fancy_box = FancyBboxPatch((0.05, y_positions[i]-0.05), 0.15, 0.08,
                                  boxstyle="round,pad=0.02", 
                                  facecolor=color, alpha=0.7, edgecolor='black')
        ax4.add_patch(fancy_box)
        
        # 한글 특징명
        ax4.text(0.25, y_positions[i], feature_ko, fontsize=11, fontweight='bold', 
                va='center', family='Malgun Gothic')
        # 영문 설명
        ax4.text(0.55, y_positions[i], feature_en, fontsize=9, 
                va='center', style='italic')
    
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_title('R 언어의 핵심 특징', fontsize=14, fontweight='bold', 
                 family='Malgun Gothic', y=0.95)
    
    plt.suptitle('R 데이터 시각화 생태계', fontsize=16, fontweight='bold', 
                y=0.95, family='Malgun Gothic')
    plt.tight_layout()
    plt.savefig('images/programming-languages/r-ecosystem.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print('Created: r-ecosystem.png')

if __name__ == "__main__":
    create_r_ecosystem()
    print("R ecosystem visualization created successfully!")