from experiments.wk02.game_search import DEMO_TREE, GameStats, alpha_beta, minimax


def test_minimax_returns_the_root_value():
    stats = GameStats()
    assert minimax(DEMO_TREE, "root", is_max=True, stats=stats) == 3
    assert stats.visited > 0


def test_alpha_beta_keeps_the_same_value_with_fewer_or_equal_visits():
    plain_stats = GameStats()
    pruned_stats = GameStats()
    plain_score = minimax(DEMO_TREE, "root", is_max=True, stats=plain_stats)
    pruned_score = alpha_beta(
        DEMO_TREE,
        "root",
        is_max=True,
        alpha=float("-inf"),
        beta=float("inf"),
        stats=pruned_stats,
    )
    assert pruned_score == plain_score
    assert pruned_stats.visited <= plain_stats.visited
    assert pruned_stats.pruned >= 1
