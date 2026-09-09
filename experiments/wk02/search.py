"""W02-1: 같은 미로에서 DFS, BFS, A*를 비교한다.

TODO 순서:
1. neighbors()  2. reconstruct_path()  3. dfs()  4. bfs()  5. manhattan()  6. a_star()
"""
from dataclasses import dataclass

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
    path: tuple[Position, ...]
    path_cost: int
    expanded: int
    frontier_max: int


def neighbors(grid: Grid, current: Position) -> tuple[Position, ...]:
    """벽 밖·벽 칸을 제외한 상하좌우 칸을 반환한다.

    힌트: (행, 열)에 (-1, 0), (1, 0), (0, -1), (0, 1)을 더한 뒤 범위를 확인한다.
    """
    raise NotImplementedError("TODO: neighbors부터 직접 구현하세요.")


def reconstruct_path(came_from: dict[Position, Position | None], goal: Position) -> tuple[Position, ...]:
    """goal에서 시작점까지 부모를 따라간 뒤, 순서를 뒤집는다."""
    raise NotImplementedError("TODO: reconstruct_path를 직접 구현하세요.")


def dfs(grid: Grid, start: Position, goal: Position) -> SearchResult:
    """스택으로 가장 최근 후보를 먼저 꺼낸다."""
    raise NotImplementedError("TODO: dfs를 직접 구현하세요.")


def bfs(grid: Grid, start: Position, goal: Position) -> SearchResult:
    """큐로 시작점에서 가까운 후보를 먼저 꺼낸다."""
    raise NotImplementedError("TODO: bfs를 직접 구현하세요.")


def manhattan(current: Position, goal: Position) -> int:
    """격자에서 가로 차이 + 세로 차이를 반환한다."""
    raise NotImplementedError("TODO: manhattan을 직접 구현하세요.")


def a_star(grid: Grid, start: Position, goal: Position, *, weight: float = 1.0) -> SearchResult:
    """우선순위 큐에서 f = g + weight * h가 가장 작은 후보를 꺼낸다."""
    raise NotImplementedError("TODO: a_star를 직접 구현하세요.")
