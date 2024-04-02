from src.metro_parser import metro_parser
from src.output_controller import output_controller
from src.metro_parser.constants import StoresID


def main():
    moscow_data = metro_parser.fetch_products_data(store_id=StoresID.MOSCOW, slug='kekw')
    petersburg_data = metro_parser.fetch_products_data(store_id=StoresID.PETERSBURG, slug='lol')

    output_controller.export_to_excel('output.xlsx', moscow_data, petersburg_data)


if __name__ == '__main__':
    main()
