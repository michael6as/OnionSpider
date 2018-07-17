import json
from typing import List
import requests
import asyncio
from urllib3.exceptions import ProtocolError

from listener.crawler_handler import BaseAction


class Http_Provider:

    def __init__(self, proxies, base_url, prop_action_dict: List[BaseAction]):
        self.http_session = requests.session()
        self.http_session.proxies = proxies
        self.prop_action_dict = prop_action_dict
        self.base_url = base_url
        self.sample_urls = [base_url]
        self.used_urls = []
        self.event_loop = asyncio.get_event_loop()

    def start_sampling(self, sleep_interval, num_of_workers):
        while True:
            tasks = []
            for i in range(num_of_workers):
                tasks.append(asyncio.ensure_future(self.__sample_site()))
            self.event_loop.run_until_complete(asyncio.wait(tasks))
            if len(self.sample_urls) == 0:
                asyncio.sleep(sleep_interval)
                self.used_urls.clear()
                self.sample_urls.append(self.base_url)

    async def __sample_site(self):
        while len(self.sample_urls) > 0:
            url = self.sample_urls.pop()
            res = await self.get_http(url)
            print('got answer from ' + url)
            json_content = json.loads(res.content)['result']
            for prop, val in json_content.items():
                for action in self.prop_action_dict:
                    if prop == action.prop_name:
                        inner_links = action.do_action(json_content)
                        if inner_links is not None:
                            for inner_link in inner_links:
                                if inner_link not in self.used_urls and inner_link not in self.sample_urls:
                                    self.sample_urls.append(inner_link)
            self.used_urls.append(url)

    async def get_http(self, url):
        try:
            return self.http_session.get(url, timeout=5000)
        except ProtocolError as e:
            proxies = self.http_session.proxies
            self.http_session.close()
            self.http_session = requests.session()
            self.http_session.proxies = proxies
            return self.get_http(url)
