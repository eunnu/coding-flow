from sys import stdin

N = int(stdin.readline())
max_score = [0, 0, 0]
min_score = [0, 0, 0]

for _ in range(N):
    game = list(map(int, stdin.readline().split(" ")))
    max_score = [game[0] + max(max_score[:2]), game[1] + max(max_score), game[2] + max(max_score[1:])]
    min_score = [game[0] + min(min_score[:2]), game[1] + min(min_score), game[2] + min(min_score[1:])]
print(max(max_score), min(min_score))


