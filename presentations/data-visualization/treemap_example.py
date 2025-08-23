import matplotlib.pyplot as plt
import squarify

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def create_treemap():
    plt.figure(figsize=(12, 8))
    
    # 데이터 준비
    categories = ['전자제품', '의류', '식품', '도서', '화장품', '스포츠', '가구', '기타']
    sales = [450, 320, 280, 150, 180, 120, 200, 100]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc', '#c2c2f0', '#ffb3e6', '#c4e17f']
    
    # 트리맵 생성
    squarify.plot(sizes=sales, label=categories, color=colors, alpha=0.8, 
                 text_kwargs={'fontsize': 12, 'fontweight': 'bold'})
    
    plt.title('카테고리별 매출 비중', fontsize=16, fontweight='bold', pad=20)
    plt.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/treemap_example.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

if __name__ == "__main__":
    create_treemap()
    print("트리맵 생성 완료")