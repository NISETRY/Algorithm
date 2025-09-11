# 전선 N개 - 교차점이 발생 - 몇 개 발생하는 지 count
# 교차점 발생 규칙 
# 1. 새로운 선 - 기존의 시작점보다 더 높음 - 기존의 도착점보다 더 낮음
# 2. 새로운 선 - 기존의 시작점보다 더 낮음 - 기존의 도착점보다 더 높음
# 3. 하나의 새로운 선에서 여러 개의 교차점이 발생할 수 있다 (기존의 전선이 여러 개라면)

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # 1. N개의 새로운 선이 추가 (기존 선들과 비교)
    wires = [] # 기존선들을 저장할 리스트
    anser_count = 0 # 교차점 수

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존 선들과 비교 (교차점 비교)
        for prev_start, prev_end in wires:
            # 1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if start > prev_start and end < prev_end:
                answer_count += 1

            # 2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
            if start < prev_start and end > prev_end:
                answer_count += 1

        # 목록에 추가
        wires.append((start, end))
        
    print(f'#{tc} {answer_count}')
