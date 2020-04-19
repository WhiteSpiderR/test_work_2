from Common.Constants.StatusCodesConstants import StatusCodesConstants as SCC
from Common.library.StatusCodesKeywords import StatusCodesKeywords
import pytest


class Test_Headers:
    """
    Класс с тестами для метода status/{codes}
    """
    def setup_class(self):
        self.status_codes_keywords = StatusCodesKeywords()

    @pytest.mark.parametrize("send_code, correct_code",
                             [(200, True), (300, True), (400, True), (500, True)])
    def test_get_request_check_correctly_status_codes(self, send_code, correct_code):
        """
        Проверка корректных кодов состояния
        """
        get_code = self.status_codes_keywords.get_api_request(code=send_code)
        self.status_codes_keywords.check_status_code(send_code=send_code, get_code=get_code, correct_code=correct_code)

    @pytest.mark.parametrize("send_code, correct_code",
                             [(1001, False), (27, False), ('300', False), ('tren', False), (True, False)])
    def test_get_request_check_incorrectly_status_codes(self, send_code, correct_code):
        """
        Проверка некорректных кодов состояния
        """
        get_code = self.status_codes_keywords.get_api_request(code=send_code)
        self.status_codes_keywords.check_status_code(send_code=send_code, get_code=get_code, correct_code=correct_code)

    @pytest.mark.parametrize("send_code, correct_code",
                             [(200, True), (300, True), (400, True), (500, True)])
    def test_post_request_check_correctly_status_codes(self, send_code, correct_code):
        """
        Проверка корректных кодов состояния
        """
        get_code = self.status_codes_keywords.post_api_request(code=send_code)
        self.status_codes_keywords.check_status_code(send_code=send_code, get_code=get_code, correct_code=correct_code)

    @pytest.mark.parametrize("send_code, correct_code",
                             [(1001, False), (27, False), ('300', False), ('tren', False), (True, False)])
    def test_post_request_check_incorrectly_status_codes(self, send_code, correct_code):
        """
        Проверка некорректных кодов состояния
        """
        get_code = self.status_codes_keywords.post_api_request(code=send_code)
        self.status_codes_keywords.check_status_code(send_code=send_code, get_code=get_code, correct_code=correct_code)