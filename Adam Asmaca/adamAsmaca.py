import random

# Kategorilere ait kelimeler
hayvan = ["aslan", "kedi", "köpek", "ayı", "timsah", "yarasa", "eşşek", "kurbağa", "kurt", "kaplan", "koala", "yılan", "zürafa", "kaplumbağa", "keçi", "geyik", "goril", "gergedan", "mirket"]
futbolTerim = ["antrenör", "averaj", "röveşata", "trivela", "ofsayt", "forma", "diziliş", "markaj", "panenka", "transfer", "taraftar"]
meyve = ["ananas", "armut", "ayva", "böğürtlen", "çilek", "çağla", "elma", "frambuaz", "greyfurt", "karpuz", "kavun", "mandalina", "portakal"]
sebze = ["domates", "lahana", "patlıcan", "havuç", "bezelye", "brokoli", "enginar", "fasulye", "pancar", "pırasa"]
sehirler = ["istanbul", "viyana", "paris", "stokholm", "amsterdam", "milano", "budapeşte", "lizbon", "barselona", "kopenhag", "hamburg", "helsinki", "varşova"]

kelimeler = [hayvan, futbolTerim, meyve, sebze, sehirler]

adam = [
    '''
      +-----+
      |     |
      o     |
     /|\    |
     / \    |
           ---''',
    '''
      +-----+
      |     |
      o     |
     /|\    |
     /      |
           ---''',
    '''
      +-----+
      |     |
      o     |
     /|\    |
            |
           ---''',
    '''
      +-----+
      |     |
      o     |
     /|     |
            |
           ---''',
    '''
      +-----+
      |     |
      o     |
      |     |
            |
           ---''',
    '''
      +-----+
      |     |
      o     |
            |
            |
           ---''',
    '''
      +-----+
      |     |
            |
            |
            |
           ---'''
]

def kategori_sec():
    print("Kategori seçin:")
    print("1. Hayvan")
    print("2. Futbol Terimi")
    print("3. Meyve")
    print("4. Sebze")
    print("5. Şehirler")

    secim = input("Seçiminizi yapın (1-5): ")
    if secim in ["1", "2", "3", "4", "5"]:
        return int(secim) - 1
    else:
        print("Geçersiz seçim. Tekrar deneyin.")
        return kategori_sec()

def adam_asmaca(kelime):
    dogruHarf = []
    yanlisHarf = []
    hak = len(adam) - 1
    while hak > 0:
        out = ""
        for h in kelime:
            if h in dogruHarf:
                out += h
            else:
                out += "_"
        if out == kelime:
            break
        print("Kelime:", out)
        print(adam[len(adam) - 1 - hak])
        girHarf = input("Bir harf girin: ").lower()
        if girHarf in dogruHarf or girHarf in yanlisHarf:
            print(girHarf, "zaten girildi.")
        elif girHarf in kelime:
            print("Doğru harf!")
            dogruHarf.append(girHarf)
        else:
            print("Yanlış harf!")
            hak -= 1
            yanlisHarf.append(girHarf)
    if hak > 0:
        print("Tebrikler kazandınız! Kelimeniz:", kelime)
    else:
        print("Maalesef kaybettiniz. Kelimeniz:", kelime)

def main():
    kategori_index = kategori_sec()
    kelime = random.choice(kelimeler[kategori_index])
    adam_asmaca(kelime)

main()
