import random
from typing import Union
import string


class CommonKeywords:
    """
    Класс с методами для headers тестов
    """

    def gen_random_string(self, count: Union[int, str]):
        """
        Генерация случайной строки
        Args:
            count: длина строки
        """
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(int(count)))
