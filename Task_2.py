num = int(input("Введите целое число: "))

h_old_version = ("%#x" % num)
print(num, "способ до версии 3.6 =", h_old_version)

h_new_version = (f'{num:#x}')
print(num, "способ начиная с версии 3.6 =", h_new_version)

h_function = hex(num)
print(num, "in hex =", h_function)