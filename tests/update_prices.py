import itertools
import os
import re
from pathlib import Path

from common.utils.datetime import date_checker

DOUBLE_END_MATCHING = {
    'FF': 'П',
    'F1': 'П',
    '17': 'П',
    '71': 'П',
    '07': 'П',
    '/1': 'П',
    '01': 'П',
    '/7': 'П',
    'N1': 'П',
    'N7': 'П'
}

SINGLE_END_MATCHING = {
    '4': 'Д',
    'F': 'Г',
    '7': 'П',
}

# TODO английские меняем на русские! это потоп поправить вобще надо в идеае - будут проблемы
ASCII_MATCHING = {
    67: 'С',
    72: 'Н',
    75: 'К',
    77: 'М',
    80: 'П'
}




class UpdatePrices:

    def get_product(self, pattern, product_str, file):
        if pattern in product_str:
            print(f'pattern: {file} --- {product_str}')

    def validate_product_str(self, product_str, file):

        # рекогнайзер криво распознал нули
        product_str = product_str.replace('O', '0')

        pattern = '30-43'
        self.get_product(pattern, product_str, file)

        # в файлах точно нет строк длиной меньше 2
        sliced_str = product_str.rsplit(' ', 1)
        data_exist = date_checker.is_date(sliced_str[1])

        # избавляемся от даты в конце
        if data_exist:
            product_str = sliced_str[0]

        product = {}

        regex = None
        # r'(\d{1,3}\s*(?:\d{3})*(?:[,]\d{2})?)\s*(p)$' - 240
        # reg = r'(\d{1,3}\s?(?:\d{3})*(?:[,.][\dCo]{2})?)\s*(p)'
        # reg = r'(\d{1,3}\s*(?:\d{3})*(?:[,.][\dCo]{2})?)\s?(?:p)?'
        price_regex = r'(\d{1,3}\s?(?:\d{3})*(?:[,.][\dCo]{2})?)\s?(p|СЂ)?$'
        re_pattern = re.compile(price_regex)
        res = re_pattern.findall(product_str)

        if len(res) > 0:
            regex = True
            price = res[0][0].replace(',', '.').replace(' ', '').replace('Co', '0').replace('C0', '0')
            price = float(price)
            if price == 0:
                print(res)
                print(product_str)
            else:
                # print(price)
                tt = 'ad'
            product['price'] = price

        product_data_parts = product_str.split()
        lennn = len(product_data_parts)

        article_parts = product_data_parts[:4]
        prefer_article = article_parts[0]

        prefer_article = prefer_article.upper()

        if prefer_article.startswith('N5'):
            prefer_article = prefer_article.replace('N5', 'NS')
        if prefer_article.startswith('VL'):
            prefer_article = prefer_article.replace('VL', 'NL')
        if prefer_article.startswith('NL'):
            prefer_article = prefer_article.replace('NL', 'NL-')

        if prefer_article.startswith('MM'):
            # TODO робит!
            # parts = prefer_article.rsplit('-', 1)
            # last_part = parts[1]
            #
            # double_iterator = 2
            # while double_iterator <= len(last_part):
            #     match = last_part[-double_iterator:]
            #     if match == '01':
            #         print(product_str)
            #
            #     convert = DOUBLE_END_MATCHING.get(match)
            #     if convert:
            #         print(f'{last_part} matched: {match} - {convert}')
            #         break
            #     else:
            #         print(product_str)
            #
            #     double_iterator += 1

            # TODO сделать проверку еще раз - ВЛОМ
            # у MML можно на концовку засунуть '0': 'П'
            # single_iterator = 2
            # while double_iterator <= len(last_part):
            #     match = last_part[-double_iterator:]
            #     print(match)
            #     convert = DOUBLE_END_MATCHING.get(match)
            #     if convert:
            #         print(f'{last_part} matched: {match} - {convert}')
            #         break
            #     else:
            #         print(product_str)
            #
            #     double_iterator += 1

            # print(f'{prefer_article} - {prefer_article})
            adad = 'ad'
        else:
            gggggggggg= 'ad'
            parts = prefer_article.rsplit('-', 1)

            excluded_list = ['NL-44', 'NL-45', 'NS', 'NL-10', 'NL-11-12-0H', 'NL-11-22-0K', 'NL-13-12-0H',
                             'NL-13-22-0C', 'NL-14-22-1K', 'NL-14-29-1K', 'NL-14-30-1K', 'NL-16-06-0MK']

            # for excluded in excluded_list:
            #     for letter in excluded:
            # TODO засунуть эту штуку в самый конец после прогона по артиклю
            #         converted = ASCII_MATCHING.get(letter)
            #         if converted:
            #             print(excluded)
            #             excluded = excluded.replace(letter, converted)
            #
            #             convert = DOUBLE_END_MATCHING.get(match)
            #             if convert:
            #                 print(f'{last_part} matched: {match} - {convert}')
            #                 break
            #             else:
            #                 print(product_str)


            for excluded in excluded_list:
                if excluded not in prefer_article:
                    last_part = parts[1]

                    if len(last_part) == 3:
                        value_to_convert = last_part[1:]
                        convert = DOUBLE_END_MATCHING.get(value_to_convert)
                        if convert:
                            # TODO доделать обновление артикля
                            print(f'{prefer_article} matched: {last_part} - {convert}')
                            prefer_article = parts[0] + convert
                            print(f'{prefer_article} matched: {last_part} - {convert}')
                            break

        # TODO потом транслитим по аски
        # txt = 'CHKM'
        # print(txt.translate(ASCII_MATCHING))

        # TODO прайс либо пустой либо есть, артикль есть
        # TODO продумать логику обновления базы и добавления в другую ЗАЕБАЛО

        return lennn, regex



    def parse_files(self):
        price_dir_path = Path('price_files')
        price_file_list = os.listdir(price_dir_path)

        max_len = -1
        min_len = 100
        count = 0
        regex_count = 0

        for price_file_name in price_file_list:
            price_file_path = price_dir_path.joinpath(price_file_name)

            with open(price_file_path) as f_in:
                lines = filter(None, (line.rstrip() for line in f_in))

                for line in lines:

                    lennn, regex = self.validate_product_str(line, price_file_path)
                    min_len = min(min_len, lennn)
                    max_len = max(max_len, lennn)
                    # max_len = lennn if lennn > max_len else max_len
                    count += 1
                    if regex:
                        regex_count += 1

        print(min_len, max_len)
        print(count, regex_count)

    # TODO сделать метч артикля
    def match_article(self, article):
        return True

    def match_article_letter(self, letter):
        return True


if __name__ == '__main__':
    update_prices = UpdatePrices()
    # update_prices.validate_line()
    update_prices.parse_files()
