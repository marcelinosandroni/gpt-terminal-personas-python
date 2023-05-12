from flask import Flask
from app.database.user.user_memory_storage import UserMemoryStorage

app = Flask(__name__)
user_storage = UserMemoryStorage()


@app.route('/users')
def user_controller():
    return user_storage.findAll()
