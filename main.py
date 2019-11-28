from hiragana import Hiragana

startDescription = "Please input latin text: "

def inputString():
    return raw_input(startDescription)

hiragana = Hiragana(inputString())
print(hiragana.matchText())