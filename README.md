# 인공지능 · Artificial Intelligence

서울여대 2026-2학기 · 전공필수 · 3학점 · 수 5–6교시

고전 AI(탐색·추론)부터 CNN·객체탐지·분할·RNN/LSTM·AE/VAE·GAN까지. 코드를 실행한 것보다 **어떤 조건을 바꿨고 결과가 왜 달라졌는지**를 설명하는 데 중점을 둔다.

## 이 레포에 남기는 것

- 매주 `가설 → 설정 → 결과 → 해석` 이 갖춰진 실험 (기준 모델 재현 후 조건 하나만 변경)
- `src/` 재사용 모듈 + `experiments/` 주별 스크립트 + `report_assets/` 생성 그래프
- `docs/` 수식 유도·트러블슈팅 노트
- 학기말 `deploy/` — 최고 모델 ONNX export · 양자화 · FastAPI 서빙 · 지연 측정

## 도구

PyTorch (CUDA, 로컬 RTX 5060 Ti / WSL2) · NumPy · matplotlib · pytest

## 참고 오픈소스

[d2l.ai](https://www.d2l.ai/) · [CS231n](https://cs231n.github.io/) · [nanoGPT](https://github.com/karpathy/nanoGPT)

## 진행

주차별 할 일은 [Issues](../../issues) 참고.
