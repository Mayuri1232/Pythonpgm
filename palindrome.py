def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

num = int(input("Enter a number: "))

if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
