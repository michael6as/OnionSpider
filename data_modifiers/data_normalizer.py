import datetime

from abc import ABC, abstractmethod


class DataModifier(ABC):

    @abstractmethod
    def modify_data(self, data):
        pass


class ExchangeModifier(DataModifier):

    def __init__(self, new_string):
        self.new_string = new_string

    def modify_data(self, data):
        return self.new_string


class TrailingSpaceDeleter(DataModifier):

    def modify_data(self, data):
        clean_lines = [line.strip() for line in data.splitlines()]
        new_content = ''
        for clean_line in clean_lines:
            new_content += clean_line + ' '
        return new_content


class DateTimeChanger(DataModifier):
    def modify_data(self, data):
        date = datetime.datetime.utcfromtimestamp(int(data))
        return str(date)

class DummyModifier(DataModifier):
    def modify_data(self, data):
        return data