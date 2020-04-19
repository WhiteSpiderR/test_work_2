from Common.Constants.HeadersConstants import HeadersConstants as HC
from Common.Constants.CommonConstants import CommonConstants as CC
from Common.library.CommonKeywords import CommonKeywords
import requests
import json
import allure


class HeadersKeywords(CommonKeywords):
    """
    Класс с методами для headers тестов
    """

    @allure.step('Получение случайных заголовков')
    def get_random_headers(self, **kwargs):
        """
        Получить случайные заголовки
        Args:
            gen_accept: флаг генерации заголовка 'Accept'
            gen_accept_encoding: флаг генерации заголовка 'Accept-Encoding'
            gen_content_type: флаг генерации заголовка 'Content-Type'
        Return:
            random_headers: заголовки со случайными значениями.
        """
        random_headers = {}
        random_headers['Accept'] = self.gen_random_string(8) if kwargs.get('gen_accept') else HC.DEFAULT_HEADERS_ACCEPT
        random_headers['Accept-Encoding'] = self.gen_random_string(8) if kwargs.get('gen_accept_encoding') \
            else HC.DEFAULT_HEADERS_ACCEPT_ENCODING
        random_headers['Content-Type'] = self.gen_random_string(8) if kwargs.get('gen_content_type') \
            else HC.DEFAULT_HEADERS_CONTENT_TYPE
        return random_headers

    @allure.step('Отправка get запроса.')
    def get_api_request(self, headers: dict):
        """
        Отправка get запроса.
        Args:
            headers: загаловки для запроса.
        Return:

        """
        response = requests.get(url=f'{CC.BASE_URL}{HC.HEADERS_URL}',
                                headers=headers)
        return json.loads(response.text)['headers']

    @allure.step('Проверка заголовков.')
    def check_headers(self, send_headers: dict, get_headers: dict):
        """
        Проверка отправленных загаловков с полученными
        Args:
            send_headers: отправленные заголовки
            get_headers: полученные заголовки
        Return:
        """
        check_headers = {}
        for key, value in get_headers.items():
            if key in send_headers:
                if send_headers[key] == get_headers[key]:
                    check_headers[key] = value
        assert sorted(check_headers) == sorted(send_headers), f'Отправленные заголовки не соответсвуют полученным'

