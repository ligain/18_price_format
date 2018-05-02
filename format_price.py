import argparse


def format_price(price=None):
    try:
        converted_price = float(price) if type(price) != bool else None
        return '{:,.0f}'.format(converted_price).replace(',', ' ')
    except (ValueError, TypeError):
        pass


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
