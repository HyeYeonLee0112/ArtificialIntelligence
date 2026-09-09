from weeks.wk02.search import DEMO_GRID, START, GOAL, neighbors, manhattan, reconstruct_path, bfs, dfs, a_star


def valid_path(result):
    path = result.path
    return (
        bool(path) and path[0] == START and path[-1] == GOAL
        and all(0 <= r < len(DEMO_GRID) and 0 <= c < len(DEMO_GRID[0])
                and DEMO_GRID[r][c] == 0 for r, c in path)
        and all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(path, path[1:]))
        and result.path_cost == len(path)-1
        and result.expanded >= 0 and result.frontier_max >= 1
    )


def test_neighbors(check):
    check("이웃 칸", lambda: neighbors(DEMO_GRID, START), ((0, 1),))


def test_neighbors_center(check):
    check("중앙 이웃", lambda: set(neighbors(DEMO_GRID, (2, 2))), {(1, 2), (2, 1), (2, 3)})


def test_manhattan(check):
    check("맨해튼 거리", lambda: manhattan(START, GOAL), 8)


def test_reconstruct(check):
    check("경로 복원", lambda: reconstruct_path({(0, 0): None, (0, 1): (0, 0)}, (0, 1)),
          ((0, 0), (0, 1)))


def test_bfs(check):
    check("BFS", lambda: bfs(DEMO_GRID, START, GOAL), "유효한 경로, 비용 8",
          lambda result: valid_path(result) and result.path_cost == 8)


def test_dfs(check):
    check("DFS", lambda: dfs(DEMO_GRID, START, GOAL), "유효한 경로, 비용은 이동 횟수와 일치", valid_path)


def test_a_star(check):
    check("A*", lambda: a_star(DEMO_GRID, START, GOAL), "유효한 경로, 비용 8",
          lambda result: valid_path(result) and result.path_cost == 8)


def test_weighted_a_star(check):
    check("가중 A*", lambda: a_star(DEMO_GRID, START, GOAL, weight=3.0),
          "유효한 경로, 비용은 이동 횟수와 일치", valid_path)
