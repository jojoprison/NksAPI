'''

WITH var AS
(SELECT '%' || 'NL-09-11-0С' || '%' AS article_mask)
SELECT  pr_t.is_published, pr_t.article, pr_t.id, pr_t.price, pr_t.title
FROM CatalogueApp_product pr_t,
     var
WHERE pr_t.article LIKE var.article_mask;

UPDATE CatalogueApp_product
SET price = ifnull(var.new_price, price),
is_published = True
FROM (SELECT 2937  AS desired_id,
-- null
null AS new_price) AS var
WHERE id = var.desired_id;

SELECT pr_t.title, pr_t.id, pr_t.article, pr_t.price
FROM CatalogueApp_product pr_t
WHERE pr_t.id = 2723
  AND pr_t.is_published;

SELECT count(id) FROM CatalogueApp_product WHERE is_published;

SELECT id, article, price FROM CatalogueApp_product
WHERE id = null AND is_published

UPDATE CatalogueApp_product
SET type_id = 7 where type_id = 1;

'''

import configparser
import sqlite3
from pathlib import Path

import requests
import validators

from common.utils.paths import get_project_root_path


class UpdatePhotos:
    labstol_root_url = 'https://labstol.ru'
    product_photos_dir = Path(f'{get_project_root_path()}/media/products/')

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        self.db_config = config['db']

    def get_connection(self):
        return sqlite3.connect(self.db_config['database'])

    def close_connection(self, connection):
        if connection:
            connection.close()

    def get_products_for_update_photo(self, is_published=True):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT id, photo_file_name FROM CatalogueApp_product WHERE is_published = ?',
                       (is_published,))
        product_ids = cursor.fetchall()

        self.close_connection(conn)

        return product_ids

    def get_product_photo_path(self, product_id):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT photo_file_name FROM CatalogueApp_product WHERE id = ?',
                       (product_id,))
        photo_path = cursor.fetchone()

        self.close_connection(conn)

        return photo_path

    def update_photo_path(self, product_id, photo_path):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('UPDATE CatalogueApp_product SET photo_file_name = ? WHERE id = ?',
                       (photo_path, product_id))

        conn.commit()
        self.close_connection(conn)

        return True

    def is_photo_exist(self, shorted_photo_name):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT photo_file_name FROM CatalogueApp_product WHERE photo_file_name = ?',
                       (shorted_photo_name,))
        photo_name = cursor.fetchone()

        self.close_connection(conn)

        return True if photo_name else False

    def update_photo(self, product_id, photo_path):
        try:
            is_photo_path_url = validators.url(photo_path)
        except TypeError:
            return False, 'parse_url_error'

        if is_photo_path_url:
            photo_file = self.get_photo_from_labstol(photo_path)

            if photo_file[0]:
                # print(photo_path.split('photos/'))
                if ('small_item' in photo_path) or ('small_shop_items' in photo_path):
                    new_shorted_path = photo_path.split('/')[-1]
                else:
                    try:
                        shorted_path = photo_path.split('photos/')[1]
                        shorted_path = shorted_path.rsplit('/', 1)[1]
                        shorted_path_parts = shorted_path.split('.')
                        shorted_path_model = shorted_path_parts[0]
                        shorted_path_photo_number = shorted_path_parts[1]
                        shorted_path_photo_number = shorted_path_photo_number.split('_')[0]
                        new_shorted_path = '.'.join([shorted_path_model, shorted_path_photo_number, 'jpg'])
                    except IndexError:
                        return False, 'cant_parse_path'

                if self.is_photo_exist(new_shorted_path):
                    return False, 'already_downloaded'
                else:
                    photo_file_name = self.product_photos_dir.joinpath(new_shorted_path)

                    with open(photo_file_name, 'wb') as handle:

                        for block in photo_file[1].iter_content(1024):
                            if not block:
                                break

                            handle.write(block)

                    self.update_photo_path(product_id, str(new_shorted_path))

                    return True
            else:
                # print(f'error: {product_id} by\n {photo_file[1]}')
                return False, 'error_while_req'
        else:
            return False, 'invalid_url'

    def fix_photo_path(self, product_id):
        photo_path = self.get_photo_path(product_id)[0]

        # фиксил, когда было двойное .jpg в конце
        # new = '.'.join(photo_path.split('.')[:3])
        # self.update_photo_path(product_id, str(new))

        photo_path = photo_path.split('D:\\PyCharm_projects\\NksAPI\\media\\products\\')
        if len(photo_path) > 1:
            new_photo_path = photo_path[1]
            self.update_photo_path(product_id, str(new_photo_path))
            return True
        else:
            return False

    def update_products_photo(self, is_published):
        products = self.get_products_for_update_photo(is_published=is_published)

        result = []

        # print(products)
        for product_id, product_photo_path in products:
            res = self.update_photo(product_id, product_photo_path)
            if len(res) == 2:
                result.append({product_id: res[1]})
            # когда криво сохранил с абсолютным путем до фотки
            # print(self.fix_photo_path(product_id))

        return result

    def get_photo_from_labstol(self, photo_url):
        response = requests.get(photo_url, stream=True)

        if not response.ok:
            return False, response
        else:
            return True, response


if __name__ == '__main__':
    update_photos = UpdatePhotos()

    res = update_photos.update_products_photo(is_published=False)
    print(res)

    # photo_path_ = update_photos.get_product_photo_path(972)[0]
    # update_photos.update_photo(972, photo_path_)
