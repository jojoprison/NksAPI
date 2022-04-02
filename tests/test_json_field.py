import configparser
import sqlite3
from pathlib import Path

from common.utils.paths import get_project_root_path
import json


class JsonFields:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(f'{get_project_root_path()}/config.ini')
        self.db_config = config['db']

    def get_connection(self):
        return sqlite3.connect(self.db_config['database'])

    def close_connection(self, connection):
        if connection:
            connection.close()

    def update_feature(self, product_id, feat):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('UPDATE CatalogueApp_product SET feature = ? WHERE id = ?',
                       (feat, product_id))

        conn.commit()
        self.close_connection(conn)

        return feat

    def get_feature(self, product_id):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT feature FROM CatalogueApp_product WHERE id = ?',
                       (product_id,))
        feature = cursor.fetchone()

        self.close_connection(conn)

        return feature

    def get_products_feature(self):
        conn = self.get_connection()

        cursor = conn.cursor()

        cursor.execute('SELECT id, feature FROM CatalogueApp_product')
        products_description = cursor.fetchall()

        self.close_connection(conn)

        return products_description

    def json_loads(self, feat):
        llll = json.loads(feat)
        return llll

    def json_dumps(self, feat):
        dddd = json.dumps(feat)
        return dddd

    def json_feats(self):
        products_description = self.get_products_feature()

        for product_id, feat in products_description:
            # print(json.dumps(feat))
            fffff = self.json_dumps(feat)
            # print(fffff)
            self.update_feature(product_id, fffff)


if __name__ == '__main__':
    ud = JsonFields()
    # print(type(ud.get_feature(33)[0]))
    # val = ['Вставка между ящиками', 'Для пристенных столов', 'Для островных столов']
    # print(json.dumps(ud.get_feature(33)[0]))

    ud.json_feats()
