import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, Arrow
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

def create_genbi_visualization():
    """GenBI(Generative Business Intelligence) 시각화 이미지 생성"""
    
    # AI 기술 이미지 저장 디렉토리 생성
    os.makedirs('images/ai-future', exist_ok=True)
    
    print('Creating GenBI visualization...')
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. 자연어 쿼리 → 시각화 변환 과정
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    
    # 자연어 입력
    input_box = FancyBboxPatch((0.5, 7), 4, 1.5, boxstyle="round,pad=0.1",
                              facecolor='lightblue', edgecolor='navy', linewidth=2)
    ax1.add_patch(input_box)
    ax1.text(2.5, 7.75, '"지난 3개월 매출 트렌드\\n지역별로 보여줘"', 
            ha='center', va='center', fontsize=10, fontweight='bold', family='Malgun Gothic')
    
    # AI 처리 단계
    ai_box = FancyBboxPatch((5.5, 7), 3.5, 1.5, boxstyle="round,pad=0.1",
                           facecolor='gold', edgecolor='orange', linewidth=2)
    ax1.add_patch(ai_box)
    ax1.text(7.25, 7.75, 'GenAI 처리\\n의도 분석 + 차트 생성', 
            ha='center', va='center', fontsize=9, fontweight='bold', family='Malgun Gothic')
    
    # 화살표
    arrow1 = mpatches.FancyArrowPatch((4.5, 7.75), (5.5, 7.75),
                                     arrowstyle='->', mutation_scale=20, color='darkgreen')
    ax1.add_patch(arrow1)
    
    # 생성된 차트 (간단한 막대 차트)
    chart_x = [1, 2, 3, 4]
    chart_y = [25, 30, 35, 28]
    regions = ['서울', '부산', '대구', '인천']
    
    bars = ax1.bar([x+0.5 for x in chart_x], [y*0.15 for y in chart_y], 
                  width=0.6, color=['#FF6B35', '#004E89', '#1A936F', '#C73E1D'], alpha=0.8)
    
    for i, (x, y, region) in enumerate(zip(chart_x, chart_y, regions)):
        ax1.text(x+0.5, y*0.15 + 0.2, region, ha='center', va='bottom', 
                fontsize=8, family='Malgun Gothic')
        ax1.text(x+0.5, y*0.15 + 0.8, f'{y}M', ha='center', va='bottom', 
                fontsize=8, fontweight='bold')
    
    ax1.set_title('GenBI: 자연어 → 시각화 자동 생성', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax1.set_xticks([])
    ax1.set_yticks([])
    
    # 2. AI 추천 시스템
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    
    # 중앙의 데이터
    data_circle = Circle((5, 6), 1, facecolor='lightcoral', alpha=0.8, edgecolor='darkred')
    ax2.add_patch(data_circle)
    ax2.text(5, 6, '데이터셋', ha='center', va='center', fontsize=11, 
            fontweight='bold', family='Malgun Gothic')
    
    # AI 추천 차트들
    recommendations = [
        ('막대차트', (2, 8.5), '#FF6B35'),
        ('선차트', (8, 8.5), '#004E89'),
        ('산점도', (2, 3.5), '#1A936F'),
        ('히트맵', (8, 3.5), '#C73E1D')
    ]
    
    for i, (chart_type, pos, color) in enumerate(recommendations):
        # 차트 박스
        chart_box = FancyBboxPatch((pos[0]-0.7, pos[1]-0.4), 1.4, 0.8,
                                  boxstyle="round,pad=0.05", facecolor=color, 
                                  alpha=0.7, edgecolor='black')
        ax2.add_patch(chart_box)
        ax2.text(pos[0], pos[1], chart_type, ha='center', va='center',
                fontsize=9, fontweight='bold', family='Malgun Gothic')
        
        # 신뢰도 점수
        confidence = np.random.randint(75, 95)
        ax2.text(pos[0], pos[1]-0.8, f'{confidence}%', ha='center', va='center',
                fontsize=8, style='italic', family='Malgun Gothic')
        
        # 연결선
        ax2.plot([5, pos[0]], [6, pos[1]], 'k--', alpha=0.5, linewidth=1)
    
    ax2.set_title('AI 차트 추천 시스템\\n적합도 기반 자동 제안', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    # 3. 인사이트 자동 발견
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    
    # 시계열 데이터 시뮬레이션
    months = np.arange(1, 13)
    sales = [100, 105, 98, 110, 125, 140, 135, 150, 145, 160, 155, 170]
    
    ax3.plot(months, [s*0.05 for s in sales], 'b-', linewidth=3, marker='o', markersize=4)
    
    # AI가 발견한 인사이트 포인트들
    insights = [
        (6, 140*0.05, '피크 시즌\\n40% 증가', 'red'),
        (9, 145*0.05, '계절성 패턴\\n3개월 주기', 'green'),
        (12, 170*0.05, '연말 급증\\n예측 달성', 'blue')
    ]
    
    for month, value, insight, color in insights:
        # 인사이트 포인트 강조
        ax3.scatter([month], [value], s=200, c=color, alpha=0.7, edgecolors='black', linewidth=2)
        
        # 인사이트 박스
        if month <= 6:
            box_x = month + 0.5
        else:
            box_x = month - 2
            
        insight_box = FancyBboxPatch((box_x, value + 0.5), 2, 1,
                                    boxstyle="round,pad=0.1", facecolor=color, 
                                    alpha=0.3, edgecolor=color, linewidth=1)
        ax3.add_patch(insight_box)
        ax3.text(box_x + 1, value + 1, insight, ha='center', va='center',
                fontsize=8, fontweight='bold', family='Malgun Gothic')
        
        # 연결선
        ax3.plot([month, box_x + 1], [value, value + 0.5], 
                color=color, linestyle='--', alpha=0.7)
    
    ax3.set_title('AI 인사이트 자동 발견\\n패턴 감지 + 예측', fontsize=12, fontweight='bold', family='Malgun Gothic')
    ax3.set_xlabel('월', family='Malgun Gothic')
    ax3.set_ylabel('매출 지수', family='Malgun Gothic')
    ax3.grid(True, alpha=0.3)
    
    # 4. GenBI 워크플로우
    ax4.axis('off')
    
    # GenBI 프로세스 단계들
    workflow_steps = [
        ('1. 자연어 질문', 0.8, '#FF6B35'),
        ('2. 의도 파악', 0.65, '#004E89'),
        ('3. 데이터 분석', 0.5, '#1A936F'),
        ('4. 차트 생성', 0.35, '#C73E1D'),
        ('5. 인사이트 제공', 0.2, '#9A031E')
    ]
    
    for i, (step, y_pos, color) in enumerate(workflow_steps):
        # 단계 박스
        step_box = FancyBboxPatch((0.1, y_pos-0.05), 0.8, 0.08,
                                 boxstyle="round,pad=0.02", facecolor=color, 
                                 alpha=0.8, edgecolor='black')
        ax4.add_patch(step_box)
        
        ax4.text(0.5, y_pos, step, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white', family='Malgun Gothic')
        
        # 화살표 (마지막 단계 제외)
        if i < len(workflow_steps) - 1:
            arrow = mpatches.FancyArrowPatch((0.5, y_pos-0.05), (0.5, y_pos-0.08),
                                           arrowstyle='->', mutation_scale=15, 
                                           color='darkgray')
            ax4.add_patch(arrow)
    
    # GenBI의 특징
    features_text = '''
GenBI 핵심 특징:
• 자연어 인터페이스
• 실시간 차트 생성
• 컨텍스트 이해
• 자동 인사이트 발견
• 대화형 분석
    '''
    
    ax4.text(0.05, 0.05, features_text.strip(), ha='left', va='bottom',
            fontsize=9, family='Malgun Gothic', 
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.3))
    
    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.set_title('GenBI 워크플로우', fontsize=14, fontweight='bold', 
                 family='Malgun Gothic', y=0.95)
    
    plt.suptitle('GenBI: 생성형 비즈니스 인텔리전스', fontsize=16, fontweight='bold', 
                y=0.95, family='Malgun Gothic')
    plt.tight_layout()
    plt.savefig('images/ai-future/genbi-ecosystem.png', dpi=150, bbox_inches='tight')
    plt.close()
    
    print('Created: genbi-ecosystem.png')

if __name__ == "__main__":
    create_genbi_visualization()
    print("GenBI visualization created successfully!")