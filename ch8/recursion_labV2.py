import time

cache = {}

def fibonnacci(n):
    global cache
    if n in cache:
        return cache[n]

    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibonnacci(n-1) + fibonnacci(n-2)
    cache[n] = result
    return result

start = time.time()

for i in range(0, 101):
    result = fibonnacci(i)
    print(i, result,)

finish = time.time()
duration = finish - start
print('Computed all 100', 'in', duration, 'seconds')
