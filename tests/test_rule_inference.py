from experiments.wk02.rule_inference import FACTS, GOAL, RULES, backward_chain, forward_chain


def test_forward_chain_derives_the_goal():
    result = forward_chain(FACTS, RULES)
    assert GOAL in result.facts
    assert result.checked_rules > 0


def test_backward_chain_proves_the_same_goal():
    result = backward_chain(GOAL, FACTS, RULES)
    assert GOAL in result.facts
    assert result.checked_rules > 0


def test_forward_chain_handles_a_cycle_without_looping_forever():
    cyclic_rules = RULES + ((frozenset({GOAL}), "비가 온다"),)
    result = forward_chain(FACTS, cyclic_rules)
    assert GOAL in result.facts
    assert result.checked_rules < 20
