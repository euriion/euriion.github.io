import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# 한글 폰트 설정 - 더 강화된 설정
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

def create_eda_tsne():
    np.random.seed(42)
    
    # 고차원 데이터 생성 (10차원)
    n_samples = 300
    n_features = 10
    n_centers = 4
    
    # 클러스터 데이터 생성
    X, y = make_blobs(n_samples=n_samples, centers=n_centers, 
                      n_features=n_features, random_state=42, 
                      cluster_std=1.5)
    
    # 표준화
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # PCA와 t-SNE 적용
    pca = PCA(n_components=2, random_state=42)
    X_pca = pca.fit_transform(X_scaled)
    
    tsne = TSNE(n_components=2, random_state=42, perplexity=30)
    X_tsne = tsne.fit_transform(X_scaled)
    
    # 시각화
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))
    
    colors = ['red', 'blue', 'green', 'orange']
    
    # 원본 데이터 (처음 2차원만)
    for i in range(n_centers):
        mask = y == i
        ax1.scatter(X[mask, 0], X[mask, 1], c=colors[i], alpha=0.6, 
                   label=f'Cluster {i+1}', s=30)
    ax1.set_title('원본 데이터 (처음 2차원)', fontweight='bold', fontsize=12, family='Malgun Gothic')
    ax1.set_xlabel('특성 1', fontsize=10, family='Malgun Gothic')
    ax1.set_ylabel('특성 2', fontsize=10, family='Malgun Gothic')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # PCA 결과
    for i in range(n_centers):
        mask = y == i
        ax2.scatter(X_pca[mask, 0], X_pca[mask, 1], c=colors[i], alpha=0.6, 
                   label=f'클러스터 {i+1}', s=30)
    ax2.set_title(f'PCA (분산 설명률: {pca.explained_variance_ratio_.sum():.1%})', 
                  fontweight='bold', fontsize=12, family='Malgun Gothic')
    ax2.set_xlabel('주성분 1', fontsize=10, family='Malgun Gothic')
    ax2.set_ylabel('주성분 2', fontsize=10, family='Malgun Gothic')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # t-SNE 결과
    for i in range(n_centers):
        mask = y == i
        ax3.scatter(X_tsne[mask, 0], X_tsne[mask, 1], c=colors[i], alpha=0.6, 
                   label=f'클러스터 {i+1}', s=30)
    ax3.set_title('t-SNE (지역 구조 보존)', fontweight='bold', fontsize=12, family='Malgun Gothic')
    ax3.set_xlabel('t-SNE 차원 1', fontsize=10, family='Malgun Gothic')
    ax3.set_ylabel('t-SNE 차원 2', fontsize=10, family='Malgun Gothic')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    plt.suptitle('EDA: 차원축소를 통한 고차원 데이터 탐색\n"10차원 → 2차원 변환으로 숨겨진 패턴 발견"', 
                fontsize=16, fontweight='bold', y=1.02, family='Malgun Gothic')
    
    plt.tight_layout()
    plt.savefig('images/eda-tsne.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    create_eda_tsne()
    print("EDA t-SNE dimension reduction image created successfully!")