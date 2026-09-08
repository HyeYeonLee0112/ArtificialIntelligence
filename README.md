# 인공지능 · Artificial Intelligence

> 강의 개념을 손계산과 작은 코드로 확인하고, 조건을 바꾼 실험 결과를 설명 가능한 보고서와 재현 가능한 코드로 남긴다.

## 프로젝트 목표

이 저장소는 강의 내용을 요약하는 노트가 아니라 **개념 → 구현 → 측정 → 해석**의 증거를 쌓는 학기 프로젝트다. 매주 작은 실험을 완성하고, 학기말에는 주요 모델의 동작 원리와 실패 원인을 직접 설명할 수 있는 포트폴리오로 묶는다.

### 학습 흐름

`직관적 개념` → `필요한 수식·손계산` → `NumPy/PyTorch 최소 실험` → `그래프·오류 분석` → `회상 문제`

한 실험에서는 가능한 한 조건 하나만 바꾼다. 그래야 결과 차이가 어떤 선택에서 생겼는지 설명할 수 있다.

### 주차별 완료 계약

한 주차는 아래 증거가 모두 있어야 완료(✅)로 바꾼다.

- `experiments/wkNN/`: 다시 실행할 수 있는 최소 실험
- `tests/`: 핵심 계산이나 동작을 확인하는 테스트
- `report_assets/wkNN/`: 비교 표·그래프·구조 그림
- `reports/REPORT_wkNN.md`: 질문, 조건, 결과, 오류 원인, 다음 실험
- 해당 GitHub 이슈: 체크리스트, 실행 명령, 결과 링크, 회상 답변

평가 과제의 답안을 미리 완성하지 않는다. 먼저 빈칸·힌트·의사코드로 구현하고, 본인이 작성한 코드를 리뷰받는다.

## 커리큘럼 & 구현 현황

**상태** ⬜ 예정 · 🟨 진행 · ✅ 완료
**깊이** `📖 개념` · `✏️ 손계산` · `🔨 구현+테스트` · `📊 실험+측정` · `⚡ 조건 비교·해석`

### 강의 범위

| 주제 | 상태 | 깊이 | 증거 |
|---|:--:|:--:|---|
| 고전 AI: 상태공간·게임 탐색·규칙 추론 (DFS·BFS·A\*·minimax·alpha-beta·IF-THEN) | 🟨 | 📖 | [#2](../../issues/2) · [#22](../../issues/22) · [#23](../../issues/23) |
| 퍼셉트론 · MLP · 역전파 | ⬜ | | `src/` (정글 NumPy MLP ↔ PyTorch 수치 대조) |
| 손실 · 최적화 (SGD·Adam·학습률) | ⬜ | | `experiments/wk04/` |
| CNN 기초 (conv·pooling·출력 크기 계산) | ⬜ | | `experiments/wk05/` |
| LeNet·AlexNet · ReLU·dropout·augmentation | ⬜ | | `experiments/wk06/` |
| 모델 평가 (혼동행렬·batchnorm·정규화) | ⬜ | | `experiments/wk07/` |
| VGG·ResNet · skip connection · 전이학습 | ⬜ | | `experiments/wk09/` |
| 객체 탐지 (IoU·NMS, 사전학습 해석) | ⬜ | | `experiments/wk10/` |
| 의미 분할 · U-Net (Dice·IoU) | ⬜ | | `experiments/wk11/` |
| RNN·LSTM · BPTT · vanishing gradient | ⬜ | | `experiments/wk12/` |
| Autoencoder · VAE (latent space) | ⬜ | | `experiments/wk13/` |
| GAN (DCGAN, mode collapse) | ⬜ | | `experiments/wk14/` |

### 엔지니어링 트랙 *(강의 밖에서 추가)*

| 주제 | 상태 | 깊이 | 증거 |
|---|:--:|:--:|---|
| `torch.profiler`로 병목 분석 (데이터 로딩 vs 연산 vs 전송) | ⬜ | | `experiments/wk06/` |
| 고전 ML (gradient boosting · k-means · PCA, 필요할 때 선택) | ⬜ | | `experiments/classical_ml/` |
| 모델 배포 (ONNX export · 양자화 · FastAPI · 지연 측정) | ⬜ | | `deploy/` |

평가 과제 1–4 (CNN / segmentation / RNN / AE) → `submission/` (학기말 공개)

## 현재 스프린트 — W02 고전 AI

| 작업 | 핵심 질문 | 남길 증거 |
|---|---|---|
| [상태공간 탐색 #2](../../issues/2) | DFS·BFS·A*는 어떤 비용으로 경로를 찾는가? | 경로 길이·확장 노드·frontier 크기 표 |
| [게임 탐색 #22](../../issues/22) | alpha-beta는 같은 최선 수를 더 적게 탐색해 찾는가? | 작은 게임 트리, 방문/가지치기 노드 비교 |
| [규칙 추론 #23](../../issues/23) | 사실 출발과 목표 출발은 무엇을 다르게 확인하는가? | 전향/후향 추론 흔적과 규칙 검사 수 |

예상 파일:

```text
experiments/wk02/
├── search.py
├── game_search.py
└── rule_inference.py
tests/
├── test_search.py
├── test_minimax.py
└── test_rule_inference.py
report_assets/wk02/
reports/REPORT_wk02.md
```

`gradient boosting`, `k-means`, `PCA`는 W02 완료 조건에서 제외한다. 프로젝트에서 표 데이터나 군집·차원 축소가 실제로 필요해질 때 별도 선택 실험으로 연다.

## 다룬 범위 / 다루지 않은 범위

- **다룸**: 비전 중심 딥러닝 + 생성모델 기초. 매 실험은 기준 모델 재현 후 조건 하나만 바꿔 비교.
- **Transformer**: 개념 연결까지 (별도 프로젝트에서 mini-GPT 구현 경험 참조).
- **안 다룸**: 강화학습, 멀티모달, 대규모 분산 학습, LLM 파인튜닝.

## 실행

로컬 GPU (RTX 5060 Ti / WSL2 / CUDA). `make setup && make test` 후 `python experiments/<name>.py`. 데이터·체크포인트는 커밋하지 않음.

## 진행 상황

주차별 할 일: [Issues](../../issues). 각 주차의 상위 이슈는 범위와 완료 기준을 관리하고, 독립적으로 측정할 수 있는 실험은 연결된 하위 이슈로 분리한다.

## 수업 정보

[docs/강의계획서.md](docs/강의계획서.md)
