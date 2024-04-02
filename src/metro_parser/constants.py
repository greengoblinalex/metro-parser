# flake8: noqa
FROM = 0
SIZE = 100


class StoresID:
    MOSCOW = 10
    PETERSBURG = 15


class CategorySlugs:
    KOFE = 'kofe'


API_URL = 'https://api.metro-cc.ru/products-api/graph'
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
