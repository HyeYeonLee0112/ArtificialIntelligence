"""학습자의 실행 결과를 기대값과 비교하고, 원인 해설 없이 표시한다."""
from dataclasses import dataclass
from pprint import pformat


@dataclass(frozen=True)
class Comparison:
    name: str
    actual: object
    expected: object
    passed: bool


def compare(name, run, expected, accepts=None):
    try:
        actual = run()
    except NotImplementedError:
        return Comparison(name, "미구현 (NotImplementedError)", expected, False)
    except Exception as error:
        return Comparison(name, f"실행 오류 ({type(error).__name__})", expected, False)
    try:
        passed = actual == expected if accepts is None else bool(accepts(actual))
    except Exception:
        passed = False
    return Comparison(name, actual, expected, passed)


def lines(result):
    actual = pformat(result.actual, width=10000, compact=True).replace("\n", " ")
    expected = pformat(result.expected, width=10000, compact=True).replace("\n", " ")
    return [f"[{result.name}] 내 구현 결과: {actual}",
            f"[{result.name}] 기대 결과: {expected}"]


def summary(results):
    total = len(results)
    passed = sum(result.passed for result in results)
    return f"{total - passed}개 실패했습니다. {passed}/{total} 통과"
