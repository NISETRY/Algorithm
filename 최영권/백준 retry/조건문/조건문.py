# 1330번
# a, b = map(int, input().split())

# if a < b:
#    print('<')
# elif a > b:
#     print('>')
# elif a == b:
#     print('==')

# 9498번
# score = int(input())
#
# if score <= 100 and score >= 90:
#     print('A')
# elif score <= 89 and score >= 80:
#     print('B')
# elif score <= 79 and score >= 70:
#     print('C')
# elif score <= 69 and score >= 60:
#     print('D')
# else:
#     print('F')

# 2753번
# year = int(input())
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('1')
# else:
#     print('0')

# 14681번
# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print(1)
# elif x > 0 and y < 0:
#     print(4)
# elif x < 0 and y > 0:
#     print(2)
# elif x < 0 and y < 0:
#     print(3)


# 2884번
# hour, minute = map(int, input().split())
#
# if hour > 0 and minute < 45:
#     hour -= 1
#     minute = minute + 15
#     print(hour, minute)
# elif hour == 0 and minute < 45:
#     hour = 23
#     minute = minute + 15
#     print(hour, minute)
# else:
#     print(hour, minute-45)

# 2525번
# cur_hour, cur_min = map(int, input().split())
# waiting_time = int(input())
#
# if (waiting_time + cur_min >= 60):
#     cur_hour = cur_hour + (waiting_time + cur_min) // 60
#     cur_min = (cur_min + waiting_time) % 60
#     if cur_hour >= 24:
#         cur_hour -= 24
#     print(cur_hour, cur_min)
# else:
#     print(cur_hour, cur_min + waiting_time)

# 2480번

# dice1, dice2, dice3 = map(int, input().split())
#
# count_same = 0
# if dice1 == dice2 == dice3:
#     print(10000 + 1000*dice1)
# elif dice1 == dice2 != dice3:
#     print(1000+dice1*100)
# elif dice2 == dice3 != dice1:
#     print(1000+dice2*100)
# elif dice1 == dice3 != dice2:
#     print(1000+dice3*100)
# else:
#     if dice1 > dice2 and dice1 > dice3:
#         print(100 * dice1)
#     elif dice3 > dice2 and dice3 > dice1:
#         print(100 * dice3)
#     elif dice2 > dice3 and dice2 > dice1:
#         print(100 * dice2)
