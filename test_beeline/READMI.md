***Для работы тестов на ОС Windows необходимо следующее окружение:***
1. Python версии 3.6 - 3.7
2. pip версии 19.3.1
3. Java 8 или 11 (для реализации allure отчёта)
4. allure версии 2 +, так же необходимо добавить в PATH
5. GIT

***Для запуска тестов выполнить следующие команды:***
1. _Перейти в папку, куда планируем клонировать репозиторий, командой `cd path/to/project`_
2. _Выполнить команду `git_init`_
3. _Склонировать проект на локальную машину командой: `git clone url/with/current_project`_
5. _Выполнить установку необходимого окружения командой `pip install -r requirements.txt`_
6. _Запустить тесты командой `pytest -v --alluredir allure_report`_
7. _Для того, что бы вывести отчёт в браузере, необходимо запустить команду `allure serve allure_report`_