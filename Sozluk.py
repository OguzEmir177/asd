meme_sozlugu = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "ROFL": "Bir şakaya karşılık cevap",
    "SHEESH": "Onaylamamak",
    "CREEPY": "Korkunç",
    "AGGRO": "Agresifleşmek/Sinirlenmek"
}

word = input("Anlamadığınız bir kelime yazın: ")

# Kullanıcının girdiği kelimeyi büyük harfle kontrol et
if word.upper() in meme_sozlugu.keys():
    print(meme_sozlugu[word.upper()])
else:
    print("Kelime sözlükte yok, eklenecek")
    # Kelime eşleşmiyorsa ne yapmalıyız? Buraya ekleyebilirsiniz.
