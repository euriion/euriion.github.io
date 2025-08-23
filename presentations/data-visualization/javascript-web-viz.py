import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
from matplotlib.patches import Circle, FancyBboxPatch, Polygon
import matplotlib.patches as mpatches

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

def create_javascript_web_ecosystem():
    """JavaScript 웹 기술 생태계 시각화 이미지 생성"""
    
    # 프로그래밍 언어 이미지 저장 디렉토리 생성
    os.makedirs('images/programming-languages', exist_ok=True)
    
    print('Creating JavaScript web ecosystem visualization...')
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. D3.js 스타일 네트워크 그래프
    # 노드 위치 설정
    nodes = {
        'D3.js': (5, 5),
        'SVG': (2, 7),
        'Canvas': (8, 7),
        'WebGL': (2, 3),
        'DOM': (8, 3),
        'Data': (5, 1)
    }
    
    node_colors = {
        'D3.js': '#FF6B35',
        'SVG': '#004E89', 
        'Canvas': '#1A936F',
        'WebGL': '#C73E1D',
        'DOM': '#9A031E',
        'Data': '#FFB700'
    }
    
    # 연결 관계
    connections = [
        ('D3.js', 'SVG'), ('D3.js', 'Canvas'), ('D3.js', 'DOM'),
        ('D3.js', 'Data'), ('SVG', 'DOM'), ('Canvas', 'WebGL')
    ]
    
    # 연결선 그리기
    for start, end in connections:
        start_pos = nodes[start]
        end_pos = nodes[end]
        ax1.plot([start_pos[0], end_pos[0]], [start_pos[1], end_pos[1]], 
                'k-', alpha=0.4, linewidth=2)
    
    # 노드 그리기
    for node, pos in nodes.items():
        color = node_colors[node]
        ax1.add_patch(Circle(pos, 0.6, facecolor=color, alpha=0.8, edgecolor='black'))
        ax1.text(pos[0], pos[1], node, ha='center', va='center', 
                fontweight='bold', fontsize=9, family='Malgun Gothic')
    
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 8)
    ax1.set_title('D3.js 생태계\nData-Driven Documents', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_aspect('equal')
    
    # 2. Chart.js 스타일 반응형 차트
    categories = ['모바일', '태블릿', '데스크톱', '스마트TV']
    values = [45, 25, 25, 5]
    colors = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
    
    # 도넛 차트
    wedges, texts, autotexts = ax2.pie(values, labels=categories, colors=colors,
                                      autopct='%1.1f%%', startangle=90,
                                      wedgeprops=dict(width=0.5))
    
    ax2.set_title('Chart.js 스타일\n반응형 도넛 차트', fontsize=12, fontweight='bold', family='Malgun Gothic')
    
    # 중앙에 총합 표시
    ax2.text(0, 0, '총 100%\n디바이스 분포', ha='center', va='center', 
            fontweight='bold', fontsize=10, family='Malgun Gothic')
    
    # 3. Three.js 스타일 3D 시각화 시뮬레이션
    # 3D 효과를 위한 등축도법 시뮬레이션
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    
    # 3D 큐브들 그리기 (등축도법)
    cubes_data = [
        (2, 2, 3, '#FF6B35'),  # x, y, height, color
        (4, 3, 5, '#004E89'),
        (6, 1, 2, '#1A936F'),
        (3, 6, 4, '#C73E1D'),
        (7, 5, 6, '#9A031E'),
        (1, 7, 2, '#FFB700')
    ]
    
    for x, y, height, color in cubes_data:
        # 정면
        front = FancyBboxPatch((x, y), 1, height/2, boxstyle="round,pad=0.02",
                              facecolor=color, alpha=0.8, edgecolor='black')
        ax3.add_patch(front)
        
        # 상단 (3D 효과)
        top_points = np.array([[x, y+height/2], [x+0.3, y+height/2+0.3], 
                              [x+1.3, y+height/2+0.3], [x+1, y+height/2]])
        top = Polygon(top_points, facecolor=color, alpha=0.6, edgecolor='black')
        ax3.add_patch(top)
        
        # 측면 (3D 효과)
        side_points = np.array([[x+1, y], [x+1.3, y+0.3], 
                               [x+1.3, y+height/2+0.3], [x+1, y+height/2]])
        side = Polygon(side_points, facecolor=color, alpha=0.4, edgecolor='black')
        ax3.add_patch(side)
        
        # 높이 값 표시
        ax3.text(x+0.5, y+height/4, str(int(height*10)), ha='center', va='center',
                fontweight='bold', fontsize=8)
    
    ax3.set_title('Three.js 스타일\n3D 데이터 시각화', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax3.set_xticks([])
    ax3.set_yticks([])
    
    # 4. 웹 기술 스택 요약
    ax4.axis('off')
    
    # 웹 시각화 기술 스택
    tech_stack = [
        ('Frontend Libraries', '#FF6B35'),
        ('D3.js - 데이터 바인딩', '#004E89'),
        ('Chart.js - 간편 차트', '#1A936F'),
        ('Three.js - 3D 그래픽', '#C73E1D'),
        ('ApexCharts - 모던 차트', '#9A031E'),
        ('Observable - 노트북', '#FFB700')
    ]
    
    y_positions = np.linspace(0.9, 0.1, len(tech_stack))
    
    for i, (tech, color) in enumerate(tech_stack):
        if i == 0:  # 헤더
            ax4.text(0.5, y_positions[i], tech, ha='center', va='center',
                    fontsize=14, fontweight='bold', family='Malgun Gothic')
        else:
            # 기술 아이콘 (원형)
            circle = Circle((0.1, y_positions[i]), 0.05, facecolor=color, alpha=0.8)
            ax4.add_patch(circle)
            
            # 기술명
            ax4.text(0.25, y_positions[i], tech, ha='left', va='center',
                    fontsize=11, fontweight='bold', family='Malgun Gothic')
    
    # 웹 브라우저 호환성 표시
    browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
    browser_y = 0.3
    for i, browser in enumerate(browsers):
        x_pos = 0.1 + i * 0.2
        browser_box = FancyBboxPatch((x_pos-0.05, browser_y-0.05), 0.1, 0.08,
                                    boxstyle="round,pad=0.02", 
                                    facecolor='lightblue', alpha=0.6)
        ax4.add_patch(browser_box)
        ax4.text(x_pos, browser_y, browser, ha='center', va='center',
                fontsize=8, family='Malgun Gothic')
    
    ax4.text(0.5, 0.15, '브라우저 호환성', ha='center', va='center',
            fontsize=10, fontweight='bold', family='Malgun Gothic')
    
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_title('웹 시각화 기술 스택', fontsize=14, fontweight='bold', 
                 family='Malgun Gothic', y=0.95)
    
    plt.suptitle('JavaScript 웹 시각화 생태계', fontsize=16, fontweight='bold', 
                y=0.95, family='Malgun Gothic')
    plt.tight_layout()
    plt.savefig('images/programming-languages/javascript-web-ecosystem.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print('Created: javascript-web-ecosystem.png')

if __name__ == "__main__":
    create_javascript_web_ecosystem()
    print("JavaScript web ecosystem visualization created successfully!")