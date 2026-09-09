"""W02-2: 작은 게임 트리에서 minimax와 alpha-beta를 비교한다."""
from dataclasses import dataclass

Node = str | int
GameTree = dict[str, tuple[Node, ...]]

# root은 MAX, A/B는 MIN, 숫자는 말단 노드의 점수다.
DEMO_TREE: GameTree = {
    "root": ("A", "B"),
    "A": (3, 5),
    "B": (2, 9),
}


@dataclass
class GameStats:
    visited: int = 0
    pruned: int = 0


def minimax(tree: GameTree, node: Node, *, is_max: bool, stats: GameStats) -> int:
    """말단은 점수를 반환하고, MAX/MIN은 자식 결과의 max/min을 반환한다."""
    raise NotImplementedError("TODO: minimax를 직접 구현하세요.")


def alpha_beta(
    tree: GameTree,
    node: Node,
    *,
    is_max: bool,
    alpha: float,
    beta: float,
    stats: GameStats,
) -> int:
    """minimax에 alpha/beta 경계와 가지치기 횟수를 추가한다."""
    raise NotImplementedError("TODO: alpha_beta를 직접 구현하세요.")
