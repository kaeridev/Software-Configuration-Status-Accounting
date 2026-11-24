def highest_stock_item(inventory_items):
    return max(inventory_items, key=lambda item: item["quantity"])


def lowest_stock_item(inventory_items):
    return min(inventory_items, key=lambda item: item["quantity"])