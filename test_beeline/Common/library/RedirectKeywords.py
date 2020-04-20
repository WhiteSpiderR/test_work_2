from Common.Constants.RedirectConstants import RedirectConstants as RC
from Common.Constants.CommonConstants import CommonConstants as CC
from Common.library.CommonKeywords import CommonKeywords
import requests
import allure
from typing import Union
import json

class RedirectKeywords(CommonKeywords):
    """
    Класс с методами для /redirect/{n} тестов
    """

    @allure.step('Отправка get запроса (codes/status)')
    def get_api_request(self, n: Union[int, str]):
        """
        Отправка get запроса.
        Args:
            code: количество перенаправлений
        Return:
            ответ сервера
        """
        headers = {'Content-Type': 'text/plain'}
        response = requests.get(url=f'{CC.BASE_URL}{RC.REDIRECT_URL}/{n}',
                                headers=headers)
        return json.loads(response.text)

    def check_redirect_response(self, get_redirect_response):
        """
        Проверка ответа для запроса /redirect/{n}
        Args:
            get_redirect_response: ответ от сервера при перенаправлении
        """
        assert get_redirect_response['url'] == RC.CONTAIN_RESPONSE_URL, f'Ожидаемый url не совпадает с полученым'

