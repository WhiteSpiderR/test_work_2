import pytest
from Common.library.HeadersKeywords import HeadersKeywords

class Test_Headers:
    """
    Класс с тестами для метода headers
    """
    def setup_class(self):
        self.headers_keywords = HeadersKeywords()

    @pytest.mark.parametrize("gen_accept, gen_accept_encoding, gen_content_type", [(True, True, True),
                                                                                   (True, True, False),
                                                                                   (True, False, False),
                                                                                   (False, False, False)])
    def test_headers_get(self, gen_accept, gen_accept_encoding, gen_content_type):
        """
        test headers
        """
        send_headers = self.headers_keywords.get_random_headers(
            gen_accept=gen_accept, gen_accept_encoding=gen_accept_encoding, gen_content_type=gen_content_type)
        get_headers = self.headers_keywords.get_api_request(headers=send_headers)
        self.headers_keywords.check_headers(send_headers=send_headers, get_headers=get_headers)
