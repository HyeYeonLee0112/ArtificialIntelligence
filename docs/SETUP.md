# 실행 환경

2026-09-09 확인: 이 컴퓨터는 RTX 5070 Ti, NVIDIA 드라이버 596.49, Windows Python 3.11이다. WSL에는 docker-desktop만 있어 이번 설정은 Windows 전용 가상환경을 사용한다.

## Windows PowerShell

저장소 루트에서 실행한다. 활성화 없이 전용 Python을 직접 호출할 수 있다.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
.\.venv\Scripts\python.exe scripts/check_environment.py --require-cuda --output report_assets/wk01/environment.json
.\.venv\Scripts\python.exe -m pytest -q
```

이미 .venv가 있으면 생성 단계는 건너뛴다. 노트북이 필요한 시점에 `python -m pip install -r requirements-notebooks.txt` 후 같은 환경의 `python -m jupyterlab`으로 연다.

## WSL/Linux 또는 CPU 대체 환경

```bash
python3 -m venv .venv
source .venv/bin/activate
make setup
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
make test
make check
```

GPU를 사용할 Linux 환경에서는 CPU 설치 줄 대신 장치에 맞는 CUDA 설치 명령을 사용한다. [PyTorch 공식 설치 선택기](https://pytorch.org/get-started/locally/)에서 OS와 CUDA 지원을 확인한다. CUDA 설치 후에는 `--require-cuda` 검사까지 통과해야 GPU 준비 완료다. 단순 설치 성공만으로 완료하지 않는다.

requirements.txt는 기본 실험 도구이며 torch/torchvision은 장치에 맞춰 별도 설치한다. 검사 결과에 실제 버전과 장치를 기록한다. 동일 seed 검사는 해당 환경의 작은 예제 검사이며 다른 장치·모든 학습의 완전 동일성을 보장하지 않는다.

## 파일 역할

- experiments/wkNN/: 직접 작성하는 주차별 코드
- src/: 실험에서 검증한 뒤 공통으로 사용하는 코드
- tests/: 핵심 계산과 공통 도구 검사
- notebooks/: 직접 만든 노트북과 로컬 수업 원본
- reports/: 주차별 질문·결과·오류 분석·회상
- report_assets/wkNN/: 환경·측정값·그림
- docs/HyeYeon/: 손계산과 트러블슈팅
- submission/: 공개하지 않는 평가 과제 작업
- deploy/: 수업 이후 선택 배포

자동 검사는 CPU에서 공통 코드와 문법을 확인한다. 신경망 학습 성능과 GPU 동작은 로컬에서 별도로 확인한다. 알고리즘 구현은 학습자가 작성할 예정이므로 현재 검사 통과가 주차 학습 완료를 뜻하지 않는다.
