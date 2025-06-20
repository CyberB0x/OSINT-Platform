# 🕵️ OSINT Platform

**OSINT Platform** — это централизованная веб-система для автоматизированного сбора информации из открытых источников (OSINT). Подходит для ИБ-аналитиков, журналистов, следователей и исследователей киберугроз.

---

## 🚀 Возможности

- 🔍 Проверка Email (поиск в базах утечек)
- 🌐 WHOIS / DNS / SSL анализ доменов
- 🧠 Хранение истории запросов
- 📡 Celery + Redis: фоновые задания
- 📊 Красивый веб-интерфейс на Bootstrap
- 🔄 Автообновление результатов (AJAX)
- 🛠 Расширяемая архитектура под Telegram-бота и API

---

## 🧩 Стек технологий

- Python 3.12+
- Django 5+
- Celery
- Redis
- Bootstrap 5
- SQLite / MySQL / PostgreSQL

---

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/osint-platform.git
   cd osint-platform
   ```
---
# Установите зависимости
**pip install -r requirements.txt**

# Запустите Celery
```bash
   celery -A osint_platform worker --loglevel=info 
```
---

# 📁 Структура проекта
```commandline
   osint_platform/
│
├── core/                # Основное приложение
│   ├── models.py
│   ├── views.py
│   ├── tasks.py
│   ├── services/
│   │   ├── email_check.py
│   │   └── whois_check.py
│   └── templates/
│       └── index.html
│
├── osint_platform/      # Конфигурация Django
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE

```

# 📌 TODO / Идеи
* 🤖 Telegram-бот
* 📥 Импорт CSV / API
* 📤 PDF-экспорт отчётов
* 🔐 Авторизация и разграничение доступа

