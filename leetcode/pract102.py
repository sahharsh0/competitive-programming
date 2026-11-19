
MOD = 10**9 + 7

def multiply(a, b):
    t = [0] * 5

    for i in range(3):
        for j in range(3):
            t[i+j] = (t[i+j] + a[i]*b[j]) % MOD

    return [
        (t[0] + t[3] + t[4]) % MOD,
        (t[1] + t[3] + 2*t[4]) % MOD,
        (t[2] + t[3] + 2*t[4]) % MOD
    ]


def geekonacci(A, B, C, N):
    A, B, C = A % MOD, B % MOD, C % MOD

    if N == 1: return A
    if N == 2: return B
    if N == 3: return C

    result = [1, 0, 0]
    base = [0, 1, 0]
    power = N - 1

    while power:
        if power & 1:
            result = multiply(result, base)
        base = multiply(base, base)
        power >>= 1

    return (result[0]*A + result[1]*B + result[2]*C) % MOD


T = int(input())
for _ in range(T):
    A, B, C, N = map(int, input().split())
    print(geekonacci(A, B, C, N))

