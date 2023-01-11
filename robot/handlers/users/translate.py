from googletrans import Translator
translate = Translator()


def indentify_lang(input):
    return translate.detect(text=input).lang


def to_english(input, lang):
    return translate.translate(text=input, dest='en', src=lang).text
