# PlanZer

## 1. Цель
Приложение, способное решить проблемы планирования дня. Такие как:
1. Невозможность визуализировать расписание дня
2. Неспособность быстро и легко планировать


## 2. Особенности
1. ***Таймлайн*** на каждый день с возможностью указания начала и конца дня
2. ***Список задач***, который можно **фильтровать**, искать по **тегам** и расставлять по **приоритетам**
3. Разделение ***мероприятий*** и ***задач***
4. Добавление **повторяющихся** ***мероприятий*** и ***задач***
5. ***Синхронизация***. Встроенная, работающая на уровне приложения, или внешняя, реализуемая сторонними методами
6. Виджеты на Android 


## 3. Платформы 
1. Windows
2. Linux
3. Android
На Windows и Linux должен присутствовать CLI и TUI, помимо GUI. 


## 4. Функциональность

### 4.1 Список задач
1. Добавление
	С возможностью последующего изменения и удаления. При создании присутствуют атрибуты:
	- Название
	- Приоритет
	- Тег
	- Крайний срок
	- Оформление
2. Выбор тэгов
3. Поиск
4. Сортировка
	- По приоритету
	- По приближению к крайнему сроку
5. Размещение задачи на таймлайне

### 4.2 Таймлайн
1. Добавление мероприятия
2. Указание текущего времени
3. Не показывать время потраченное на сон
4. Пасхалки

### 4.3 Синхронизация
- Google
	или
- Syncthing


## 5. Стиль
Название - PLANZER


## 6. Codestyle
- 100% покрытие кода тайп-хинтингами [ссылка](https://youtu.be/dKxiHlZvULQ ), [ссылка](https://youtu.be/etkNsCRoKNY)
- Google Doc Style [ссылка](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Явные исключения


## 7. Процесс разработки
1. ✔ Подготовка
	- ✔ GitHub repo
2. ✘ Core
	- ✔ Классы заглушки. Вся архитектура без логики
	- ✔ Тесты
	- ✔ Логика удовлетворяющая тесты 
3. ✘ Система сохранения и загрузки
4. ✘ CLI
5. ✘ GUI
6. ✘ TUI
7. ✘ Системные функции
	- ✘ Windows уведомления
	- ✘ Linux уведомления
	- ✘ Android уведомления
	- ✘ Android виджеты
8. ✘ Обновления
9. ✘ Синхронизация


## 8. Архитектура
В `doc\`
