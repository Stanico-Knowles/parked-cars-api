from dataclasses import dataclass, field
from typing import Dict

@dataclass
class CarSearchFiltersDto:
    color: str = None
    is_clean: bool = None
    max_hours: int = None
    min_hours: int = None
    max_price: float = None
    min_price: float = None
    page: int = 1
    page_size: int = 10

    def __post_init__(self):
        self.page = int(self.page)
        self.page_size = int(self.page_size)