import time

def fibonnacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

for i in range(20, 55, 5):
    start = time.time()
    result = fibonnacci(i)
    end = time.time()
    duration = end - start
    print(i, result, duration)
