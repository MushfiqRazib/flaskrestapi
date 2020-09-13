
import itertools
import functools
# cachin fib

result = []
def memoize_fib(f):
    cache = {}
    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            result.append(cache[args])
            #print(cache)
            return cache[args]
    return decorated_function

@memoize_fib
def fib(num):
    if num < 2:
        return 1
    return fib(num-1) + fib(num-2)

def fibonacci(n):
    """ A generator for creating the Fibonacci numbers """
    a, b, counter = 1, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1

# Dynamic Programming Python implementation of Coin  
# Change problem 
def count(S, n):
    m = len(S) 
    # We need n+1 rows as the table is constructed  
    # in bottom up manner using the base case 0 value 
    # case (n = 0) 
    table = [[0 for x in range(m)] for x in range(n+1)] 
  
    # Fill the entries for 0 value case (n = 0) 
    for i in range(m): 
        table[0][i] = 1
    
    # Fill rest of the table entries in bottom up manner 
    for i in range(1, n+1): 
        for j in range(m):  
            # Count of solutions including S[j] 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
            
            # Count of solutions excluding S[j] 
            y = table[i][j-1] if j >= 1 else 0
  
            # total count 
            table[i][j] = x + y 

    return table[n][m-1] 

def cntMoney(num, money):
    mSz = len(money)
    numbers = [[0]*(1+num) for _ in range(mSz)]
    for mI in range(mSz): numbers[mI][0] = 1
    for mI,m in enumerate(money):
        for i in range(1,num+1):
            numbers[mI][i] = numbers[mI][i-m] if i >= m else 0
            if mI != 0: numbers[mI][i] += numbers[mI-1][i]
        print('m,numbers',m,numbers[mI])
    return numbers[mSz-1][num]

def find_changes(n, coins):
    if n < 0:
        return []
    if n == 0:
         return [[]]

    all_changes = []

    for last_used_coin in coins:
        combos = find_changes(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            all_changes.append(combo)

    return all_changes


def combinations_backtracking(target, numbers):
    tables = [[number] for number in numbers]
    new_tables = []
    result = []

    while tables:
        for table in tables:
            s = sum(table)
            for number in numbers:
                if number >= table[-1]:
                    if s + number < target:
                        new_tables.append(table + [number])
                    elif s + number == target:
                        result.append(table + [number])
        tables = new_tables
        new_tables = []
    return result


result = []

class FibDecorators(object):
    @classmethod
    def memoize_fib(f):
        cache = {}
        def decorated_function(*args):
            if args in cache:
                return cache[args]
            else:
                cache[args] = f(*args)
                result.append(cache[args])
                return cache[args]
        return decorated_function

@functools.lru_cache(maxsize=100)
def fibo(num):
    if num < 2:
        return 1
    return fibo(num-1) + fibo(num-2)

if __name__ == '__main__':
    print('fib number:')
    print(fib(11))
    print('result: ', result)

    ans = [ num for num in result if num < 11 and num > 1 ]
    print('ans: ', ans)

    print(combinations_backtracking(11, ans))

    #combi = [seq for i in range(len(ans), 0, -1) for seq in itertools.combinations(ans, i) if sum(seq) == 11]
    #print('combi: ', list(combi))
    
    #f = fibonacci(11)
    #for x in f:
     #   print(x, " ", end="")
    #print()

    # Driver program to test above function
    num = 11 
    arr = [1, 2, 3] 
    n = 4
    #x = count(ans, num)
    x = count(arr, n) 
    print (x)

    money = [1,5,10,25]

    #print('money,combinations',num,cntMoney(num, ans))

    print(combinations_backtracking(4, [1,2,3]))

    result = [fibo(n) for n in range(num)]
    print('fibo: ', result)