meme_sozlugu = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "ROFL bir şakaya karşılıktır, LOL gibidir",
            "SHEESH":  "Onaylamamak",
            "CREEPY":  "Korkunç"
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in meme_sozlugu.keys():
    print(meme_sozlugu[word])
else:
    print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
