from dateutil.parser import parse


def is_date(string):
    """

    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        # не создастся новая строка если нечего менять
        prepared_str = string.replace('(', '').replace(')', '').replace(',', '.').replace('-', '').replace(']', '')

        if prepared_str.isdigit():
            r = ''
            # print(f'{string} - {prepared_str}')
            return 'D'

        return parse(prepared_str, dayfirst=True, fuzzy=False)

    except ValueError:
        return False
