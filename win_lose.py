def compare_array(v, h, n):
    for j in range(n):
        if h[j] < v[j]:
            return 'LOSE'
    return 'WIN'


def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        v = list(map(int, input().split()))
        h = list(map(int, input().split()))
        v.sort()
        h.sort()
        print(compare_array(v, h, n))


if __name__ == '__main__':
    main()
