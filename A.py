# 標準入力を受け付ける。
A, B = map(int, input().split())

# A = 0かつ0 < Bなら「純銀」
if A == 0 and 0 < B:
    print('Silver')
# 0 < AかつB = 0なら「純金」
elif 0 < A and B == 0:
    print('Gold')
# 0 < Aかつ0 < Bなら「合金」
else:
    print('Alloy')
