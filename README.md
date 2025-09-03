# Тестовое для Pusto studio test2

Тестовое задание: система учёта игроков, уровней, бустов и призов, а также CSV

---
### Добавлена новая модель
В models.py была добавленна новая модель PlayerPrize для фиксация того, что игрок получил приз за уровень

---

## 📦 Стек

- Python 3.10+
- Django 4.x
- SQLite (по умолчанию)
- PEP8 / Читабельный и простой код

---

# Экспорт CSV

Реализован экспорт данных через HTTP:

Путь: /export/player-levels/

Формат: CSV

Строки: player_id, level_title, is_completed, prizes

### Экспорт данных в CSV
Реализован в views.py

http://localhost:8000/export/player-levels/
CSV-файл начнёт загружаться.

# Установка
git clone git@github.com:Mrclive7406/test_prosto2.git
cd test_prosto2

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver