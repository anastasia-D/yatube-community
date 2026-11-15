# Yatube Community

Учебный блог на Django, начатый в Яндекс Практикуме. Это продолжение [Yatube](https://github.com/anastasia-D/yatube) с учётными записями, группами и публикациями пользователей.

## Мой вклад

- Добавила модель группы и связала её с публикациями через Django ORM.
- Сделала страницы группы, профиля автора и отдельной записи. Добавила пагинацию общей ленты и профиля.
- Добавила регистрацию и формы создания и редактирования записей. В версии для портфолио редактирование сохраняет изменения в существующей записи, а доступ к нему проверяется по автору.

## Локальный запуск

Команды рассчитаны на Python 3.12 в WSL или Linux. Выполни их из корня репозитория:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export DJANGO_SECRET_KEY="$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')"
python yatube/manage.py migrate
python yatube/manage.py runserver
```

Открой [главную страницу](http://127.0.0.1:8000/), зарегистрируйся, войди и создай запись. Чтобы добавить группу, создай администратора командой `python yatube/manage.py createsuperuser` и воспользуйся [админкой](http://127.0.0.1:8000/admin/). Письма для сброса пароля при локальном запуске выводятся в терминал.
