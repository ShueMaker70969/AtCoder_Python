str = input()
l = list(str)
if len(l) == 1:
    print(l[0])
else:
    palin = l.copy()
    index = 0
    for i in range(1, len(l)+1):
        if l[-i] != l[-i-1]:
            index = -i
            break
    for i in range(index-1, -len(l)-1, -1):
        palin.append(l[i])
    for i in palin:
        print(i, end='')
#未完成コード！！！これはあくまで最後尾の文字が同じか、だけを確認している。
#だが実際は、末尾の最長の回文を確認する必要があり、こちらの方がはるかに複雑となる。

