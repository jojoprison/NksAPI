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
import os
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

    def get_products_for_update_photo(self, only_is_published=True):
        conn = self.get_connection()

        cursor = conn.cursor()

        if only_is_published:
            cursor.execute('SELECT id, photo_file_name FROM CatalogueApp_product WHERE is_published = True')
            product_ids = cursor.fetchall()
        else:
            cursor.execute('SELECT id, photo_file_name FROM CatalogueApp_product')
            product_ids = cursor.fetchall()

        self.close_connection(conn)

        return product_ids

    def get_product_photo_path(self, product_id):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT photo_file_name FROM CatalogueApp_product WHERE id = ?',
                       (product_id,))
        photo_path = cursor.fetchone()[0]

        self.close_connection(conn)

        return photo_path

    def update_photo_path(self, product_id, photo_path):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('UPDATE CatalogueApp_product SET photo_file_name = ? WHERE id = ?',
                       (photo_path, product_id))

        conn.commit()
        self.close_connection(conn)

        return photo_path

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
                        new_shorted_path_without_extension = '_'.join([shorted_path_model, shorted_path_photo_number])
                        new_shorted_path = new_shorted_path_without_extension + '.jpg'
                    except IndexError:
                        return False, 'cant_parse_path'

                if self.is_photo_exist(new_shorted_path):
                    print(self.update_photo_path(product_id, str(new_shorted_path)))
                    return False, 'already_downloaded'
                else:
                    photo_file_name = self.product_photos_dir.joinpath(new_shorted_path)

                    with open(photo_file_name, 'wb') as handle:

                        for block in photo_file[1].iter_content(1024):
                            if not block:
                                break

                            handle.write(block)

                    print(self.update_photo_path(product_id, str(new_shorted_path)))

                    return True, 'updated'
            else:
                # print(f'error: {product_id} by\n {photo_file[1]}')
                return False, 'error_while_req'
        else:
            return False, 'invalid_url'

    def fix_photo_path_dots(self, product_id, photo_path):
        # когда .jpg в конце
        # new = '.'.join(photo_path.split('.')[:3])

        # photo_path = photo_path.split('D:\\PyCharm_projects\\NksAPI\\media\\products\\')
        # if len(photo_path) > 1:
        #     new_photo_path = photo_path[1]
        #     self.update_photo_path(product_id, str(new_photo_path))
        #     return True
        # else:
        #     return False

        # меняем все точки на поджопники - так пути до файлов невидно
        jpg_deleted = photo_path.replace('.jpg', '')
        underscore_path = jpg_deleted.replace('.', '_')
        new_path = underscore_path + '.jpg'

        return product_id, self.update_photo_path(product_id, new_path)

    def update_products_photo(self, is_published):
        products = self.get_products_for_update_photo(only_is_published=is_published)

        result = []

        # print(products)
        for product_id, product_photo_path in products:
            res = self.update_photo(product_id, product_photo_path)
            if not res[0]:
                result.append({product_id: res[1]})
            # когда криво сохранил с абсолютным путем до фотки
            # print(self.fix_photo_path(product_id))

        return result

    def fix_photo_path_if_copy_all(self):
        products = self.get_products_for_update_photo(only_is_published=False)

        for product_id, product_photo_path in products:
            if product_photo_path:
                res = self.fix_photo_path_if_copy(product_id, product_photo_path)
                if res:
                    print(res)

    def fix_photo_path_if_copy(self, product_id, photo_path):
        if photo_path:
            # меняем все точки на поджопники - так пути до файлов невидно
            jpg_deleted = photo_path.replace('.jpg', '')
            underscore_path = jpg_deleted.replace('.', '_')

            # удаляем хеш, сгенерированный для копий фоток (на лабстоле так было)
            underscore_path_parts = underscore_path.rsplit('_', 1)
            last_underscore_part = underscore_path_parts[-1]
            last_char_last_underscore_part = last_underscore_part[-1]

            if not last_char_last_underscore_part.isdigit():
                # берем все без части с хешем копии
                new_path = underscore_path_parts[0] + '.jpg'
                return product_id, self.update_photo_path(product_id, new_path)

    def fix_photos_path_dots_all(self):
        products = self.get_products_for_update_photo(only_is_published=False)

        for product_id, product_photo_path in products:
            # криво сохранил пути до фоток
            if product_photo_path:
                print(self.fix_photo_path_dots(product_id, product_photo_path))

    def rename_photos(self):
        file_names = os.listdir(self.product_photos_dir)

        for file_name in file_names:
            full_path = os.path.join(self.product_photos_dir, file_name)
            print(full_path)

            # фиксим двойное расширение
            converted = file_name.replace('.jpg', '')

            # меняем расширение если гифка
            find_gif_or_png = converted.rsplit('.', 1)
            if find_gif_or_png[-1] == 'gif' or find_gif_or_png[-1] == 'png':
                converted = find_gif_or_png[0]

            if '.' in converted:
                # меняем все точки на поджопники - так пути до файлов невидно
                converted = converted.replace('.', '_')

            new_file_name = converted + '.jpg'

            new_full_path = os.path.join(self.product_photos_dir, new_file_name)
            print(f'NEW: {new_full_path}')
            os.rename(full_path, new_full_path)

            # if new_file_name not in file_names:
            #     new_full_path = os.path.join(self.product_photos_dir, new_file_name)
            #     print(f'NEW: {new_full_path}')
            #
            #     os.rename(full_path, new_full_path)
            # else:
            #     os.remove(full_path)

    def get_photo_from_labstol(self, photo_url):
        response = requests.get(photo_url, stream=True)

        if not response.ok:
            return False, response
        else:
            return True, response


if __name__ == '__main__':
    update_photos = UpdatePhotos()

    # resss = update_photos.update_products_photo(is_published=False)
    # print(resss)


    # print(validators.url('https://labstol.ru/media/images/products/photos/2021/07/28/nl6421xM.590_8cq71ZM.jpg'))

    # update_photos.fix_photos_path_dots_all()

    update_photos.rename_photos()

    # p_id = 2726
    # p_p = update_photos.get_product_photo_path(p_id)
    # print(update_photos.fix_photo_path_if_copy(p_id, p_p))

    # update_photos.fix_photo_path_if_copy_all()

    # print(update_photos.fix_photo_path(2659, p_p))

    # photo_path_ = update_photos.get_product_photo_path(972)[0]
    # update_photos.update_photo(972, photo_path_)
