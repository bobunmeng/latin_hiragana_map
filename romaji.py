import copy

class Romaji:
    latinVowels = ('a', 'e', 'i', 'o', 'u')

    def __init__(self, latinText):
        self.arrLatinText = list(latinText)

    def mapWord(self, arrText):
        word = ""
        newArr = copy.copy(arrText)
        for l in arrText:
            word += l
            newArr.pop(0)
            if l in self.latinVowels:
                break
            if len(newArr):
                nextL = newArr[0]
                if nextL not in self.latinVowels:
                    break
        if not(newArr):
            return [word]
        return [word] + self.mapWord(newArr)
        
