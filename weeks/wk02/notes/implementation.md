# 작성하고 확인하는 순서

저장소 루트를 VS Code로 열고 weeks/wk02/search.py부터 시작한다.
함수는 네가 작성하고, tests/가 입력을 넣어 반환값을 기대 결과와 비교한다.
파일만 실행하면 함수가 정의될 뿐 출력은 없다.

## 한 함수씩

neighbors → manhattan → reconstruct_path → bfs → dfs → a_star 순서로 진행한다.
함수 위에는 역할·입력·반환값과 첫 힌트만 있다. TODO의 NotImplementedError를 구현으로 바꾼다.

저장소 루트 PowerShell에서 첫 함수만 검사한다.

```powershell
.\.venv\Scripts\python.exe -m pytest weeks/wk02/tests/test_search.py -k test_neighbors
```

거리만 검사하려면 -k test_manhattan, BFS만 검사하려면 -k test_bfs를 사용한다.

## 주제 또는 주차 전체

```powershell
.\.venv\Scripts\python.exe -m pytest weeks/wk02/tests/test_search.py
.\.venv\Scripts\python.exe -m pytest weeks/wk02/tests/test_game_search.py
.\.venv\Scripts\python.exe -m pytest weeks/wk02/tests/test_rule_inference.py
.\.venv\Scripts\python.exe -m pytest weeks/wk02/tests
```

출력 예시(설명용 가상 결과):

```text
[맨해튼 거리] 내 구현 결과: 7
[맨해튼 거리] 기대 결과: 8
1개 실패했습니다. 0/1 통과
```

각 검사에 두 줄을 출력하고 맨 아래 전체 집계를 표시한다. 원인 해설이나 정답 힌트는 자동 출력하지 않는다.
미구현은 실패로 센다. 문법·import 오류는 검사 자체를 시작할 수 없는 수집 오류이므로 문제풀이 실패와 구분한다.
자세한 오류가 필요할 때만 --tb=short -ra를 붙인다.

경로처럼 정답이 여러 개면 결과 경로를 보여주고 '벽을 지나지 않는 인접 경로, 비용 8' 같은 기대 조건과 비교한다.
A*의 확장 수가 항상 BFS 이하라고 강제하지 않는다. 순환/도달 불가 등 추가 문제는 구현 후 본인이 추가할 수 있다.

## 검증과 기록

루트의 tests/는 공통 도구 검사, 이 폴더의 tests/는 직접 풀 문제다.
GitHub 자동 검사는 공통 도구와 문법만 검사한다. 학습 테스트를 통과했다고 표시하지 않는다.
문제풀이 결과는 REPORT.md에 적고 필요한 그림·표를 assets/에 둔다.
