# W02 고전 AI

이 폴더 안에서 탐색·게임 탐색·규칙 추론을 구현하고 확인한다. 실험 규모는 본인이 정하며, 기존 예제는 시작 입력으로 유지했다.

| 파일 | 직접 구현할 내용 | 확인 파일 |
|---|---|---|
| search.py | 보조 함수 → BFS → DFS → A* | tests/test_search.py |
| game_search.py | minimax → alpha-beta | tests/test_game_search.py |
| rule_inference.py | 전향 추론 → 후향 추론 | tests/test_rule_inference.py |

- [개념 예습](notes/preview.md)
- [구현·실행 안내](notes/implementation.md)
- [직접 작성할 결과 보고서](REPORT.md)
- [기록할 그림·측정값](assets/README.md)

관련 이슈: [#2](https://github.com/HyeYeonLee0112/ArtificialIntelligence/issues/2), [#22](https://github.com/HyeYeonLee0112/ArtificialIntelligence/issues/22), [#23](https://github.com/HyeYeonLee0112/ArtificialIntelligence/issues/23).
함수 위의 입력·반환 설명을 읽고 TODO를 채운다. 첫 힌트는 짧게 두었으며 추가 힌트는 막혔을 때 요청한다.
