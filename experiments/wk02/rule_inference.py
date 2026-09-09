"""W02-3: 같은 규칙 집합으로 전향 추론과 후향 추론을 비교한다."""
from dataclasses import dataclass

Fact = str
Rule = tuple[frozenset[Fact], Fact]

FACTS = frozenset({"비가 온다"})
RULES: tuple[Rule, ...] = (
    (frozenset({"비가 온다"}), "길이 젖는다"),
    (frozenset({"길이 젖는다"}), "이동 속도가 느려진다"),
)
GOAL = "이동 속도가 느려진다"


@dataclass(frozen=True)
class InferenceResult:
    facts: frozenset[Fact]
    trace: tuple[str, ...]
    checked_rules: int


def forward_chain(facts: frozenset[Fact], rules: tuple[Rule, ...]) -> InferenceResult:
    """새 사실이 더 이상 나오지 않을 때까지 적용 가능한 규칙을 반복한다."""
    raise NotImplementedError("TODO: forward_chain을 직접 구현하세요.")


def backward_chain(goal: Fact, facts: frozenset[Fact], rules: tuple[Rule, ...]) -> InferenceResult:
    """goal을 만드는 규칙의 조건을 재귀적으로 확인한다. 순환은 visited로 막는다."""
    raise NotImplementedError("TODO: backward_chain을 직접 구현하세요.")
