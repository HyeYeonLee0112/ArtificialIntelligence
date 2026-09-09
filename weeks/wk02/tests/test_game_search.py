from weeks.wk02.game_search import DEMO_TREE, GameStats, minimax, alpha_beta


def plain():
    stats = GameStats()
    score = minimax(DEMO_TREE, "root", is_max=True, stats=stats)
    return {"점수": score, "방문": stats.visited, "생략 가지": stats.pruned}


def pruned():
    stats = GameStats()
    score = alpha_beta(DEMO_TREE, "root", is_max=True, alpha=float("-inf"),
                       beta=float("inf"), stats=stats)
    return {"점수": score, "방문": stats.visited, "생략 가지": stats.pruned}


def test_minimax(check):
    check("minimax", plain, {"점수": 3, "방문": 7, "생략 가지": 0})


def test_alpha_beta(check):
    check("alpha-beta (주어진 자식 순서)", pruned, {"점수": 3, "방문": 6, "생략 가지": 1})
