from dataclasses import dataclass

@dataclass
class CarsDto:
    license_plate: str
    color: str
    is_clean: bool
    hours: int
    price: float = 0.0