import matplotlib.pyplot as plt
import numpy as np

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_pie_chart():
    plt.figure(figsize=(8, 8))
    labels = ['모바일', '데스크톱', '태블릿', '기타']
    sizes = [45, 30, 20, 5]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, 
                                      autopct='%1.1f%%', startangle=90,
                                      textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    plt.title('디바이스별 접속 비율', fontsize=16, fontweight='bold', pad=20)
    
    # 퍼센트 텍스트 스타일링
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
        autotext.set_fontsize(11)
    
    plt.tight_layout()
    plt.savefig('images/pie_chart_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_pie_chart()
    print("원 차트 생성 완료")