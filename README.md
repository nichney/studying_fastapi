Here I study FastAPI and backend programming for 12 weeks by ChatGPT roadmap just for fan.

# Here's ChatGPT's plan
🔥 Отлично, тогда давай сделаем конкретный план на **3 месяца (12 недель)**. Он будет заточен под твой выбор: **backend (Python) + DevOps-база**, с **минимумом фронтенда** для UI.

---

# 🚀 Дорожный план (3 месяца)

## Месяц 1 — база backend + контейнеры

**Цель:** поднять API, научиться базово работать с БД и упаковать всё в Docker.

### Неделя 1 - DONE

* Python: повторить основы (ООП, virtualenv, pip).
* Flask или FastAPI: установка, первый endpoint `/hello`.
* Git + GitHub (репозиторий, коммиты, README).

➡️ Мини-задача: сделать API с двумя эндпоинтами: `/hello` и `/time`.

### Неделя 2 - DONE

* FastAPI: работа с query params, POST-запросы.
* JSON и валидация данных (pydantic).
* Простая SQLite база.

➡️ Мини-задача: API для заметок (создать, прочитать, удалить заметку).

### Неделя 3

* PostgreSQL (docker контейнер).
* SQLAlchemy (ORM).
* Настроить связь API ↔ Postgres.

➡️ Мини-задача: ToDo API (CRUD: create/read/update/delete задачи).

### Неделя 4

* Docker: базовые команды.
* Dockerfile для твоего API.
* Docker Compose (api + db).

➡️ Мини-задача: запустить ToDo API и Postgres вместе через docker-compose.

---

## Месяц 2 — CI/CD + деплой

**Цель:** научиться автоматизировать сборку и выкатывать приложение на сервер.

### Неделя 5

* GitHub Actions: запуск тестов (pytest).
* Добавить линтеры (black, flake8).

➡️ Мини-задача: при каждом пуше в GitHub твой код проверяется тестами.

### Неделя 6

* GitHub Actions: билд docker-образа.
* DockerHub (опубликовать образ).

➡️ Мини-задача: CI/CD pipeline, который собирает и пушит образ твоего API.

### Неделя 7

* Взять VPS (Hetzner/Timeweb/OVH).
* Настроить ssh, firewall, nginx.
* Развернуть API вручную (docker-compose).

➡️ Мини-задача: твой ToDo API доступен в интернете по домену или IP.

### Неделя 8

* GitHub Actions: автоматический деплой на VPS.
* Простейший monitoring (healthcheck endpoint).

➡️ Мини-задача: пуш в main → приложение обновилось на сервере.

---

## Месяц 3 — фронт + дополнительные проекты

**Цель:** добавить фронтенд-обёртку и второй проект, чтобы показать разнообразие.

### Неделя 9

* HTML + CSS базово.
* JS: fetch API (GET/POST запросы).

➡️ Мини-задача: страница, которая берёт список задач из твоего API.

### Неделя 10

* React (только Create React App или Vite).
* Сделать компонент: форма для новой задачи + список задач.

➡️ Мини-задача: простой UI для ToDo API.

### Неделя 11

* Новый проект: URL shortener (FastAPI + Postgres + Redis).
* Docker-compose (api + db + redis).

➡️ Мини-задача: сервис сокращения ссылок (ввод url → короткая ссылка).

### Неделя 12

* CI/CD для URL shortener.
* Развернуть его на том же VPS.
* Сделать мини-портфолио (README + GitHub Pages).

➡️ Мини-задача: 2 проекта онлайн + красивый GitHub.

