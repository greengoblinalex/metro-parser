import requests
from requests.exceptions import RequestException

from exceptions import UnexpectedDataFormatError
from .constants import (
    API_URL,
    HEADERS,
    GRAPH_QL_QUERY,
    FROM,
    SIZE,
    CategorySlugs,
    StoresID
)


class MetroParser:
    def fetch_products_data(
        self,
        slug: str = CategorySlugs.KOFE,
        store_id: int = StoresID.MOSCOW,
        size: int = SIZE,
        from_: int = FROM,
        in_stock: bool = True
    ) -> dict:
        """
        Отправляет запрос к API Metro и возвращает данные о продуктах в формате JSON.

        Аргументы:
            slug (str): Slug категории продуктов (по умолчанию - кофе).
            store_id (int): ID магазина Metro (по умолчанию - Москва).
            size (int): Количество продуктов, запрашиваемых за один запрос (по умолчанию - 100).
            from_ (int): Индекс начала списка продуктов (по умолчанию - 0).
            in_stock (bool): Флаг, показывающий продукты только в наличии, если True
                             и все, если False (по умолчанию - True).

        Возвращает:
            dict: Результат запроса в формате JSON.
        """
        try:
            json_data = {
                'query': GRAPH_QL_QUERY,
                'variables': {
                    'isShouldFetchOnlyProducts': True,
                    'slug': slug,
                    'storeId': store_id,
                    'sort': 'default',
                    'size': size,
                    'from': from_,
                    'filters': [
                        {
                            'field': 'main_article',
                            'value': '0',
                        },
                    ],
                    'attributes': [],
                    'in_stock': in_stock,
                    'eshop_order': False,
                },
            }

            response = requests.post(
                url=API_URL,
                headers=HEADERS,
                json=json_data
            )

            try:
                products_data = response.json()
                products_data['data']['category']['products']
            except (KeyError, TypeError):
                raise UnexpectedDataFormatError('Неожиданный формат данных в результате запроса')

            return products_data
        except RequestException as exception:
            print(f'Ошибка при выполнении запроса: {exception}')


metro_parser = MetroParser()
