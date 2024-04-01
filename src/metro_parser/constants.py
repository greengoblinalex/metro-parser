# flake8: noqa
FROM = 0
SIZE = 100


class StoresID:
    MOSCOW = 10
    PETERSBURG = 15


class CategorySlugs:
    KOFE = 'kofe'


API_URL = 'https://api.metro-cc.ru/products-api/graph'
COOKIES = {
    'metroStoreId': '10',
    'manual_input_tooltip': '1',
    '_slid_server': '6609569d6296beaa350aae4a',
    '_slsession': '9B39C2B2-8BB2-4A10-BB43-18B9C8660513',
    'name_highlight': '1',
    '_slid': '6609569d6296beaa350aae4a',
    'metro_api_session': 'tazmOsOFa5tlHqHJJ85ZkG4iegDUaEYAXJAd96Lr',
    'metro_user_id': '580207ededae38d5e9cb9220f2d59f65',
    'tmr_lvid': '5d92c4599436c97ea410f4a68d02f05a',
    'tmr_lvidTS': '1711888031929',
    '_ym_uid': '1711888032809592651',
    '_ym_d': '1711888032',
    '_gcl_au': '1.1.2010742661.1711888032',
    '_ga': 'GA1.1.1920912170.1711888032',
    '_ym_isad': '2',
    'mindboxDeviceUUID': '73b4d1fb-242c-4e76-b963-3527fdd3a080',
    'directCrm-session': '%7B%22deviceGuid%22%3A%2273b4d1fb-242c-4e76-b963-3527fdd3a080%22%7D',
    '_ym_visorc': 'b',
    'uxs_uid': '0117dbe0-ef5a-11ee-8a8a-57f1744a5e5b',
    '_slfreq': '633ff97b9a3f3b9e90027740%3A633ffa4c90db8d5cf00d7810%3A1711895232%3B64a81e68255733f276099da5%3A64abaf645c1afe216b0a0d38%3A1711895232%3B649ea9cb5bdadc85d50474f9%3A65def0999e2a0f68530a11c7%3A1711895287',
    'sl_exit_intent_viewed': 'true',
    '_slfs': '1711888501008',
    'mp_5e1c29b29aeb315968bbfeb763b8f699_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e947a60c916e2-0e6dcb125a9d12-26001a51-1fa400-18e947a60ca16e2%22%2C%22%24device_id%22%3A%20%2218e947a60c916e2-0e6dcb125a9d12-26001a51-1fa400-18e947a60ca16e2%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    'mp_88875cfb7a649ab6e6e310368f37a563_mixpanel': '%7B%22distinct_id%22%3A%20%22%24device%3A18e947a61801799-0104088105e7ea-26001a51-1fa400-18e947a61801799%22%2C%22%24device_id%22%3A%20%2218e947a61801799-0104088105e7ea-26001a51-1fa400-18e947a61801799%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%7D',
    '_ga_VHKD93V3FV': 'GS1.1.1711888032.1.1.1711888502.0.0.0',
}
HEADERS = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://online.metro-cc.ru',
    'pragma': 'no-cache',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}
GRAPH_QL_QUERY = """
    query Query(
      $storeId: Int!,
      $slug: String!,
      $attributes: [AttributeFilter],
      $filters: [FieldFilter],
      $from: Int!,
      $size: Int!,
      $sort: InCategorySort,
      $in_stock: Boolean,
      $eshop_order: Boolean,
      $is_action: Boolean,
      $price_levels: Boolean
    ) {
      category (
        storeId: $storeId,
        slug: $slug,
        inStock: $in_stock,
        eshopAvailability: $eshop_order,
        isPromo: $is_action,
        priceLevels: $price_levels
      ) {
        id
        name
        slug
        parent_id
        meta {
          description
          h1
          title
          keywords
        }
        disclaimer
        description {
          top
          main
          bottom
        }
        breadcrumbs {
          category_type
          id
          name
          parent_id
          parent_slug
          slug
        }
        promo_banners {
          id
          image
          name
          category_ids
          virtual_ids
          type
          sort_order
          url
          is_target_blank
          analytics {
            name
            category
            brand
            type
            start_date
            end_date
          }
        }
        dynamic_categories(from: 0, size: 9999) {
          slug
          name
          id
          category_type
          dynamic_product_settings {
            attribute_id
            max_value
            min_value
            slugs
            type
          }
        }
        filters {
          facets {
            key
            total
            filter {
              id
              hru_filter_slug
              is_hru_filter
              name
              display_title
              is_list
              is_main
              text_filter
              is_range
              category_id
              category_name
              values {
                slug
                text
                total
              }
            }
          }
        }
        total
        prices {
          max
          min
        }
        pricesFiltered {
          max
          min
        }
        products(
          attributeFilters: $attributes,
          from: $from,
          size: $size,
          sort: $sort,
          fieldFilters: $filters
        ) {
          health_warning
          limited_sale_qty
          id
          slug
          name
          name_highlight
          article
          main_article
          main_article_slug
          is_target
          category_id
          url
          images
          pick_up
          rating
          icons {
            id
            badge_bg_colors
            rkn_icon
            caption
            image
            type
            is_only_for_sales
            stores
            caption_settings {
              colors
              text
            }
            stores
            sort
            image_png
            image_svg
            description
            end_date
            start_date
            status
          }
          manufacturer {
            id
            image
            name
          }
          packing {
            size
            type
            pack_factors {
              instamart
            }
          }
          stocks {
            value
            text
            eshop_availability
            scale
            prices_per_unit {
              old_price
              offline {
                price
                old_price
                type
                offline_discount
                offline_promo
              }
              price
              is_promo
              levels {
                count
                price
              }
              online_levels {
                count
                price
                discount
              }
              discount
            }
            prices {
              price
              is_promo
              old_price
              offline {
                old_price
                price
                type
                offline_discount
                offline_promo
              }
              levels {
                count
                price
              }
              online_levels {
                count
                price
                discount
              }
              discount
            }
          }
        }
      }
    }
  """
