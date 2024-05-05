from dataclasses import dataclass
from typing import List

@dataclass
class ParseInfo:
    title: str
    author: List[str]
    year: int
    volume: int
    found_volume: bool

    def __init__(self, title: str, author: List[str], year: int, volume: str, found_volume: bool = False):
        self.title = title
        self.author = author
        self.year = year
        self.volume = volume
        self.found_volume = found_volume
        