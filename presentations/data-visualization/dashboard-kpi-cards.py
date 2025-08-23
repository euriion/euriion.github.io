import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
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

def create_kpi_cards():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # KPI 카드 데이터
    kpis = [
        {"title": "총 매출", "value": "₩2.4B", "change": "+15.3%", "trend": "up", "mini_data": [100, 105, 103, 108, 112, 115, 118, 120, 125, 128, 135, 140]},
        {"title": "신규 고객", "value": "1,247", "change": "+8.7%", "trend": "up", "mini_data": [80, 85, 82, 88, 95, 98, 102, 105, 110, 108, 115, 120]},
        {"title": "고객 만족도", "value": "4.6/5.0", "change": "-2.1%", "trend": "down", "mini_data": [95, 96, 94, 92, 90, 88, 89, 91, 93, 92, 90, 89]},
        {"title": "전환율", "value": "12.3%", "change": "+5.2%", "trend": "up", "mini_data": [10, 11, 10.5, 11.2, 11.8, 12.1, 11.9, 12.3, 12.5, 12.2, 12.8, 13.1]}
    ]
    
    axes = [ax1, ax2, ax3, ax4]
    
    for ax, kpi in zip(axes, kpis):
        # 배경 카드
        card = FancyBboxPatch((0.05, 0.1), 0.9, 0.8, 
                             boxstyle="round,pad=0.02",
                             facecolor='white', 
                             edgecolor='lightgray',
                             linewidth=2)
        ax.add_patch(card)
        
        # 제목
        ax.text(0.1, 0.8, kpi["title"], fontsize=12, fontweight='bold', color='gray')
        
        # 메인 수치
        ax.text(0.1, 0.6, kpi["value"], fontsize=20, fontweight='bold', color='black')
        
        # 변화율
        change_color = 'green' if kpi["trend"] == 'up' else 'red'
        trend_symbol = '↗' if kpi["trend"] == 'up' else '↘'
        ax.text(0.1, 0.4, f"{trend_symbol} {kpi['change']}", fontsize=14, fontweight='bold', color=change_color)
        
        # 미니 차트 (스파크라인)
        mini_x = np.linspace(0.1, 0.9, len(kpi["mini_data"]))
        mini_y = np.array(kpi["mini_data"])
        # 정규화
        mini_y = 0.15 + (mini_y - mini_y.min()) / (mini_y.max() - mini_y.min()) * 0.15
        
        ax.plot(mini_x, mini_y, color=change_color, linewidth=2, alpha=0.7)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
    
    plt.suptitle('비즈니스 대시보드: KPI 카드 설계\n"핵심 지표를 한눈에 파악"', 
                fontsize=16, fontweight='bold', y=0.95)
    plt.tight_layout()
    plt.savefig('images/dashboard-kpi-cards.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_kpi_cards()
    print("대시보드 KPI 카드 생성 완료")