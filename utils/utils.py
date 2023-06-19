import random
import string


class StringUtils:
    @staticmethod
    def randon_string():
        letters_and_digits = string.ascii_letters + string.digits
        return "".join(random.sample(letters_and_digits, 10))
