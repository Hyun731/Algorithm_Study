memo = {}
def fibo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

def roof_fibo(n):
    if 1 >= n:
        return n
    return roof_fibo(n-1) + roof_fibo(n-2)

print(roof_fibo(15))