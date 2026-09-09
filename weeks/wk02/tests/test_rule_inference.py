from weeks.wk02.rule_inference import FACTS, GOAL, RULES, forward_chain, backward_chain


def test_forward(check):
    check("전향 추론", lambda: forward_chain(FACTS, RULES), "목표 포함, 검사 횟수 양수, 적용 기록 존재",
          lambda r: GOAL in r.facts and r.checked_rules > 0 and bool(r.trace))


def test_backward(check):
    check("후향 추론", lambda: backward_chain(GOAL, FACTS, RULES), "목표 포함, 검사 횟수 양수, 적용 기록 존재",
          lambda r: GOAL in r.facts and r.checked_rules > 0 and bool(r.trace))


def test_unprovable(check):
    check("증명할 수 없는 목표", lambda: backward_chain("눈이 온다", FACTS, RULES),
          "증명하지 못한 목표를 facts에 추가하지 않음", lambda r: "눈이 온다" not in r.facts)
