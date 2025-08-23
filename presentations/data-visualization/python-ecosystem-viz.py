import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

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

def create_python_ecosystem():
    """Python 생태계 시각화 이미지 생성"""
    
    # 프로그래밍 언어 이미지 저장 디렉토리 생성
    os.makedirs('images/programming-languages', exist_ok=True)
    
    print('Creating Python ecosystem visualization...')
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Matplotlib 스타일 차트
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    
    ax1.plot(x, y1, 'b-', label='sin(x)', linewidth=2)
    ax1.plot(x, y2, 'r--', label='cos(x)', linewidth=2)
    ax1.set_title('Matplotlib 스타일\n기본 라이브러리', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax1.set_xlabel('X 값', family='Malgun Gothic')
    ax1.set_ylabel('Y 값', family='Malgun Gothic')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Seaborn 스타일 히트맵 시뮬레이션
    np.random.seed(42)
    correlation_data = np.random.randn(6, 6)
    correlation_data = np.corrcoef(correlation_data)
    
    im = ax2.imshow(correlation_data, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    variables = ['변수1', '변수2', '변수3', '변수4', '변수5', '변수6']
    ax2.set_xticks(range(6))
    ax2.set_yticks(range(6))
    ax2.set_xticklabels(variables, family='Malgun Gothic')
    ax2.set_yticklabels(variables, family='Malgun Gothic')
    ax2.set_title('Seaborn 스타일\n통계적 시각화', fontsize=12, fontweight='bold', family='Malgun Gothic')
    
    # 상관계수 값 표시
    for i in range(6):
        for j in range(6):
            text = ax2.text(j, i, f'{correlation_data[i, j]:.2f}', 
                           ha='center', va='center', fontsize=8,
                           color='white' if abs(correlation_data[i, j]) > 0.5 else 'black')
    
    # 3. Plotly 스타일 인터랙티브 시뮬레이션
    categories = ['A', 'B', 'C', 'D', 'E']
    values1 = [23, 45, 56, 78, 32]
    values2 = [34, 25, 67, 45, 56]
    
    x_pos = np.arange(len(categories))
    width = 0.35
    
    bars1 = ax3.bar(x_pos - width/2, values1, width, label='시리즈 1', 
                   color='#1f77b4', alpha=0.8, edgecolor='black')
    bars2 = ax3.bar(x_pos + width/2, values2, width, label='시리즈 2', 
                   color='#ff7f0e', alpha=0.8, edgecolor='black')
    
    ax3.set_title('Plotly 스타일\n인터랙티브 차트', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax3.set_xlabel('카테고리', family='Malgun Gothic')
    ax3.set_ylabel('값', family='Malgun Gothic')
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(categories)
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # 값 레이블 추가
    for bar in bars1:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom', fontsize=9)
    
    for bar in bars2:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height}', ha='center', va='bottom', fontsize=9)
    
    # 4. 파이썬 라이브러리 생태계 요약
    ax4.axis('off')
    
    # 라이브러리 카테고리와 설명
    libraries = [
        ('matplotlib', '기본 플롯팅', '#1f77b4'),
        ('seaborn', '통계 시각화', '#ff7f0e'),
        ('plotly', '인터랙티브', '#2ca02c'),
        ('pandas', '데이터 분석', '#d62728'),
        ('bokeh', '웹 시각화', '#9467bd'),
        ('streamlit', '대시보드', '#8c564b')
    ]
    
    y_positions = np.linspace(0.9, 0.1, len(libraries))
    
    for i, (lib, desc, color) in enumerate(libraries):
        # 색상 박스
        ax4.add_patch(plt.Rectangle((0.1, y_positions[i]-0.05), 0.1, 0.08, 
                                   facecolor=color, alpha=0.7))
        # 라이브러리 이름
        ax4.text(0.25, y_positions[i], lib, fontsize=12, fontweight='bold', 
                va='center', family='Malgun Gothic')
        # 설명
        ax4.text(0.5, y_positions[i], desc, fontsize=10, 
                va='center', family='Malgun Gothic')
    
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_title('Python 시각화 생태계', fontsize=14, fontweight='bold', 
                 family='Malgun Gothic', y=0.95)
    
    plt.suptitle('Python 데이터 시각화 생태계', fontsize=16, fontweight='bold', 
                y=0.95, family='Malgun Gothic')
    plt.tight_layout()
    plt.savefig('images/programming-languages/python-ecosystem.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print('Created: python-ecosystem.png')

if __name__ == "__main__":
    create_python_ecosystem()
    print("Python ecosystem visualization created successfully!")