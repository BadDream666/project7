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
Тестирование находится в папке htmlcov. Для проверки статуса тестирования в веб- интерфейсе нужно запустить index.html