def fizzbuzz(n):
    if n <= 0 : 
        return []
    for i in range(1,101):
        variable = ''
        if i % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0:
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        else:
            return str(n)

