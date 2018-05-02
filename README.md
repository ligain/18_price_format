
# Price Formatter  
  
Very simple tool to format number with spaces as thousands separator.
Example: `3245.000000` -> `3 245.00`
# Usage as CLI
```bash
$ python format_price.py -p 34534003459830459834059830945380453455.345
Formatted price: 34 534 003 459 830 460 657 132 492 270 705 049 600.35
```
# Usage as module
```python
>>> from format_price import format_price
>>> format_price('3245.000000')
'3 245.00'
```
# Run tests
```bash
$ python -m unittest tests
```
# Project Goals  
  
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)