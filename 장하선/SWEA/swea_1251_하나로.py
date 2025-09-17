import sys
sys.stdin=open('input.txt')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    x_island=list(map(int,input().split()))
    y_island=list(map(int,input().split()))
    e=float(input)