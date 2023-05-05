# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!


from num2words import num2words

def switch_it_up(num):
        print(num2words(num, lang='en'))

num = int(input('Введите число от 0 до 9:'))
switch_it_up(num)