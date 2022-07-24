from dataclasses import dataclass


@dataclass
class CarSearchFiltersDto:
    color: str = None
    is_clean: bool = None
    hours: int = None
    max_price: float = None
    min_price: float = None
    page: int = 1
    page_size: int = 10

    def __post_init__(self):
        self.page = int(self.page)
        self.page_size = int(self.page_size)