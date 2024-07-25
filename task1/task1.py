def caching_fibonacci(n):
   cache = {
       0: 0,
       1: 1
   }
   def fibonacci(n):
       if (n in cache):
           return cache[n]
       return fibonacci(n - 1) + fibonacci(n - 2)
   return fibonacci(n)

# Отримуємо функцію fibonacci
fib = caching_fibonacci

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(15))