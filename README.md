В проекті "SOAP" реалізована можливість автоматизації процесу виклику методів веб-сервісів з використанням мови програмування python і бібліотеки zeep.
Структура проекту: пакети (models, tests), конфігураційний файл config.json, файл з тестовими даними test_data.json, файл з фікстурами (preconditions до
запуску тестів) conftest.py.
В пакеті models реалізовані загальні методи, необхідні для запуску тестів, відкриття конфігураційних файлів, файлів тестових даних. В пакеті tests
створені перевірки методів.
Пакет tests містить перевірки таких методів веб-сервісів:
1) createApplication (test_createApplication.py)
2) getCards (test_getCards.py)
Запуск даних файлів необхідно виконувати в середовищі (IDE) PyCharm.

Інструкції запуску файлів тестів

1) Перед запуском теста test_createApplication.py на виконання потрібно підготувати файл з даними (параметрами), вказати шлях до нього і виконати мапинг полів
(файла .xlsx) з параметрами метода в файлі test_createApplication.py.
2) Для запуску test_getCards.py на виконання необхідно підготувати тестові дані і занести в файл test_data.json. В конфігураційному файлі зазначається набір
даних, з яким запускаються тести на виконання.
