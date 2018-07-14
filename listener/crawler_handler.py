import asyncio
import time
from abc import ABC, abstractmethod
from urllib.parse import urljoin


class BaseAction(ABC):
    def __init__(self, prop_name):
        self.prop_name = prop_name

    @abstractmethod
    def do_action(self, result):
        pass


class DescendingAction(BaseAction):
    def __init__(self, desc_uri_prefix, prop_name):
        super().__init__(prop_name)
        self.desc_uri_prefix = desc_uri_prefix

    def do_action(self, result):
        value = result[self.prop_name]
        if type(value) is int:
            return self.__extract_inner_links(range(0, value))
        else:
            return self.__extract_inner_links(value)

    def __extract_inner_links(self, link_list):
        for link in link_list:
            inner_url = urljoin(self.desc_uri_prefix, str(link))
            yield inner_url


class ExtractDataAction(BaseAction):
    def __init__(self, paste_factory, db_provider, prop_name):
        super().__init__(prop_name)
        self.paste_factory = paste_factory
        self.db_provider = db_provider

    def do_action(self, result):
        paste = self.paste_factory.create_paste(result)
        try:
            self.db_provider.insert_paste(paste)
        except Exception as e:
            print('Couldnt write to DB '+ e)
