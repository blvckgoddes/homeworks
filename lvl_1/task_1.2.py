# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
import random
songs = random.sample(my_favorite_songs, 3)
summ = (songs[0][1] + songs[1][1] + songs[2][1])
print(f'Три песни звучат {round(summ, 2)} минут')



# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

import random
playlist = list(my_favorite_songs_dict.items())
random_s = random.sample(playlist, 3)
playlist = random_s[0][1] + random_s[1][1] + random_s[2][1]
print(f'Три песни звучат {round(playlist,2)} минут' )

# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random
import random
random_songs = random.sample(my_favorite_songs, 3)
print(random_songs[0][0] + ', ' + random_songs[1][0] + ', ' + random_songs[2][0])


# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 
import datetime
time = datetime.datetime.now()
print(time.strftime('%M минут %S секунд'))




