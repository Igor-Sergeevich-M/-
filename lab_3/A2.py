import string
password = input("Введите надёжный пароль: ")
lenght = len(password)
without_specail_symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits
all_conditions = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*'

errors = []
if all(symbol in  all_conditions for symbol in password)  and lenght >= 8:
    errors.append("Пароль надёжен ")
if any(symbol.isdigit() for symbol in password) == False:
    errors.append("В пароле отсутсвуют цифры")
if any(symbol.islower() for symbol in password) == False:
    errors.append("В пароле отсутствуют строчные буквы")
if any(symbol.isupper() for symbol in password) == False:
    errors.append("В пароле отсутствуют заглавные буквы")
if all(symbol in without_specail_symbols for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")
if lenght <=8:
    errors.append("Длина пароля не равна 8")
print(errors)
