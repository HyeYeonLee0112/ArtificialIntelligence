"""탐색: 같은 미로에서 다음 후보를 고르는 방법을 비교한다.

전체 연결:
    BFS / DFS / A* → neighbors        : 갈 수 있는 칸
    BFS / DFS / A* → reconstruct_path : 찾은 경로 복원
    A*            → manhattan        : 남은 비용 추정
    세 탐색        → SearchResult     : 경로·측정값 반환

위에서부터 예제 → 반환 형식 → 보조 함수 → 본 탐색 순서다.
구현: neighbors → manhattan → reconstruct_path → bfs → dfs → a_star.
확인: python -m pytest weeks/wk02/tests (저장소 루트, 전용 환경).
이 파일만 실행하면 출력은 없다. 테스트가 함수를 호출한다."""
from dataclasses import dataclass

# ① 예제와 자료 모양: tuple은 순서가 있고 수정하지 않는 값 묶음이다.
# Position 하나는 (행, 열), Grid는 여러 행을 모은 미로다. 좌표는 0부터 센다.
Position = tuple[int, int]
Grid = tuple[tuple[int, ...], ...]

OPEN = 0
WALL = 1
START: Position = (0, 0)
GOAL: Position = (4, 4)
DEMO_GRID: Grid = (
    (OPEN, OPEN, OPEN, WALL, OPEN),
    (WALL, WALL, OPEN, WALL, OPEN),
    (OPEN, OPEN, OPEN, OPEN, OPEN),
    (OPEN, WALL, WALL, WALL, OPEN),
    (OPEN, OPEN, OPEN, OPEN, OPEN),
)


@dataclass(frozen=True)
class SearchResult:
    """탐색이 반환할 묶음. dataclass가 필드들을 받는 생성자를 만든다.

path: 시작·목표 포함 좌표 tuple. path_cost: 한 칸 비용 1인 이동 횟수.
expanded: 실제 이웃을 조사한 횟수(목표·오래된 큐 항목 제외).
frontier_max: 조사 대기 후보의 최대 항목 수.
실패는 path=(), path_cost=-1. 시작=목표이면 path=(start,), 비용=0."""
    path: tuple[Position, ...]
    path_cost: int
    expanded: int
    frontier_max: int


# ③ 보조 함수: 탐색의 반복문 안에서 호출할 작은 부품들.
def neighbors(grid: Grid, current: Position) -> tuple[Position, ...]:
    """사용처: BFS/DFS/A*가 다음 이동 후보를 구할 때.
입력: grid=0은 길/1은 벽인 미로, current=(행, 열).
반환: 갈 수 있는 좌표 tuple. 예: ((0, 1),). 없으면 ().
힌트: 상하좌우 후보의 범위를 먼저 확인한 뒤 벽을 제외한다. 방문 이력은 탐색이 관리한다."""
    raise NotImplementedError("TODO: neighbors부터 직접 구현하세요.")


def manhattan(current: Position, goal: Position) -> int:
    """사용처: A*의 h(남은 비용 추정).
입력: 현재/목표 좌표. 반환: 정수 거리. (1,2)→(4,4)는 5.
힌트: 행 차이와 열 차이의 절댓값을 더한다. 상하좌우 이동 비용 1, 벽은 무시한다."""
    raise NotImplementedError("TODO: manhattan을 직접 구현하세요.")


def reconstruct_path(came_from: dict[Position, Position | None], goal: Position) -> tuple[Position, ...]:
    """사용처: 세 탐색이 목표에 도착한 뒤.
입력: came_from[현재]=직전 칸인 사전, 도달한 goal. 시작의 부모는 None.
반환: 시작→목표 좌표 tuple. 예: ((0,0), (0,1)).
힌트: 목표부터 부모를 따라 기록하면 역순이다. 부모 연결은 순환하지 않는다고 가정한다."""
    raise NotImplementedError("TODO: reconstruct_path를 직접 구현하세요.")


# ④ 본 탐색: 아래 함수들이 위의 부품을 조립한다.
# 공통 입력은 grid/start/goal, 출력은 SearchResult. 시작·목표는 유효한 길 칸이다.
# frontier는 '다음에 조사할 후보 보관함'. 그 보관함에서 꺼내는 기준이 서로 다르다.
def bfs(grid: Grid, start: Position, goal: Position) -> SearchResult:
    """입력: 미로와 유효한 시작/목표 칸. 반환: SearchResult.
사용: neighbors로 이웃을 찾고, 목표에서 reconstruct_path로 경로를 만든다.
힌트: 먼저 넣은 후보를 먼저 꺼내는 큐. 중복 발견을 기록한다.
이 예제의 최단 비용은 8. 확인: python -m pytest weeks/wk02/tests -k test_bfs"""
    raise NotImplementedError("TODO: bfs를 직접 구현하세요.")


def dfs(grid: Grid, start: Position, goal: Position) -> SearchResult:
    """입력/반환: BFS와 동일. neighbors와 reconstruct_path를 재사용한다.
힌트: 가장 최근 후보부터 꺼내는 스택. 중복 방문을 막는다.
최단 경로는 보장하지 않는다. 확인: python -m pytest weeks/wk02/tests -k test_dfs"""
    raise NotImplementedError("TODO: dfs를 직접 구현하세요.")


def a_star(grid: Grid, start: Position, goal: Position, *, weight: float = 1.0) -> SearchResult:
    """입력: 공통 입력 + weight(기본 1). 반환: SearchResult.
사용: neighbors로 이웃, manhattan으로 h, reconstruct_path로 결과 경로.
힌트: 우선순위 f=g+weight*h. 더 싼 경로를 찾으면 비용과 부모를 갱신한다.
오래된 큐 항목은 건너뛴다. weight 증가의 효과는 측정하며 최단 경로를 보장하지 않는다."""
    raise NotImplementedError("TODO: a_star를 직접 구현하세요.")
