"""규칙 추론: 사실에서 전개하거나 목표의 근거를 거꾸로 찾는다.

전체 연결:
    FACTS + RULES        → forward_chain  → InferenceResult
    GOAL + FACTS + RULES → backward_chain → InferenceResult
두 함수는 서로 호출하지 않고 같은 지식으로 목표의 증명 여부를 비교한다.
순서: 사실·규칙 → 반환 형식 → 전향 추론 → 후향 추론.
확인: python -m pytest weeks/wk02/tests/test_rule_inference.py"""
from dataclasses import dataclass

# ① 사실은 문자열 하나. frozenset은 중복이 없고 원본을 수정할 수 없는 집합이다.
# 규칙 하나 = (모두 만족해야 하는 조건 집합, 조건이 맞으면 얻는 결론).
# 예: ({비가 온다}, 길이 젖는다). 여러 조건이면 AND, 같은 결론의 여러 규칙은 OR다.
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
    """반환 묶음. facts는 원래 사실과 실제 증명한 결론(frozenset).
trace는 새 결론을 얻은 순서의 설명 tuple. 예: ('비 → 젖은 길',).
checked_rules는 조건을 검사한 횟수(재검사 포함).
목표 성공 여부는 GOAL in result.facts로 확인한다."""
    facts: frozenset[Fact]
    trace: tuple[str, ...]
    checked_rules: int


def forward_chain(facts: frozenset[Fact], rules: tuple[Rule, ...]) -> InferenceResult:
    """입력: facts=처음 아는 사실, rules=규칙 tuple. 원본은 수정하지 않는다.
반환: InferenceResult. 예제 결과에는 '이동 속도가 느려진다'가 포함된다.
힌트: 조건이 모두 있는 규칙의 새 결론만 추가한다. 새 사실이 없으면 멈춘다."""
    raise NotImplementedError("TODO: forward_chain을 직접 구현하세요.")


def backward_chain(goal: Fact, facts: frozenset[Fact], rules: tuple[Rule, ...]) -> InferenceResult:
    """입력: goal=목표, facts=처음 아는 사실, rules=규칙들.
반환: InferenceResult. 증명 성공 시 goal 포함, 실패한 가정은 facts에 넣지 않는다.
힌트: 목표를 만드는 규칙의 조건을 재귀로 확인한다. 필요하면 내부 prove 함수를 둔다.
현재 증명 중인 목표로 돌아오면 순환이다. 한 규칙이 실패해도 다른 규칙은 확인한다."""
    raise NotImplementedError("TODO: backward_chain을 직접 구현하세요.")
