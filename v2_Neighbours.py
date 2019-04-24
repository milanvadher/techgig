def main():
    # test case
    t = int(input())
    for _ in range(t):
        # no. of houses
        n = int(input())
        # tickets for each houses
        tickets = list(map(int, input().split()))
        # print(n, tickets)
        tickets_sum = []
        _temp = []
        for i in range(n):
            for j in range(i + 2, n):
                a = tickets[i] if tickets[i] > 0 else 0
                b = tickets[j] if tickets[j] > 0 else 0
                if a is not 0 and b is not 0:
                    tickets_sum.append([a + b, str(b) + str(a)])
                    _temp.append(a + b)
                elif a is not 0:
                    tickets_sum.append([a + b, str(a)])
                    _temp.append(a + b)
                elif b is not 0:
                    tickets_sum.append([a + b, str(b)])
                    _temp.append(a + b)
        # print(tickets_sum)
        # print(_temp)
        ans = []
        if len(tickets_sum) > 0:
            g = (j for j, e in enumerate(_temp) if e == max(_temp))
            for _ in range(_temp.count(max(_temp))):
                ans.append(tickets_sum[next(g)])
        # print('ans', ans)
        if len(ans) == 1:
            print(ans[0][1])
        elif len(ans) > 1:
            ans_ = ans[0][1]
            for k in range(1, len(ans)):
                # print(ans_[0], ans[k][1][0])
                if int(ans_[0]) < int(ans[k][1][0]):
                    ans_ = ans[k][1]
            print(ans_)


if __name__ == '__main__':
    main()


# 10 11 10 9 : 1010
# 4 5 4 3 -2 -2 -2 4 5 4 3 : 4444
# 12 15 25 -15 35 : 352512
# 1 2 50 3 2 50 : 50501
# 9 1 2 8 : 89
# 5 4 6 8 : 85
# 9 1 2 8 5 4 6 8 : 8489
# 4 7 4 1 1 5 : 544
# 3 7 5 1 1 5 : 553
# 48 65 184 24 17 108 56 423 148 44 : 4442310818448