
from userexceptions import InvalidPasswordError
def check_password(user_input, actual_password):
    if user_input != actual_password:
        raise InvalidPasswordError("Incorrect password! Access denied.")
    else:
        print("Password is correct! Access granted.")


def main():
    actual_password = "Python123"
    user_input = input("Enter the password: ")

    try:
        check_password(user_input, actual_password)
    except InvalidPasswordError as e:
        print(e)


if __name__ == "_main_":
    main()