# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!

n = int(input('Введите номер месяца:'))
lst = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
if n > 12:
    print('Такого месяца нет!')
elif n == 2:
    print('Вы ввели февраль. 28 дней')
elif n in [1, 3, 5, 7, 8, 10, 12]:
    print(f'Вы ввели {lst[n-1]}. 31 дней')
else:
    print(f'Вы ввели {lst[n-1]}. 30 дней')