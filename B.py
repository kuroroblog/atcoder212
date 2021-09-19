# 標準入力を受け付ける。
s = list(input())

# 全て同じ番号で暗証番号が構成される場合、Weakを出力する。
# 重複削除参考 : https://note.nkmk.me/python-list-unique-duplicate/
if len(list(set(s))) == 1:
    print('Weak')
    exit()

# 直前の番号を記録する。
frontVal = int(s[0])
# 最終的に暗証番号が強いかどうか判定するフラグ。
isStrong = False
for i in range(1, len(s)):
    # frontValが9の場合に、次の番号を0にするため % 10を行う。
    frontVal = (frontVal + 1) % 10
    # 暗証番号が強いと判断したら、breakする。
    if not frontVal == int(s[i]):
        isStrong = True
        break

if isStrong:
    print('Strong')
else:
    print('Weak')
