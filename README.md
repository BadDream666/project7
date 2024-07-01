# Проект для обучения языку программирования Python

## Описание:
Данный проект создан в качестве обучения языку программирования Python по программе обучения от Skypro.

## Установка:
1. Клонируйте репозиторий:
```
git clone https://github.com/BadDream666/project7.git
```
2. Убедитесь что все файлы стоят на своих местах. **Должно быть не менее трёх файлов** в папке src

## Использование:
1. Удалите в файлах masks.py, widget.py и processing.py пометку комментария("#") 
2. Запустите код
3. Закоментируйте код в изначальный вид

### Пример использования:
1. В конце каждой функции есть закомментированный print
```
def sort_by_date(original_list: list[dict], reverse=True) -> list[dict]:
    """Функиця, сортирующая исходные данные по дате"""

    sorted_list: list[dict] = sorted(original_list, key=lambda inform_state: inform_state["date"], reverse=reverse)
    return sorted_list

#print(sort_by_date(original_list, True))
```
2. Удалите символ # и запустите код

### Тестирование:
* Тестирование находится в папке htmlcov. Для проверки статуса тестирования в веб- интерфейсе нужно запустить index.html
* В папке tests хранятся проверки. Их можно запускать напрямую из файла или в терминале ввести комаду pytest. 
* Ожидаемый результат успешного тестирования -> Все тесты отмечены зеленым, никаких ошибок не выдало.

### Дополнительные функции кода:
1. В проекте появилась новая функция. Данная функция реализует генератор для обработки массивов транзакции. Это требуется
для удобства и быстроты финансовым аналитикам находить нужную информацию о транзакции и проводить анализ данных.
Пример:
```
def filter_by_currency(info: list[dict], usd: str) -> Iterator[int]:
    """Функция выдает по очереди операции, в которых указана заданная валюта"""

    for k in info:
        if k["operationAmount"]["currency"]["code"] == usd:
            yield k["id"]


usd_transactions = filter_by_currency(transactions, "USD")
```
2. В проекте добавлен декоратор, который позволяет обеспечить более глубокий контроль и анализ поведения программы в 
процесс её выполнения.