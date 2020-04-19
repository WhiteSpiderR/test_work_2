from Common.Constants.StatusCodesConstants import StatusCodesConstants as SSC
from Common.Constants.CommonConstants import CommonConstants as CC
from Common.library.CommonKeywords import CommonKeywords
import requests
import allure
from typing import Union


class StatusCodesKeywords(CommonKeywords):
    """
    Класс с методами для /status/{codes} тестов
    """

    @allure.step('Отправка get запроса (codes/status)')
    def get_api_request(self, code: Union[int, str]):
        """
        Отправка get запроса.
        Args:
            code: код состояния для отправки запроса.
        Return:
            код состояния, который вернул сервер.
        """
        headers = {'Content-Type': 'text/plain'}
        response = requests.get(url=f'{CC.BASE_URL}{SSC.STATUS_URL}/{code}',
                                headers=headers)
        return response.status_code

    @allure.step('Проверка отправленного кода состояния с полученым')
    def check_status_code(self, send_code: Union[int, str], get_code: Union[int, str], correct_code: bool = True):
        """
        проверка кода состояния
        Args:
            send_code: код состояния отправленный на сервер
            get_code: полученный код состояния
            correct_code: флаг корректности ожмдаемого кода (должен ли отправленныый код, совпадать с полученным)
        """
        if correct_code:
            assert len(str(send_code)) == SSC().COUNT_CHARS_IN_CODE, f'Отправленный код, не соответсвует условиям'
            assert send_code == get_code, f'Отправленный код сосотяния: {send_code} не соответсвует полученному: {get_code}'
        if not correct_code:
            assert send_code != get_code, f'Отпраленный и полученный коды состояния совпадают. {send_code} == {get_code}'

    @allure.step('Отправка post запроса (codes/status)')
    def post_api_request(self, code: Union[int, str]):
        """
        Отправка post запроса.
        Args:
            code: код состояния для отправки запроса.
        Return:
            код состояния, который вернул сервер.
        """
        headers = {'Content-Type': 'text/plain'}
        data = {}
        response = requests.post(url=f'{CC.BASE_URL}{SSC.STATUS_URL}/{code}',
                                 headers=headers, data=data)
        return response.status_code