def caching_fibonacci():
    cache = {}  
    def fibonacci(n):
        if n in cache:  
            return cache[n]
        elif n <= 1:
            return n
        else:
            result = fibonacci(n - 1) + fibonacci(n - 2)  
            cache[n] = result  
            return result
    
    return fibonacci