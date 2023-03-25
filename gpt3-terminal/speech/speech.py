import abc

class Speech(abc.ABC):
    @abc.abstractmethod
    def say(self, text):
        pass



