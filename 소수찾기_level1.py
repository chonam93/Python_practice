def solution(n):
    num=set(range(2,n+1))
    print(num)
    for i in range(2,n+1):
        if i in num:
            print(set(range(2*i,n+1,i)))
            num-=set(range(2*i,n+1,i))
    return len(num)
print(solution(20))

##에라토스테네스의 체
def numberOfPrime(n):
    '''https://stackoverflow.com/questions/3939660/sieve-of-eratosthenes-finding-primes-python'''
    sieve = [True]*(n+1)
    sieve[0] = sieve[1] = False
    num = 0
    for i, isprime in enumerate(sieve):
        if isprime:
            num += 1
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return num