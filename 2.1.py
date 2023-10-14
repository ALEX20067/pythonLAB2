def is_password_good(password):
    if len(password)<8:
        return False
    upper = any(char.isupper() for char in password)
    if not upper:
        return False
    is_digit = any(char.isdigit() for char in password)
    if not is_digit:
        return False
    return True
password=(input("Введите пароль:"))
result = is_password_good(password)
if result:
    print("Пароль надежный.")
else:
    print("Пароль недостаточно надежный.")

is_password_good(password)
