from src.lab_checks import compare, lines, summary


def test_mixed_results_and_two_line_output():
    success = compare("합", lambda: 3, 3)
    failure = compare("거리", lambda: 7, 8)
    assert success.passed and not failure.passed
    assert len(lines(failure)) == 2
    assert "7" in lines(failure)[0] and "8" in lines(failure)[1]
    assert summary([success, failure]) == "1개 실패했습니다. 1/2 통과"


def test_exceptions_count_as_failures_without_explanation():
    def todo():
        raise NotImplementedError("정답 힌트는 출력하지 않음")
    def broken():
        raise ValueError("상세 원인도 기본 출력하지 않음")
    for fn in (todo, broken):
        result = compare("예외", fn, 8)
        assert not result.passed
        assert "기대 결과" in lines(result)[1]
        assert "정답 힌트" not in lines(result)[0]


def test_predicate_accepts_multiple_valid_answers():
    result = compare("여러 정답", lambda: (2, 1), "1과 2를 각각 포함", lambda a: set(a) == {1, 2})
    assert result.passed


def test_wrong_return_shape_is_still_reported():
    result = compare("형식", lambda: None, "경로 결과", lambda a: a.path_cost == 8)
    assert result.actual is None and not result.passed
    assert len(lines(result)) == 2
