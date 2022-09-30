# Goit_python_web
1. Запускаем виртуальное окружение venv
2. Запускаем докер. Создаем базу данных psql
    docker run --name alembic-exemple -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres

3. создание таблиц файл - models.py
 использовать alembic revision -m 'Init' уже после создания и настроек "alembic init alembic"
 загрузить в базу alembic upgrade head
4. Наполнение базы данных фейковыми данными файл - seed.py
5. Просмотр базы данных main.py приведено 2 варианта
