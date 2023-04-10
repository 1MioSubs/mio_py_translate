from googletrans import Translator


while True:
    test = input("Ваш текст: ")
    if test == "q":
        break

    t = Translator()
    a = t.translate(test, 'en')
    print("Перевод: " + str(a.text))