from pyaspeller import YandexSpeller


def spell(message):
    speller = YandexSpeller()
    fixed = speller.spelled(message)
    return fixed
