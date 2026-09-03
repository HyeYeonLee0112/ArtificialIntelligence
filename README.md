# 인공지능 · Artificial Intelligence

> 퍼셉트론부터 CNN·객체탐지·분할·RNN·생성모델까지 PyTorch 실험 기록과 모델 배포.

## 커리큘럼 & 구현 현황

**상태** ⬜ 예정 · 🟨 진행 · ✅ 완료
**깊이** `📖 개념` · `✏️ 손계산` · `🔨 구현+테스트` · `📊 실험+측정` · `⚡ 조건 비교·해석`

### 강의 범위

| 주제 | 상태 | 깊이 | 증거 |
|---|:--:|:--:|---|
| 고전 AI: 상태공간 탐색 (DFS·BFS·A\*) | ⬜ | | `experiments/wk02/` |
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
| 고전 ML (gradient boosting · k-means · PCA) | ⬜ | | `experiments/wk02/` |
| 모델 배포 (ONNX export · 양자화 · FastAPI · 지연 측정) | ⬜ | | `deploy/` |

평가 과제 1–4 (CNN / segmentation / RNN / AE) → `submission/` (학기말 공개)

## 다룬 범위 / 다루지 않은 범위

- **다룸**: 비전 중심 딥러닝 + 생성모델 기초. 매 실험은 기준 모델 재현 후 조건 하나만 바꿔 비교.
- **Transformer**: 개념 연결까지 (별도 프로젝트에서 mini-GPT 구현 경험 참조).
- **안 다룸**: 강화학습, 멀티모달, 대규모 분산 학습, LLM 파인튜닝.

## 실행

로컬 GPU (RTX 5060 Ti / WSL2 / CUDA). `make setup && make test` 후 `python experiments/<name>.py`. 데이터·체크포인트는 커밋하지 않음.

## 진행 상황

주차별 할 일: [Issues](../../issues)

## 수업 정보

[docs/강의계획서.md](docs/강의계획서.md)
