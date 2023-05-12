import abc


class Storage(abc.ABC):
    @abc.abstractmethod
    def findAll(self):
        pass

    @abc.abstractclassmethod
    def find(self, id: str, name: str):
        pass

    @abc.abstractclassmethod
    def save(self, entity):
        pass

    @abc.abstractclassmethod
    def update(self, id: str, entity):
        pass

    @abc.abstractclassmethod
    def delete(self, id: str):
        pass
