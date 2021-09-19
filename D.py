# ヒープソートを行う関数
# 配列を二分木として扱う。
# 二分木とは? : https://e-words.jp/w/%E4%BA%8C%E5%88%86%E6%9C%A8.html#:~:text=%E4%BA%8C%E5%88%86%E6%9C%A8%E3%81%A8%E3%81%AF%E3%80%81%E3%83%87%E3%83%BC%E3%82%BF,%E6%A7%8B%E9%80%A0%E3%81%AE%E6%9C%A8%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82
# 新しく追加した値 = 子, (pos - 1) >> 1のインデックスに該当する値を親とする。
# 親と子の値比較を行い、配列の順番を並び替える。
# (pos - 1) >> 1を繰り返し、親を探索する。親が存在しなくなるまで、親子の値入れ替えを行う。
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

# 参考 : https://docs.python.org/ja/3/library/heapq.html
from heapq import heappop

# 標準入力を受け付ける。
Q = int(input())
arr = []
offset = 0
for i in range(0, Q):
    s = input().split()
    p = int(s[0])
    if p == 1:
        x = int(s[1])
        # 配列に値を追加する際に、以前までのoffsetは加算されない。
        # offsetとは? : https://wa3.i-3-i.info/word11923.html
        arr.append(x - offset)
        _siftdown(arr, 0, len(arr) - 1)
    elif p == 2:
        x = int(s[1])
        # offsetの演算を行う。
        offset += x
    else:
        # ヒープソートされた配列の最小値を取り出す。
        # ヒープソートとは? : https://ja.wikipedia.org/wiki/%E3%83%92%E3%83%BC%E3%83%97%E3%82%BD%E3%83%BC%E3%83%88
        val = heappop(arr)
        print(offset + val)
