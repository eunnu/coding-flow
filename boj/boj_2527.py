# '''
# 항상 뒤에 나오는 수가 더 크므로 해당 좌표들이 서로 포함관계인지 같은지를 판별
# 안만나면 d
# 같다면 점만 같은지 선분이 겹치는 지 확인 해서 b, c를 판별
# 둘 다 아니라면 a
# '''
#
for _ in range(4):
    ans = 'a'
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # 점이 겹치는 경우
    if (x1 == x4 and y1 == y4) or (x1 == x4 and y2 == y3) or (x2 == x3 and y1 == y4) or (x2 == x3 and y2 == y3):
        ans = 'c'

    # 안 겹치는 경우
    elif x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
        ans = 'd'

    # 선이 겹치는 경우
    elif x2 == x3 or x1 == x4 or y2 == y3 or y1 == y4:
        ans = 'b'

    print(ans)
