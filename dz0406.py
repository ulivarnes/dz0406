# Змінні та типи даних Частина 2

# Рівень 1 завдання 1:
print("Переведення температури в градуси за Фаренгейтом")
Celsiy = float(input("Введіть температуру за шкалою Цельсія: "))
Farengeyt =(Celsiy*9/5) + 32
print("Температура за Фаренгейтом", Farengeyt)

# Рівень 1 завдання 2:
print("Переведення євро у долари")
euro = float(input("Введіть Суму в євро : "))
kurs = float(input("Введіть курс євро до долару(наприклад: 1.05)," ))
dollars= euro*kurs
print("Сума у доларах", dollars)

# Рівень 2 завдання 3 
print("значення першого і другого розряду")
number = int(input("Введіть двозначне число: "))
print(number // 10)  # десятки
print(number % 10)   # одиниці

# Рівень 2 завдання 4
print("створити число, що містить введенні цифри")
a = int(input("Введіть першу цифру: "))
b = int(input("Ввести другу цифру: "))
number2 = int(str(a)+str(b))
print("Сформоване число:",number2)



# Рівень 3 завдання 5:
print("На різних рядках значення першого, другого і третього розряду")
number=int(input("Введіть тризначне число:"))
a=number//100
b=(number//10)%10
c=(number%10)
print("Перша цифра", a)
print("Друга цифра", b)
print("Третя цифра", c)
print (a+b+c)

# Рівень 3 завдання 6:
print("Сума вкладу та відсоткова ставка")
vklad_suma = float(input("Введіть суму вкладу:"))
stavka_vidsotkova = float(input("Введіть річну відсоткову ставку, %: "))
stavka_vidsotkova_rozrahunok = stavka_vidsotkova/100
suma_vklada_1rik = vklad_suma*(1+stavka_vidsotkova_rozrahunok)
suma_vklada_2rik = suma_vklada_1rik*(1+stavka_vidsotkova_rozrahunok)
suma_vklada_3rik = suma_vklada_2rik*(1+stavka_vidsotkova_rozrahunok)
suma_vklada_4rik = suma_vklada_3rik*(1+stavka_vidsotkova_rozrahunok)
suma_vklada_5rik = suma_vklada_4rik*(1+stavka_vidsotkova_rozrahunok)
zagalna_suma_vkladu = suma_vklada_5rik-vklad_suma
print("Сума вкладу за перший рік", suma_vklada_1rik)
print("Сума вкладу за другий рік", suma_vklada_2rik)
print("Сума вкладу за третій рік", suma_vklada_3rik)
print("Сума вкладу за четвертий рік", suma_vklada_4rik)
print("Сума вкладу за пятий рік", suma_vklada_5rik)
print("Загальна сума за пять років", suma_vklada_5rik)

