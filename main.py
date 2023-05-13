one_minuts_later = input("Хотители вы воспользоватся калькулятором который только умножает?(закончить - стоп)")
one_minuts_later = one_minuts_later.lower()
while one_minuts_later != "стоп":
    number_one = int(input("Введите первое число:"))
    number_two = int(input("Введите второе число:"))
    act = number_one * number_two
    print("Ответ:",act)
    one_minuts_later = input("Хотители вы воспользоватся калькулятором который только умножает?(закончить - стоп)")