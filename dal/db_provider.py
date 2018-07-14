from abc import ABC, abstractmethod


class DbProvider(ABC):
    @abstractmethod
    def insert_paste(self, paste):
        pass

    @abstractmethod
    def search_paste(self, paste):
        pass
