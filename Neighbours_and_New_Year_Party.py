def choose_ans(tickets, t):
    if tickets[t] < 0 or tickets[t + 2] < 0:
        if tickets[t] > 0:
            return tickets[t]
        elif tickets[t + 2] > 0:
            return tickets[t + 2]
    else:
        if tickets[t + 2] == 0 or tickets[t] == 0:
            if tickets[t + 2] == 0 and tickets[t] == 0:
                return None
            elif tickets[t + 2] == 0:
                return tickets[t]
            elif tickets[t] == 0:
                return tickets[t + 2]
        else:
            return str(tickets[t + 2]) + str(tickets[t])


def calculate_result(tickets, n):
    temp_ans = []
    for i in range(n - 2):
        if tickets[i] < 0 or tickets[i + 2] < 0:
            if tickets[i] > 0:
                temp_ans.append(tickets[i])
            elif tickets[i + 2] > 0:
                temp_ans.append(tickets[i + 2])
        else:
            temp_ans.append(tickets[i] + tickets[i + 2])

    t = temp_ans.index(max(temp_ans))
    g = (j for j, e in enumerate(temp_ans) if e == max(temp_ans))

    if temp_ans.count(max(temp_ans)) > 1:
        temp_index = []
        temp_ans_ = []
        for _ in range(temp_ans.count(max(temp_ans))):
            temp_index.append(next(g))
        for j in temp_index:
            ans = choose_ans(tickets, j)
            if ans is not None:
                temp_ans_.append(ans)
        temp = []
        first_letter = []
        for k in temp_ans_:
            temp.append(k[0])
        for item in temp_ans_:
            first_letter.append(item[0])
        return temp_ans_[first_letter.index(max(first_letter))]
    else:
        return choose_ans(tickets, t)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tickets = list(map(int, input().split()))
        # print(tickets)
        print(calculate_result(tickets, n))


if __name__ == '__main__':
    main()
