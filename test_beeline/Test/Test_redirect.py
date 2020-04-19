from Common.library.RedirectKeywords import RedirectKeywords
import pytest

class TestRedirect:
    """
    Класс с тестами дял проверки redirect/{n} метода
    """

    def setup_class(self):
        self.redirect_keywords = RedirectKeywords()

    @pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
    def test_check_get_redirect_request(self, n):
        response = self.redirect_keywords.get_api_request(n=n)
        self.redirect_keywords.check_redirect_response(get_redirect_response=response)
