import pytest

from experiments.wk02.search import (
    DEMO_GRID,
    GOAL,
    START,
    WALL,
    a_star,
    bfs,
    manhattan,
    neighbors,
)


def test_neighbors_stay_inside_grid_and_avoid_walls():
    assert neighbors(DEMO_GRID, START) == ((0, 1),)
    assert all(DEMO_GRID[row][col] != WALL for row, col in neighbors(DEMO_GRID, (2, 2)))


def test_manhattan_distance():
    assert manhattan(START, GOAL) == 8


def test_bfs_finds_the_known_shortest_path():
    result = bfs(DEMO_GRID, START, GOAL)
    assert result.path[0] == START
    assert result.path[-1] == GOAL
    assert result.path_cost == 8


def test_a_star_matches_bfs_with_normal_heuristic():
    bfs_result = bfs(DEMO_GRID, START, GOAL)
    a_star_result = a_star(DEMO_GRID, START, GOAL)
    assert a_star_result.path_cost == bfs_result.path_cost
    assert a_star_result.expanded <= bfs_result.expanded


@pytest.mark.parametrize("weight", [1.5, 3.0])
def test_weighted_a_star_still_returns_a_valid_path(weight):
    result = a_star(DEMO_GRID, START, GOAL, weight=weight)
    assert result.path[0] == START
    assert result.path[-1] == GOAL
