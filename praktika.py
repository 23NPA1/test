# 1 задание
def sum_s_while(i):
    total = 0
    current_num = 1
    while current_num <= i:
        total += current_num
        current_num += 1
    return total
    

print(sum_s_while(10))

def sum_s_for():
    i = 10
    total_sum = 0
    current_num = 1
    for current_num in range(1, i + 1):
        total_sum += current_num


sum_s_for()

# 2 задание
def chet_s_while():
    i = 10
    current_num = 0
    while current_num <= i:
        print(current_num)
        current_num += 2
chet_s_while()

# 3 задание
def chet_ili_ne():
    number = 6
    if number % 2 == 0:
        print("число четное")
    else:
        print("число нечетное")

chet_ili_ne()

# 4 задание
def ocenka():
    score = 100
    if score < 0 or score > 100:
        print("Ошибка: чел ты..........")
        return
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

ocenka()

# 5 задание
def vozrast():
    age = 52
    if age < 13:
        print("Вам менее 13 лет (ребёнок)")
    elif 13 <= age <= 19:
        print("Вам от 13 до 19 лет (подросток)")
    elif 20 <= age <= 59:
        print("Вам от 20 до 59 лет (взрослый)")
    else:
        print("Вам 60 лет и больше (пожилой человек)")

vozrast()

# Условия. Работа с if/elif/else. Задача 4.
def triangle(a, b, c):
    if a + b > c:
        if a + c > b:
            if c + b > a:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(triangle(3, 4, 100))    
# 7 задание 
def calculator(operator):
    num1 = 5
    num2 = 5
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Ошибка: на ноль делить нельзя")
            return
        result = num1 / num2
    else:
        print("Неверный оператор")
        return


calculator("+")
calculator("-")
calculator("*")
calculator("/")
calculator("%")

# 8 задание
spisok = []
if not spisok:
    print("Список пуст")
else:
    spisok.sort()
    big_number = spisok[-1]
    
# 9 задание
def summa(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

spisok = [5, 2, 4, 3, 1, 6]
result = summa(spisok)


# Циклы. Работа с for и while. Задача 2.

def func_while(i):
    spisok = []
    n = 0
    while n <= i:
        if n % 2 == 0:
            spisok.append(n)
        n += 1
    return spisok
def func_for(i):
    spisok = []
    for n in range(0, i + 1):
        if n % 2 == 0:
            spisok.append(n)
    return spisok
        




print(func_for(20))
print(func_while(10))
