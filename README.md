EasyConvert
===========

Коротко
-------
Лёгкий набор конвертеров (калькулятор, площадь, куб, температура, вес, память, время, удача) в Django-приложении.

Быстрый старт
------------
1. Убедитесь, что установлен Python 3.8+.
2. Создайте виртуальное окружение и активируйте его.

PowerShell (Windows):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Установите зависимости (если есть `requirements.txt`) или установите Django напрямую:

```powershell
pip install -r requirements.txt
# или
pip install django
```

4. Выполните миграции и запустите сервер:

```powershell
python manage.py migrate
python manage.py runserver
```

Где что находится
-----------------
- Шаблоны: `converters/templates/`
- Статика: `converters/static/converters/styles.css`
- Основной файл запуска: `manage.py`
- Приложение: `converters/`

Примечания
---------
- README минимален — если нужно, добавлю инструкции по развёртыванию, тестам или requirements.txt.
- Файл не содержит эмодзи и оформлен просто по запросу.
