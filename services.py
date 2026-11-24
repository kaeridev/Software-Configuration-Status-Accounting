"""Business operations for selecting inventory items."""

from inventory import InventoryItem


def highest_stock_item(
    inventory_items: list[InventoryItem],
) -> InventoryItem:
    """Return the inventory item with the greatest stock quantity.

    Args:
        inventory_items: Inventory items to compare.

    Returns:
        The item with the highest quantity.
    """
    return max(inventory_items, key=lambda item: item.quantity)


def lowest_stock_item(
    inventory_items: list[InventoryItem],
) -> InventoryItem:
    """Return the inventory item with the least stock quantity.

    Args:
        inventory_items: Inventory items to compare.

    Returns:
        The item with the lowest quantity.
    """
    return min(inventory_items, key=lambda item: item.quantity)
