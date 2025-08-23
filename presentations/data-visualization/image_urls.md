# Image URLs

## 역사적 시각화 자료

### John Snow의 콜레라 지도 (1854)
- **파일명**: `snow-cholera-map.jpg`
- **설명**: 역사상 최초의 데이터 시각화 사례 중 하나. 런던 콜레라 발병 지역과 우물 위치를 지도에 표시하여 콜레라의 원인을 찾아낸 혁신적인 시각화
- **출처**: https://en.wikipedia.org/wiki/1854_Broad_Street_cholera_outbreak

### Florence Nightingale의 장미 다이어그램 (1858)
- **파일명**: `nightingale-rose-diagram.jpg`
- **설명**: 크림 전쟁 중 사망 원인을 시각화한 원형 차트. 질병으로 인한 사망이 전투로 인한 사망보다 많음을 보여줌
- **출처**: https://en.wikipedia.org/wiki/Florence_Nightingale#/media/File:Nightingale-mortality.jpg

### Napoleon의 러시아 원정 지도 (Charles Minard, 1869)
- **파일명**: `minard-napoleon-march.png`
- **설명**: Edward Tufte가 "역사상 최고의 통계 그래픽"이라고 평가한 작품. 시간, 위치, 온도, 군대 규모를 하나의 차트에 표현
- **출처**: https://en.wikipedia.org/wiki/Charles_Joseph_Minard#/media/File:Minard.png

## 현대 시각화 도구

### Gapminder 도구
- **파일명**: `gapminder-tools.png`, `gapminder-bubble-chart.jpg`
- **설명**: Hans Rosling의 Gapminder 프로젝트. 국가별 GDP와 기대수명 관계를 동적 버블 차트로 시각화
- **웹사이트**: https://www.gapminder.org/
- **출처**: https://www.gapminder.org/tools/

## 데이터 저널리즘

### 워싱턴 포스트 데이터 시각화
- **파일명**: `washington-post-dataviz.png`
- **설명**: 워싱턴 포스트의 데이터 저널리즘 사례. 선거, COVID-19, 기후변화, 사회 이슈 등을 다양한 차트로 시각화
- **출처**: https://www.washingtonpost.com/graphics/
- **특징**: 인터랙티브하고 실시간 업데이트되는 시각화

### MBC 선거 여론조사 벌집지도
- **파일명**: `mbc-hexagonal-map.png`, `mbc-kitogram.png`
- **설명**: MBC 2024년 총선 여론조사 결과를 벌집 모양 지도로 시각화. 지역별 정당 지지율을 색상으로 구분
- **출처**: https://poll-mbc.co.kr/poll2024/
- **특징**: 한국 지역별 선거 데이터의 혁신적 시각화

## 시각화 패러다임 예제

### Edward Tufte 스타일
- **파일명**: `tufte-style-chart.png`
- **설명**: 데이터-잉크 비율을 최대화한 미니멀 차트. 불필요한 요소를 제거하고 데이터에 집중
- **생성 스크립트**: `tufte-style-chart.py`

### D3.js 스타일
- **파일명**: `d3-style-chart.png`
- **설명**: 웹 기반 인터랙티브 시각화를 모방한 네트워크 그래프
- **생성 스크립트**: `d3-style-chart.py`

### ggplot2 스타일
- **파일명**: `ggplot-style-chart.png`
- **설명**: R의 ggplot2 패키지 스타일을 모방한 Grammar of Graphics 기반 차트
- **생성 스크립트**: `ggplot-style-chart.py`

## 인터랙티브 시각화 기법

### 호버 툴팁 (Hover Tooltips)
- **파일명**: `interactive/hover-tooltip.png`
- **설명**: 산점도에 마우스 오버 시 상세 정보를 제공하는 툴팁 기능을 시뮬레이션한 차트
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 차트 위 마우스 오버 시 추가 정보 표시

### 줌 및 팬 (Zoom and Pan)
- **파일명**: `interactive/zoom-pan.png`
- **설명**: 대용량 시계열 데이터에서 특정 구간을 확대/축소하고 이동할 수 있는 기능을 표현
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 시계열 데이터, 지도 데이터의 상세 탐색

### 동적 필터링 (Dynamic Filtering)
- **파일명**: `interactive/dynamic-filtering.png`
- **설명**: 실시간으로 데이터 조건을 변경하여 차트가 즉시 업데이트되는 기능을 표현
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 대시보드, 데이터 탐색 도구

### 연결된 뷰 (Linked Views)
- **파일명**: `interactive/linked-views.png`
- **설명**: 여러 차트가 서로 연동되어 한 차트의 선택이 다른 차트에 반영되는 기능
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 다각도 데이터 분석, 복합 대시보드

### 애니메이션 (Animation)
- **파일명**: `interactive/animation.png`
- **설명**: 시간에 따른 데이터 변화를 애니메이션으로 표현하는 기법 (정적 이미지로 여러 프레임 표시)
- **생성 방법**: Python matplotlib으로 생성
- **활용**: Gapminder 스타일 버블차트, 시간별 데이터 변화 시각화

## 베스트 프랙티스 (Best Practices)

### 색상 설계 가이드라인
- **파일명**: `best-practices/color-guidelines.png`
- **설명**: 순차적, 발산적, 범주형, 색각 이상자 친화적 색상 팔레트 예시를 한 눈에 보여주는 차트
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 색상 선택 전략과 접근성 고려사항 설명

### 레이아웃과 타이포그래피
- **파일명**: `best-practices/layout-typography.png`
- **설명**: 좋은 시각적 위계와 나쁜 예시, 적절한 그리드 시스템과 과도한 그리드 비교
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 시각적 위계 구성과 가독성 최적화 가이드

### 성능 최적화 전략
- **파일명**: `best-practices/performance-optimization.png`
- **설명**: 데이터 집계, 샘플링, 레벨 오브 디테일(LOD) 등 성능 최적화 기법들을 시각적으로 비교
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 대용량 데이터 처리와 렌더링 최적화 설명

### 접근성 고려사항
- **파일명**: `best-practices/accessibility.png`
- **설명**: 색상만 사용하는 경우와 색상+패턴을 함께 사용하는 경우, 명도 대비의 좋은 예와 나쁜 예 비교
- **생성 방법**: Python matplotlib으로 생성
- **활용**: 유니버설 디자인과 접근성 표준 설명

## 비즈니스 시각화 도구 (Business Tools)

### Microsoft Excel
- **파일명**: `business-tools/excel-visualization.png`
- **설명**: Excel의 대표적인 차트 유형들 (막대차트, 원형차트, 선차트, 표)을 Excel 스타일로 재현
- **생성 방법**: Python matplotlib으로 생성, Excel 고유의 색상 팔레트와 스타일 적용
- **활용**: Excel 시각화 기능과 실무 활용법 설명

### Tableau
- **파일명**: `business-tools/tableau-visualization.png`
- **설명**: Tableau의 강력한 시각화 기능들 (산점도 매트릭스, 히트맵, 다중 선차트, 스택차트)을 구현
- **생성 방법**: Python matplotlib으로 생성, Tableau 스타일의 색상과 레이아웃 적용
- **활용**: Tableau의 고급 시각화 기능과 비즈니스 가치 설명

### TIBCO Spotfire
- **파일명**: `business-tools/spotfire-visualization.png`
- **설명**: Spotfire의 고급 분석 기능들 (버블차트, 박스플롯, 트리맵, 평행좌표)을 시연
- **생성 방법**: Python matplotlib으로 생성, Spotfire의 분석적 접근법과 색상 체계 반영
- **활용**: 고급 분석 플랫폼의 차별화된 기능과 산업별 특화 설명

## 프로그래밍 언어 생태계 (Programming Languages)

### Python 생태계
- **파일명**: `programming-languages/python-ecosystem.png`
- **설명**: Python 시각화 라이브러리들의 특징을 보여주는 종합 차트 (matplotlib, seaborn, plotly 스타일과 생태계 요약)
- **생성 방법**: Python matplotlib으로 생성, 각 라이브러리의 고유 스타일 재현
- **스크립트**: `python-ecosystem-viz.py`
- **활용**: Python 기반 데이터 시각화 도구들의 특징과 철학 설명

### R 생태계  
- **파일명**: `programming-languages/r-ecosystem.png`
- **설명**: R의 ggplot2 중심 생태계와 패키지 네트워크, Shiny 대시보드, R 언어 특징을 시각화
- **생성 방법**: Python matplotlib으로 생성, ggplot2 스타일과 R 특유의 접근법 재현
- **스크립트**: `r-ecosystem-viz.py`
- **활용**: R 언어의 통계 중심 시각화 철학과 Grammar of Graphics 설명

### JavaScript 웹 기술
- **파일명**: `programming-languages/javascript-web-ecosystem.png`
- **설명**: D3.js 네트워크, Chart.js 반응형 차트, Three.js 3D 시각화, 웹 기술 스택을 종합 표현
- **생성 방법**: Python matplotlib으로 생성, 웹 기술의 시각적 특징과 브라우저 호환성 반영
- **스크립트**: `javascript-web-viz.py`
- **활용**: 웹 기반 시각화 기술의 장점과 현대적 접근법 설명

## AI 기반 시각화의 미래 (AI Future)

### GenBI 생태계
- **파일명**: `ai-future/genbi-ecosystem.png`
- **설명**: GenBI(Generative Business Intelligence) 워크플로우와 생태계를 4개 패널로 시각화. 자연어 쿼리 → 시각화 변환, AI 차트 추천 시스템, 인사이트 자동 발견, GenBI 프로세스 단계들을 포함
- **생성 방법**: Python matplotlib과 Malgun Gothic 폰트로 생성
- **스크립트**: `genbi-viz.py`
- **활용**: GenBI의 혁신적 특징과 자연어 기반 데이터 시각화 자동화 프로세스 설명
- **주요 구성요소**: 
  - 자연어 → 시각화 변환 과정 (한글 예시: "지난 3개월 매출 트렌드 지역별로 보여줘")
  - AI 추천 시스템 (막대차트, 선차트, 산점도, 히트맵 등 신뢰도 점수와 함께)
  - 인사이트 자동 발견 (시계열 데이터에서 패턴, 계절성, 예측 포인트 자동 감지)
  - GenBI 워크플로우 5단계 (자연어 질문 → 의도 파악 → 데이터 분석 → 차트 생성 → 인사이트 제공)

## 주의사항
- 모든 역사적 자료는 공개 도메인입니다
- 현대 도구 이미지는 교육 목적으로 사용됩니다
- 웹사이트 스크린샷은 해당 사이트의 저작권을 따릅니다
- 인터랙티브 시각화 이미지들은 Python matplotlib을 사용하여 교육 목적으로 생성되었습니다
- 베스트 프랙티스 이미지들은 Python matplotlib과 Malgun Gothic 폰트를 사용하여 교육 목적으로 생성되었습니다
- 비즈니스 도구 이미지들은 각 도구의 시각적 특징을 Python matplotlib으로 모방하여 교육 목적으로 생성되었습니다
- 프로그래밍 언어 생태계 이미지들은 각 언어의 시각화 철학과 특징을 Python matplotlib과 Malgun Gothic 폰트로 구현하여 교육 목적으로 생성되었습니다
