from const import MORSE_CODE_DICT


def reverse_morse_dict_decorator(func):
    """
    Decorator that adds the reversed Morse code dictionary as an argument to the function.
    """
    reverse_morse_dict = {value: key for key, value in MORSE_CODE_DICT.items()}

    def wrapper(*args, **kwargs):
        return func(*args, reverse_morse_dict=reverse_morse_dict, **kwargs)

    return wrapper


class Morse:
    """
    Class representing Morse code.
    """

    def __int__(self, text: str, code: str) -> None:
        """
        Initializes the Morse object.

        :param text: Text to encode.
        :param code: Morse code to decode.
        """
        self.text = text
        self.code = code

    @staticmethod
    def encode_morse(text: str) -> str:
        """
        Encodes text into Morse code.

        :param text: Text to encode.
        :return: Morse code.
        """
        morse_code = ''
        for char in text:
            morse_code += MORSE_CODE_DICT.get(char.upper(), ' ') + ' '
        return morse_code.strip()

    @staticmethod
    @reverse_morse_dict_decorator
    def decode_morse(code: str, reverse_morse_dict: dict) -> str:
        """
        Decodes Morse code into text.

        :param code: Morse code to decode.
        :param reverse_morse_dict: Reversed Morse code dictionary.
        :return: Decoded text.
        """
        morse_words = code.split(' ')
        text = ''
        for word in morse_words:
            text += reverse_morse_dict.get(word, ' ')
        return text


morse_object = Morse()
morse_encode = morse_object.encode_morse('Example Text')
print(morse_encode)
morse_decode = morse_object.decode_morse(morse_encode)
print(morse_decode)
