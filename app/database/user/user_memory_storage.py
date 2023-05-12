from app.database.storage import Storage
from app.database.user.user_mock import users


class UserMemoryStorage(Storage):
    _users = []

    def __init__(self):
        self._users = users

    def findAll(self):
        return self._users

    def find(self, name: str):
        return list(filter(lambda user: user['name'] == name, self._users))
    
    def save(self, user):
        self._users.append(user)

    def update(self, name: str, user):
        user_to_update = [user for user in self._users if user['name'] == name]
        if not user_to_update:
            return 'user not found'
        user_to_update[0]['name'] = user['name']

    def delete(self, name: str):
        user_to_delete = [user for user in self._users if user['name'] == name]
        if not user_to_delete:
            return 'user not found'
        self._users.remove(user_to_delete[0])