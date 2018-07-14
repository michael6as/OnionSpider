from typing import List
from data_modifiers.property_normalizer import PropertyNormalizer


class PasteFactory:
    def __init__(self, prop_modifier_dict: List[PropertyNormalizer]):
        self.prop_modifier_dict = prop_modifier_dict

    def create_paste(self, data_json):
        paste = {}
        for prop_normalizer in self.prop_modifier_dict:
            if prop_normalizer.prop_name in data_json:
                try:
                    paste[prop_normalizer.prop_name] = prop_normalizer.normalizer.modify_data(data_json[prop_normalizer.prop_name])
                except Exception as e:
                    print(e)
        return paste
