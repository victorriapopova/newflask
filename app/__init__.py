# __init__.py или run.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Создаем экземпляр приложения Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Укажите свой путь к базе данных
db = SQLAlchemy(app)

# Импортируем маршруты после создания экземпляра приложения, чтобы избежать круговой зависимости
from app import routes

# Создаем таблицы в базе данных
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
