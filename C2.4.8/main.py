some_string = input("Введите число:\n")
try:
    some_number = int(some_string)
except:
    print("Разве это похоже на число??")
else:
    print("Вы ввели", some_number)
finally:
    print("Выход из программы")
