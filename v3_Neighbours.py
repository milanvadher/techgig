def find_max_sum(arr):
    # Function to return max sum such that
    # no two elements are adjacent
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return excl if excl > incl else incl


def main():
    # test case
    t = int(input())
    for _ in range(t):
        # no. of houses
        n = int(input())
        # tickets for each houses
        tickets = list(map(int, input().split()))
        print(n, tickets)
        print(find_max_sum(tickets))


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
