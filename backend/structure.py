from dataclasses import dataclass
from typing import List

@dataclass
class ParseInfo:
    title: str
    author: List[str]
    year: int

    def __init__(self, title: str, author: List[str], year: int):
        self.title = title
        self.author = author
        self.year = year
        