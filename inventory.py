"""Inventory item model and sample inventory data."""

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class InventoryItem:
    """Represent an inventory item and its unit price."""

    item_name: str
    quantity: int
    price: Decimal


inventory: list[InventoryItem] = [
    InventoryItem("Notebook", 25, Decimal("2.99")),
    InventoryItem("Pen", 100, Decimal("0.99")),
    InventoryItem("Backpack", 12, Decimal("24.99")),
]