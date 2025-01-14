from googletrans import Translator



def translate(text,language):
    translator = Translator()
    result= translator.translate(text, dest=language)
    return result.text