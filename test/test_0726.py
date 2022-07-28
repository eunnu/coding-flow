a = [[3,1,2],
	 [4,7,9],
     [6,8,5]]

print('original mat : ',a)

# 직접구현 전치코드 -> 좋으나 3*4 모양이면 귀찮음
# for r in range(3):
# 	for c in range(3):
# 		if r > c:
# 			a[r][c], a[c][r] = a[c][r], a[r][c]

#tr_mat = list(zip(*a))
tr_mat = list(map(list, zip(*a)))      

print('after swap mat : ',tr_mat)
