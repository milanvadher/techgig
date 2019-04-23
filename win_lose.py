def compare_array(v, h, n):
    for j in range(n):
        if h[j] < v[j]:
            return 'LOSE'
    return 'WIN'


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        h = list(map(int, input().split()))
        v.sort()
        h.sort()
        print(compare_array(v, h, n))


if __name__ == '__main__':
    main()
