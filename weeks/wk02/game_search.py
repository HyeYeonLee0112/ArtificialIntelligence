"""게임 탐색: 상대의 대응을 고려해 최선 점수를 구한다.

전체 연결:
    DEMO_TREE → minimax    → 점수 / GameStats에 방문 기록
    같은 트리 → alpha_beta → 점수 / GameStats에 방문·생략 기록
두 함수는 자식에 자기 자신을 호출한다. 서로 호출할 필요는 없다.
순서: 예제 → 기록 형식 → minimax → alpha_beta.
확인: python -m pytest weeks/wk02/tests/test_game_search.py"""
from dataclasses import dataclass

# ① str은 자식이 있는 노드의 이름, int는 게임 끝에서 받은 점수다.
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
    """측정용 객체. 각 실행에 새 GameStats()를 넘긴다.
visited: 실제 평가한 내부·말단 노드 수.
pruned: 생략한 직접 자식 가지 수(하위 전체 노드 수가 아님).
함수는 점수를 반환하고, 측정값은 이 객체를 갱신한다."""
    visited: int = 0
    pruned: int = 0


def minimax(tree: GameTree, node: Node, *, is_max: bool, stats: GameStats) -> int:
    """입력: tree=자식 사전, node=이름/점수, is_max=MAX 차례 여부, stats=기록.
반환: 정수 점수. 예제 root는 3. 선택한 수 이름이나 경로가 아니다.
힌트: 숫자면 종료하고, 자식에서는 MAX/MIN을 번갈아 적용한다.
노드마다 방문 수를 센다. 입력은 유한하고 순환하지 않는 트리다."""
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
    """입력: minimax 입력 + alpha/beta 경계. root에서는 -무한대/+무한대.
반환: 정수 점수. root의 최적 값은 minimax와 같다.
힌트: MAX가 확보한 하한 alpha와 MIN이 확보한 상한 beta를 갱신한다.
alpha>=beta면 남은 자식 가지를 생략하고 stats에 기록한다."""
    raise NotImplementedError("TODO: alpha_beta를 직접 구현하세요.")
