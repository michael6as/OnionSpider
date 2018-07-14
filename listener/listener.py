from abc import ABC, abstractmethod
import asyncio
import time

from listener.http_crawler import Http_Provider


class Listener(ABC):

    def __init__(self, base_url_action):
        self.url_list = [base_url_action]
        self.event_loop = asyncio.get_event_loop()

    @abstractmethod
    def start(self, sleep_interval, http_config, prop_action_dict):
        pass


class BasicListenerHandler(Listener):

    def start(self, sleep_interval, http_config, prop_action_dict):
        pass