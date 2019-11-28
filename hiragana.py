from data import data
from romaji import Romaji
from ast import literal_eval
import copy

class Hiragana:
    dictionary = data

    def __init__(self, latinText):
        self.arrLatinText = latinText.lower()

    def matchText(self):
        romaji = Romaji(self.arrLatinText)
        arrRomaji = romaji.mapWord(romaji.arrLatinText)
        # return arrRomaji
        hiraganaText = ""
        for text in arrRomaji:
            hiraganaText += self.matchCharacter(data, list(text))
        return hiraganaText

    def matchCharacter(self, dictionary, arrText):
        newArrText = copy.copy(arrText)
        for t in arrText:
            value =  dictionary.get(t.upper()) if t == 'n' and len(arrText) == 1 else dictionary.get(t)

            if not value:
                return "Input Incorrect Latin Text."

            if type(value) is str:
                return value
            
            if type(value) is dict:
                newArrText.pop(0)
                return self.matchCharacter(value, newArrText)
