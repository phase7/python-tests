        
if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
    lst.sort(key = lambda x: x[1])
    mx = lst[0][1]
    prnt = []
    cnt = 0
    key = 0.0
    for i in range(len(lst)-1):
        if mx == lst[i][1]:
            cnt += 1
        else :
            key = lst[i][1]
            break
    for [a,b] in lst:
        if key == b:
            prnt.append(a)
    prnt.sort()
    for i in prnt:
        print(i)