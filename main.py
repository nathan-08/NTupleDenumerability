'''Demonstration of the denumerability of the set of n-tuples of natural numbers for a fixed n'''
'''that is, there exists a one-to-one mapping from (N^n -> N) for any finite n'''

def f2(n, m):
    '''N^2 -> N'''
    return 2**(n-1) * (2*m - 1)

def f2inv(a):
    '''N -> N^2'''
    n = 1
    m = 0
    while (a % 2 == 0):
        n += 1
        a /= 2
    m = (a + 1) / 2
    return (n, m)

def f3(n,m,s):
    '''N^3 -> N'''
    return f2(n,f2(m,s))

def f3inv(a):
    '''N -> N^3'''
    (n, b) = f2inv(a)
    (m, s) = f2inv(b)
    return (n, m, s)

def fNinv(n, a):
    '''N -> N^n'''
    nums = [a]
    while len(nums) < n:
        (x,y) = f2inv(nums.pop())
        nums.append(x)
        nums.append(y)
    return nums

for i in range(1, 20):
    print(f'{i}:'.ljust(5) + f'{fNinv(5, i)}')

