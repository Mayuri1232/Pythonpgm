def factorial(n):
    if n < 1 or n ==0:
        return "Factorial does not exist for numbers."
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a number: "))
print(f"The factorial of {num} is: {factorial(num)}")

