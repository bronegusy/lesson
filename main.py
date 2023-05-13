start = input("Хотите ли вы вычеслить что либо?")
while start != "нет":
    num1 = float(input("Первое число:"))
    num2 = float(input("Первое число"))
    oper = input("Операция:")
    if oper == "+" or oper == "сложить":
        print("Ответ:",num1 + num2)
    elif oper == "-" or oper == "вычеслить":
        print("Ответ:",num1 - num2)
    elif oper == "*" or oper == "умножить":
        print("Ответ:",num1 * num2)
    elif oper == "/" or oper == "разделить":
        print("Ответ:",num1 / num2)
    start = input("Хотите ли вы вычеслить что либо?")