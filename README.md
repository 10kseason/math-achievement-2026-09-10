# 순환 차분의 소멸 시간 — 추측 (14) 검토 보충자료

이 저장소는 `순환 차분의 소멸 시간 — 전체 증명.md`의 추측 (14)에 대한 보충 원고와 재현 가능한 정확 계산을 담는다.

## 현재 결론

- 기존 원문에서 증명된 범위는 그대로 유지한다: `a≤2` 또는 `b≤3`.
- 모든 소수 `p`와 `a,b≥1`에 대해 `f(t)=log_p|D^tV|`의 `t=0,1,2,3` 값은 엄밀히 계산된다.
- `a≥3,b≥4`의 나머지 구간에 대해서는 이 자료가 일반 증명을 제공하지 않는다.
- 포함된 계산은 작은 사례에서 추측식과 일치하지만, 계산 일치는 증명이 아니다.

수식과 주장에 대한 자세한 범위·장애물·증명 경로는 [`docs/supplement_ko.md`](docs/supplement_ko.md)를 참조한다.

## 재현

```bash
python3 check_distribution.py --p 2 --a 3 --b 4
python3 check_distribution.py --p 3 --a 3 --b 4
python3 check_distribution.py --p 2 --a 4 --b 4
python3 check_distribution.py --p 3 --a 4 --b 4 --boundary-only
python3 check_distribution.py --p 3 --a 3 --b 5 --boundary-only
```

`results/`에는 위 실행의 JSON 결과가 들어 있다. 계산은 정수 행렬을 `Z/p^b Z` 위에서 valuation-aware 소거해 상의 크기를 직접 계산한다.

## 문헌 상태

관련 키워드(순환군 환의 augmentation ideal, modular group algebra, nilpotency index)는 원고의 문헌 메모에 정리했다. 여기서 인용한 자료가 추측 (14)의 전체 분포 공식을 증명한다고 주장하지 않는다.

## AI 사용 표기

이 보충자료의 초안 정리, 증명 서술 보조, 재현 스크립트와 결과 정리는 AI(Codex)의 도움을 받아 작성했다. 수학적 주장과 계산 결과의 최종 검토 및 공개 책임은 저자에게 있다. AI 사용 사실은 내용의 엄밀성이나 독창성을 보증하지 않는다.


