# 리스트 활용해서 해쉬 테이블 구현
# 해쉬 함수 : key % 8
# 해쉬 키 생성 : hash(data)
# 1. 기본
# 2. Chaining : 해쉬 테이블 저장공간 외의 공간을 활용하는 기법
#             : 충돌이 일어나면, 링크드 리스트 자료 구조를 사용해서, 추가로 뒤에 연결시켜서 저장하는 방법
# 3. Linear Probing : 해쉬 테이블 저장공간 안에서 충돌 문제를 해결 하는 방법
#                   : 충돌이 일어나면, 해당 주소 다음 주소 부터 맨 처음 나오는 빈 공간에 저장하는 기법
#                   : 저장공간 활용도를 높이기 위한 기법


hash_table = [0]*8


def hash_func(key):
    return key % 8


def set_data(data, value):
    # 1
    # key = hash_func(data)
    # hash_table[key] = value

    # 2
    hash_idx = hash(data)
    hash_key = hash_func(hash_idx)
    if hash_table[hash_key] != 0:
        for i in range(len(hash_table[hash_key])):
            if hash_table[hash_key][i][0] == hash_idx:
                hash_table[hash_key][i][1] = value
                return True
        hash_table[hash_key].append([hash_idx, value])
        return True
    else:
        hash_table[hash_key] = [[hash_idx, value]]
        return True

    # 3
    # hash_idx = hash(data)
    # hash_key = hash_func(hash_idx)
    # if hash_table[hash_key]:
    #     for i in range(hash_key, len(hash_table)):
    #         if hash_table[i] == 0:
    #             hash_table[i] = [hash_idx, value]
    #             return True
    #         elif hash_table[i][0] == hash_key:
    #             hash_table[i][1] = value
    #             return True
    # else:
    #     hash_table[hash_key] = [hash_idx, value]
    #     return True


def get_data(data):
    # 1
    # key = hash_func(data)
    # return hash_table[key]

    # 2
    hash_idx = hash(data)
    hash_key = hash_func(hash_idx)
    if hash_table[hash_key]:
        for value in hash_table[hash_key]:
            if value[0] == hash_idx:
                print(value[1])
                return value[1]
        print("None")
        return None
    else:
        print("None")
        return None
    #
    # 3
    # hash_idx = hash(data)
    # hash_key = hash_func(hash_idx)
    # if hash_table[hash_key]:
    #     for idx in range(hash_key, len(hash_table)):
    #         if hash_table[idx] == 0:
    #             return None
    #         elif hash_table[idx][0] == hash_idx:
    #             return hash_table[idx][1]
    #     return None


# 2
# [0, [[9, '함수']], 0, [[3, '해쉬']], 0, 0, 0, 0]
# [0, [[9, '함수'], [1, '우와']], 0, [[3, '해쉬']], 0, 0, 0, 0]
# 3
# [0, [9, '함수'], 0, [3, '해쉬'], 0, 0, 0, 0]
# [0, [9, '함수'], [1, '우와'], [3, '해쉬'], 0, 0, 0, 0]
set_data(3, "해쉬")
print(hash_table)
set_data(9, "함수")
print(get_data(3))
print(hash_table)
set_data(1, "우와")
print(hash_table)