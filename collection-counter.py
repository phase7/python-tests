from collections import Counter
if __name__ == "__main__":
    n = input()
    lst  = [int(x) for x in input().split()]
    cntr = Counter(lst)
    n = input()
    ans = 0
    for _ in range(int(n)):
        buy = [int(i) for i in input().split()]
        if cntr[buy[0]] > 0:
            cntr[buy[0]] -= 1
            ans += buy[1]
        else :
            continue
    print (ans)