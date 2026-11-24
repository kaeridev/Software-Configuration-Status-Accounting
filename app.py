"""Print an inventory table and stock-level summaries."""

from helpers import format_inventory_table
from inventory import InventoryItem, inventory
from services import highest_stock_item, lowest_stock_item

print(format_inventory_table(inventory))

highest_item: InventoryItem = highest_stock_item(inventory)
lowest_item: InventoryItem = lowest_stock_item(inventory)

print(f"Item with highest stock: {highest_item.item_name} ({highest_item.quantity} units)")
print(f"Item with lowest stock: {lowest_item.item_name} ({lowest_item.quantity} units)")