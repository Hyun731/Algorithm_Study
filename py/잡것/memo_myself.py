memo = {}

def memo_fibo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = memo_fibo(n-1) + memo_fibo(n-2)
    return memo[n]

def roof(n):
    if n <= 1:
        return n
    return memo_fibo(n-1) + memo_fibo(n-2)

memo[0] = 0
memo[1] = 1
print(memo_fibo(10))