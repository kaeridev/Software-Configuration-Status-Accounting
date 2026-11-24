from inventory import inventory
from utils import highest_stock_item, lowest_stock_item

total_stock_value = sum(item["quantity"] * item["price"] for item in inventory)
print(f"Total stock value: ${total_stock_value:.2f}")

highest_item = highest_stock_item(inventory)
lowest_item = lowest_stock_item(inventory)

print(f"Item with highest stock: {highest_item['item_name']} ({highest_item['quantity']} units)")
print(f"Item with lowest stock: {lowest_item['item_name']} ({lowest_item['quantity']} units)")