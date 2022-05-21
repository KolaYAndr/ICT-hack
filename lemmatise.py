from pymystem3 import Mystem


def lemmatise(message):
    mystem = Mystem()
    message = mystem.lemmatize(message)
    message = post_clear(message)
    return message


def post_clear(message):
    i = 0
    while i < len(message):
        if message[i] == " " or message[i] == "\n" or message[i] == ' ' or message[i] == ' \n':
            message.pop(i)
        i += 1
    return message
