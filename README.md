# Inventory App

A small Python inventory application that stores product information and calculates
the total value of the current stock.

## Features

- Stores item names, quantities, and prices
- Calculates the total stock value
- Includes helpers for finding the item with the highest or lowest stock

## Requirements

- Python 3

The project does not use external Python packages.

## Project Structure

- `app.py` - Calculates and prints the total inventory value
- `inventory.py` - Contains the inventory data
- `utils.py` - Provides stock-level helper functions
- `requirement.txt` - Dependency manifest (currently empty)

## Getting Started

From the project directory, run:

```powershell
python app.py
```

The application prints the total value of all inventory items. For the included
inventory data, the result is:

```text
Total stock value: $473.63
```

## Inventory Helpers

`utils.py` provides two helper functions:

```python
from utils import highest_stock_item, lowest_stock_item

print(highest_stock_item())
print(lowest_stock_item())
```

The functions return the inventory dictionary with the greatest or smallest
`quantity`, respectively.