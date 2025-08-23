import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle
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

def create_d3_style_chart():
    # D3.js 스타일의 인터랙티브한 느낌의 차트
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 노드 데이터 (네트워크 그래프 스타일)
    np.random.seed(42)
    n_nodes = 20
    
    # 중심점들
    centers = [(0.3, 0.7), (0.7, 0.7), (0.5, 0.3)]
    center_labels = ['웹', '모바일', '데스크톱']
    
    # 각 중심 주변에 노드들 배치
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, (center, label, color) in enumerate(zip(centers, center_labels, colors)):
        # 중심 노드
        circle = Circle(center, 0.08, facecolor=color, edgecolor='white', 
                       linewidth=3, alpha=0.9, zorder=10)
        ax.add_patch(circle)
        ax.text(center[0], center[1], label, ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white', zorder=11)
        
        # 주변 노드들
        for j in range(6):
            angle = j * np.pi / 3
            radius = 0.15 + np.random.normal(0, 0.03)
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)
            
            # 연결선
            ax.plot([center[0], x], [center[1], y], color=color, 
                   alpha=0.5, linewidth=1.5, zorder=1)
            
            # 작은 노드
            size = 0.02 + np.random.uniform(0, 0.02)
            small_circle = Circle((x, y), size, facecolor=color, 
                                alpha=0.7, zorder=5)
            ax.add_patch(small_circle)
    
    # 중심들 간의 연결
    for i in range(len(centers)):
        for j in range(i+1, len(centers)):
            ax.plot([centers[i][0], centers[j][0]], 
                   [centers[i][1], centers[j][1]], 
                   'gray', alpha=0.3, linewidth=2, linestyle='--', zorder=0)
    
    # D3 스타일 설정
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    
    # 배경색
    fig.patch.set_facecolor('#f8f9fa')
    ax.set_facecolor('#f8f9fa')
    
    # 제목
    plt.suptitle('D3.js 스타일: 인터랙티브 데이터 시각화\n"동적이고 인터랙티브한 웹 기반 시각화"', 
                fontsize=16, fontweight='bold', y=0.95)
    
    # 범례 (수동으로 생성)
    legend_y = 0.15
    for i, (label, color) in enumerate(zip(center_labels, colors)):
        circle = Circle((0.1, legend_y - i*0.05), 0.02, facecolor=color, alpha=0.9)
        ax.add_patch(circle)
        ax.text(0.15, legend_y - i*0.05, f'{label} 플랫폼', va='center', fontsize=10)
    
    plt.tight_layout()
    plt.savefig('images/d3-style-chart.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_d3_style_chart()
    print("D3 스타일 차트 생성 완료")