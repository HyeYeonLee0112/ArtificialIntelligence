"""W02 문제풀이 출력. 일반 공통 도구 테스트와 학습 비교 결과를 구분한다."""
import pytest
from src.lab_checks import compare, lines, summary


def pytest_configure(config):
    config.lab_results = []


@pytest.fixture
def check(request):
    def run_case(name, run, expected, accepts=None):
        result = compare(name, run, expected, accepts)
        request.config.lab_results.append(result)
        if not result.passed:
            pytest.fail(name, pytrace=False)
    return run_case


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if config.lab_results:
        terminalreporter.write_sep("=", "문제풀이 결과")
        for result in config.lab_results:
            for line in lines(result):
                terminalreporter.write_line(line)
        terminalreporter.write_line(summary(config.lab_results))
