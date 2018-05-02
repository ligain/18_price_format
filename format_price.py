import argparse
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation


def format_price(price=None):

    if type(price) == bool:
        return

    try:
        converted_price = Decimal(price).quantize(
            Decimal('.01'), rounding=ROUND_HALF_UP)
    except (InvalidOperation, ValueError, TypeError):
        return

    return '{:,.2f}'.format(converted_price).replace(',', ' ').replace('.00', '')


def get_args():
    parser = argparse.ArgumentParser(
        description='CLI tool for parsing float point price'
    )
    parser.add_argument(
        '-p', '--price',
        help='Price to parse',
        required=True
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()

    print('Formatted price: {}'.format(format_price(args.price)))
