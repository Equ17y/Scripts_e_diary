# Скрипты для электронного дневника

Набор функций для работы с базой данных электронного дневника школы.

## Установка

1. Положите файл `scripts.py` в папку с проектом (рядом с `manage.py`)
2. Запустите Django shell:

```bash
  python manage.py shell
```

3. Импортируйте функции:
```
>>> import scripts
>>> child = scripts.find_schoolkid('Фролов Иван')
```

## Использование

### Исправление оценок
```python
scripts.fix_marks(child)
```

### Удаление замечаний
```python
scripts.remove_chastisements(child)
```

### Создание похвалы
```python
scripts.create_commendation(child, "Математика")
scripts.create_commendation(child, "Музыка")
```

## Примеры работы

```python
# Для ученика Фролов Иван
>>> import scripts
>>> child = scripts.find_schoolkid('Фролов Иван')
>>> scripts.fix_marks(child)
>>> scripts.remove_chastisements(child) 
>>> scripts.create_commendation(child, "Математика")
```

## Обработка ошибок
```python
Если ученик не найден: выведет сообщение об ошибке
Если найдено несколько учеников: выведет предупреждение
Если предмет не найден: выведет сообщение об ошибке
```
## Требования
```python
Django
Доступ к базе данных электронного дневника
```
