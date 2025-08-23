import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
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

def create_eda_scatter_matrix():
    np.random.seed(42)
    
    # iris 스타일 데이터 생성
    n_samples = 150
    
    # 3개 그룹 생성
    group1 = np.random.multivariate_normal([5.0, 3.5, 1.5, 0.3], 
                                         [[0.3, 0.1, 0.1, 0.05],
                                          [0.1, 0.2, 0.05, 0.02],
                                          [0.1, 0.05, 0.3, 0.1],
                                          [0.05, 0.02, 0.1, 0.1]], 50)
    
    group2 = np.random.multivariate_normal([6.0, 2.8, 4.5, 1.4], 
                                         [[0.4, 0.1, 0.2, 0.1],
                                          [0.1, 0.3, 0.1, 0.05],
                                          [0.2, 0.1, 0.4, 0.2],
                                          [0.1, 0.05, 0.2, 0.2]], 50)
    
    group3 = np.random.multivariate_normal([6.5, 3.0, 5.5, 2.0], 
                                         [[0.5, 0.1, 0.3, 0.15],
                                          [0.1, 0.4, 0.15, 0.1],
                                          [0.3, 0.15, 0.5, 0.25],
                                          [0.15, 0.1, 0.25, 0.3]], 50)
    
    # 데이터 결합
    data = np.vstack([group1, group2, group3])
    labels = ['Group A'] * 50 + ['Group B'] * 50 + ['Group C'] * 50
    
    df = pd.DataFrame(data, columns=['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width'])
    df['Species'] = labels
    
    # 산점도 매트릭스 생성
    fig, axes = plt.subplots(4, 4, figsize=(12, 12))
    
    variables = df.columns[:-1]
    colors = ['red', 'blue', 'green']
    species = df['Species'].unique()
    
    for i, var1 in enumerate(variables):
        for j, var2 in enumerate(variables):
            ax = axes[i, j]
            
            if i == j:
                # 대각선: 히스토그램
                for k, spec in enumerate(species):
                    subset = df[df['Species'] == spec]
                    ax.hist(subset[var1], alpha=0.6, color=colors[k], label=spec, bins=15)
                ax.set_title(f'{var1}', fontsize=10, fontweight='bold')
                if i == 0:
                    ax.legend(fontsize=8)
            else:
                # 비대각선: 산점도
                for k, spec in enumerate(species):
                    subset = df[df['Species'] == spec]
                    ax.scatter(subset[var2], subset[var1], alpha=0.6, color=colors[k], s=20)
                
                if i == len(variables) - 1:
                    ax.set_xlabel(var2, fontsize=10)
                if j == 0:
                    ax.set_ylabel(var1, fontsize=10)
            
            ax.tick_params(labelsize=8)
            ax.grid(True, alpha=0.3)
    
    plt.suptitle('EDA: 산점도 매트릭스\n"모든 변수 쌍의 관계를 동시에 탐색"', 
                fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/eda-scatter-matrix.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_eda_scatter_matrix()
    print("EDA 산점도 매트릭스 생성 완료")