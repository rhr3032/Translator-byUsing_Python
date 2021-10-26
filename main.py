from translate
import Translator

options = Translator(from_lang = "english", to_lang = "bangla")
inputString = "I love to write code."

translate = options.translate(inputString)
print(translate)