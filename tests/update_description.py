import configparser
import sqlite3
from pathlib import Path

from common.utils.paths import get_project_root_path


class UpdateDescriptions:
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

    def update_description(self, product_id, description):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('UPDATE CatalogueApp_product SET description = ? WHERE id = ?',
                       (description, product_id))

        conn.commit()
        self.close_connection(conn)

        return description

    def get_description(self, product_id):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT description FROM CatalogueApp_product WHERE id = ?',
                       (product_id,))
        photo_name = cursor.fetchone()

        self.close_connection(conn)

        return True if photo_name else False

    def get_products_description(self):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT id, description FROM CatalogueApp_product')
        products_description = cursor.fetchall()

        self.close_connection(conn)

        return products_description

    def delete_starting(self, description):
        new_desc = description.replace('Описание товара:', '')
        return new_desc

    def update_desc_all(self):
        products_description = self.get_products_description()

        for product_id, desc in products_description:
            new_desc = self.delete_starting(desc)
            print(new_desc)
            self.update_description(product_id, new_desc)


if __name__ == '__main__':
    ud = UpdateDescriptions()
    ud.update_desc_all()
