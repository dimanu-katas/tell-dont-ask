from dataclasses import dataclass, field

from python.initial_code.src.domain.category import Category


@dataclass
class Product:
    name: str = ""
    price: float = 0
    category: Category = field(default_factory=Category)
