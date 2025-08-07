# 총 10개의 테스트 케이스 주어짐

T = 10

for tc in range (1, T+1):

    N = int(input())  # 건물의 개수 N

    buildings = list(map(int, input().split()))
    okay = 0
    for i in range(2, N-2):
        if (buildings[i-2] < buildings[i] and 
            buildings[i-1] < buildings[i] and 
            buildings[i] > buildings[i+1] and 
            buildings[i] > buildings[i+2]):
            okay += buildings[i] - max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])    

    print(f'#{tc} {okay}')



# for문은 간격을 불규칙적으로 옮길 수 없는데
# while은 간격을 불규칙적으로 옮길 수 있음. 그러면, 조망권을 획득했을 때 3칸을 옮기는 것으로 while() 다시 짜보기