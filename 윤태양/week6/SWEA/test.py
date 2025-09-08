t = int(input()) # 테스트 케이스 인풋

for tc in range(1, t+1):
    slope = list(map(int, input().split())) # 경사도 리스트 받기
    last = -1 # 마지막 방문했던 경사 / 디폴트는 -1로 설정
    
    temp = [] # 임시 리스트
    slope_list = [] # 각각의 경사도를 담은 리스트

    for i in slope: # 경사도 리스트를 돌면서
        if i >= last: # 현재가 이전보다 크다면
            temp.append(i) # 임시리스트에 추가
            last = i # 이전을 현재로 갱신

        else:
            slope_list.append(temp) # 현재가 이전보다 작다면 한 개의 경사도가 끝났음으로 경사도 리스트에 추가
            temp = []  # 임시 리스트 초기화
            temp.append(i) # 임시 리스트에 현재 추가
            last = i # 이전 갱신

    slope_list.append(temp) # for문이 끝날 때 경사도 리스트에 추가하는 로직이 없으므로 추가
    slope_list.sort(key=len, reverse= True) # 길이 기준으로 정렬 + 거꾸로 / 디폴트는 짧은 순
    
    max_min = [] # max-min 값을 저장할 리스트

    for i in slope_list:
        max_slope, min_slope = max(i), min(i)
        max_min.append(((max_slope-min_slope)/len(i),len(i)))

    max_min.sort(reverse=True)
    print(max_min[0][1])
        