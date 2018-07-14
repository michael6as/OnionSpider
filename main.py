from data_modifiers.paste_factory import PasteFactory
from data_modifiers.property_normalizer import PropertyNormalizer
from listener.crawler_handler import DescendingAction, ExtractDataAction
from listener.http_crawler import Http_Provider
from data_modifiers.data_normalizer import *
from dal.tinydb_provider import TinyDbProvider

proxies = {
}

config = {
    'proxies': {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'},
    'url': 'http://nzxj65x32vh2fkhk.onion/api/json/list',
    'sleep': 4,
    'paste-tags': {'title': 'h4', 'author': 'div'}
}


def create_prop_action_dict(paste_factory, db_provider):
    return [
        DescendingAction('http://nzxj65x32vh2fkhk.onion/api/json/show/', 'pastes'),
        DescendingAction('http://nzxj65x32vh2fkhk.onion/api/json/list/', 'pages'),
        ExtractDataAction(paste_factory, db_provider, 'id')
    ]


def create_listener(paste_factory, db_provider):
    http_provider = Http_Provider(config['proxies'], config['url'], create_prop_action_dict(paste_factory, db_provider))
    return http_provider


def create_factory():
    prop_modifier_dict = [PropertyNormalizer('id', DummyModifier()),
                          PropertyNormalizer('author', ExchangeModifier('Guest')),
                          PropertyNormalizer('timestamp', DateTimeChanger()),
                          PropertyNormalizer('data', TrailingSpaceDeleter()),
                          PropertyNormalizer('title', DummyModifier())]
    return PasteFactory(prop_modifier_dict)


def create_db_provider():
    return TinyDbProvider()


crawler = create_listener(create_factory(), create_db_provider())
crawler.start_sampling(4,5)
