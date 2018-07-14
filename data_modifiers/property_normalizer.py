from dataclasses import dataclass

from data_modifiers.data_normalizer import DataModifier


@dataclass
class PropertyNormalizer:
    prop_name: str
    normalizer: DataModifier
