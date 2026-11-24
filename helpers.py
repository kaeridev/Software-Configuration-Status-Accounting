"""Presentation helpers for inventory output."""

from decimal import Decimal

from inventory import InventoryItem


def format_inventory_table(inventory_items: list[InventoryItem]) -> str:
    """Return an aligned table of items and their currency values."""
    headers = ("Item", "Quantity", "Unit Price", "Stock Value")
    rows: list[tuple[str, str, str, str]] = [
        (
            item.item_name,
            f"{item.quantity:,}",
            f"${item.price:,.2f}",
            f"${item.price * item.quantity:,.2f}",
        )
        for item in inventory_items
    ]
    total_value = sum(
        (item.price * item.quantity for item in inventory_items),
        start=Decimal("0"),
    )
    total_row = ("TOTAL", "", "", f"${total_value:,.2f}")
    widths = [len(header) for header in headers]

    for row in rows + [total_row]:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    row_format = (
        f"{{:<{widths[0]}}} | {{:>{widths[1]}}} | "
        f"{{:>{widths[2]}}} | {{:>{widths[3]}}}"
    )
    separator = "-+-".join("-" * width for width in widths)
    table_lines = [row_format.format(*headers), separator]
    table_lines.extend(row_format.format(*row) for row in rows)
    table_lines.extend((separator, row_format.format(*total_row)))
    return "\n".join(table_lines)
