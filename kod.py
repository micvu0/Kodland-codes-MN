None
meme_dict = {
    "CRINGE": "Coś wyjątkowo dziwnego lub zawstydzającego",
    "LOL": "Częsta reakcja na coś zabawnego",
    "ROFL": "odpowiedź na żart",
    "SHEESH": "lekka dezaprobata",
    "CREEPY": "straszny, złowieszczy",
    "AGGRO": "stać się agresywnym/zły"
}

while True:
    word = input("Wpisz słowo, którego nie rozumiesz (używaj wielkich liter!): ")
    word = word.upper()
    word = word.strip()
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Niestety nie znam takiego słowa")

    print(" ")
