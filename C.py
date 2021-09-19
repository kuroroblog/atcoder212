# 二分探索を行う関数
def binary_search(a, b):
    min = 0
    max = len(b) - 1
    while min <= max:
        # 中央のインデックスを取得する。
        middle = (min + max) // 2
        if b[middle] == a:
            min = max = middle
            break
        elif b[middle] < a:
            min = middle + 1
        else:
            max = middle - 1

    return [min, max]

# 標準入力を受け付ける。
N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 重複削除を行う。
A = list(set(A))
B = list(set(B))

# 桁の大きい値を設定する。
INF = 1000000000000
# Bの値の最小値、最大値を設定する。
# 二分探索が終了しない問題を解決するため。
# 二分探索とは? : https://e-words.jp/w/%E4%BA%8C%E5%88%86%E6%8E%A2%E7%B4%A2.html
B.append(-INF)
B.append(INF)

B.sort()

ans = INF
for i in range(0, len(A)):
    # 二分探索を用いて、A[i]に近いBの値を探す。
    minIdx, maxIdx = binary_search(A[i], B)
    ans = min(ans, abs(A[i] - B[minIdx]))
    ans = min(ans, abs(A[i] - B[maxIdx]))
print(ans)
