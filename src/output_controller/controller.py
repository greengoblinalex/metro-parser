import pandas as pd

from .exceptions import NoProductsFoundError
from .constants import METRO_BASE_URL


class OutputController:
    def export_to_excel(self, filepath: str, *args: dict) -> None:
        """
        Метод для экспорта данных о продуктах в формат Excel.

        Аргументы:
            filepath (str): Путь к файлу Excel, для сохранения данных.
            *args (dict): Произвольное количество словарей с данными о продуктах.
        """
        processed_products_data = self._process_products_data(*args)
        df = pd.DataFrame(processed_products_data)
        df.to_excel(filepath, index=False)

    @staticmethod
    def _process_products_data(*args: dict) -> list[dict]:
        """
        Метод для обработки данных о продуктах и подготовки к экспорту.

        Аргументы:
            *args (dict): Произвольное количество словарей с данными о продуктах.

        Возвращает:
            list[dict]: Список словарей с обработанными данными о продуктах.
        """
        all_products = []
        for data in args:
            products = data['data']['category']['products']
            all_products.extend(products)

        processed_products_data = []
        for product in all_products:
            prices = product['stocks'][0]['prices']

            price = prices['old_price'] if prices['is_promo'] else prices['price']
            promo_price = prices['price'] if prices['is_promo'] else '-'

            row = {
                'id': product['id'],
                'name': product['name'],
                'url': METRO_BASE_URL+product['url'],
                'price': price,
                'promo_price': promo_price,
                'brand': product['manufacturer']['name']
            }
            processed_products_data.append(row)

        if not processed_products_data:
            raise NoProductsFoundError('Продукты не найдены в переданных словарях')

        return processed_products_data


output_controller = OutputController()
