import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_line_chart():
    plt.figure(figsize=(10, 6))
    months = ['1월', '2월', '3월', '4월', '5월', '6월']
    sales_2023 = [120, 135, 148, 162, 178, 195]
    sales_2024 = [140, 155, 171, 188, 205, 225]
    
    plt.plot(months, sales_2023, marker='o', linewidth=3, label='2023년', color='#1f77b4', markersize=8)
    plt.plot(months, sales_2024, marker='s', linewidth=3, label='2024년', color='#ff7f0e', markersize=8)
    
    plt.title('월별 매출 추이', fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('월', fontsize=12)
    plt.ylabel('매출 (백만원)', fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/line_chart_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_line_chart()
    print("선 차트 생성 완료")