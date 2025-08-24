player = [list(map(int, input().split())) for _ in range(5)]
judge = [list(map(int, input().split())) for _ in range(5)]


def check_bingo(arr, r, c):
    lines = []
    if all(x==0 for x in arr[r]):
        lines.append(('Row', r))
    elif all(arr[i][c] == 0 for i in range(5)):
        lines.append(('Col', c))
    elif r == c and all( arr[i][i] == 0 for i in range(5)):
        lines.append(('Main', 1))
    elif r == 4 - c and all(arr[i][4-i] == 0 for i in range(5)):
        lines.append(('Anti', 1))
    return lines

pos = {}
for i in range(5):
    for j in range(5):
        pos[player[i][j]] = (i, j)
completed = set()

count_bingo = 0
call_num = 0

for jr in range(5):
    for jc in range(5):
        call_num += 1
        num = judge[jr][jc]
        pr, pc = pos[num]
        player[pr][pc] = 0

        for line in check_bingo(player, pr, pc):
            if line not in completed:
                completed.add(line)
                count_bingo += 1

                if count_bingo >= 3:
                    print(call_num)
                    exit()