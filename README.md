# Выполненое тестовое задание TrafficProject
Текст задания - [Test](https://github.com/MITATED/TrafficProject/blob/master/task.md "Test")

Ответы:
1. [Объявить класс с полями и методами; унаследовать от него другой класс, переопределить метод](https://github.com/MITATED/TrafficProject/blob/master/task_1.py "Объявить класс с полями и методами; унаследовать от него другой класс, переопределить метод")
2. [Чем отличается список от кортежа?](https://github.com/MITATED/TrafficProject/blob/master/task_2.md "Чем отличается список от кортежа?")
3. [Что такое генератор и как он используется?](https://github.com/MITATED/TrafficProject/blob/master/task_3.md "Что такое генератор и как он используется?")
4. [Что такое list comprehension и как используется?](https://github.com/MITATED/TrafficProject/blob/master/task_4.md "Что такое list comprehension и как используется?")
5. [Что такое лямбда-функция и как используется?](https://github.com/MITATED/TrafficProject/blob/master/task_5.md "Что такое лямбда-функция и как используется?")
6. [Как итерировать числа от 1 до 10000?](https://github.com/MITATED/TrafficProject/blob/master/task_6.md "Как итерировать числа от 1 до 10000?")
7. [Имеется определение функции: def f(t, x={}):  ... Есть ли здесь проблема? Если есть, то в чём?](https://github.com/MITATED/TrafficProject/blob/master/task_7.md "Имеется определение функции: def f(t, x={}):  ... Есть ли здесь проблема? Если есть, то в чём?")
8. [Чем отличается ‘==’ от ‘is’?](https://github.com/MITATED/TrafficProject/blob/master/task_8.md "Чем отличается ‘==’ от ‘is’?")
9. [С помощью библиотеки http://www.seleniumhq.org и Python написать симуляцию поискового запроса в Google. Нельзя напрямую вызывать URL с параметрами поиска. Код на Python должен заполнить поле ввода запроса текстом и нажать на кнопку поиска. Опционально вывести список найденных результатов в консоль. Код должен запускаться и нормально выполняться как минимум в Linux или Mac OS X.](https://github.com/MITATED/TrafficProject/blob/master/task_9.py "С помощью библиотеки http://www.seleniumhq.org и Python написать симуляцию поискового запроса в Google. Нельзя напрямую вызывать URL с параметрами поиска. Код на Python должен заполнить поле ввода запроса текстом и нажать на кнопку поиска. Опционально вывести список найденных результатов в консоль. Код должен запускаться и нормально выполняться как минимум в Linux или Mac OS X.")

Для того чтобы запустить скрипт задания №9 
- На Linux
	1. нужно установить библиотеку selenium коммандой `pip3 install selenium`
	2. установить chromedriver `sudo apt-get install chromium-chromedriver`
- На Windows
	1. нужно скачать драйвер под вашу версию chrome на странице https://sites.google.com/a/chromium.org/chromedriver/downloads
	2. в строке `driver = Driver(executable_path="PATH")` вместо `PATH` вставить путь к скачаному драйверу.

Скрипт использует самописный модуль xelenium. Был написан мною для удобства работы с библиотекой selenium.
