#öğretim yönetim sistemi

adSoyad = [" ", " ", " ", " ", " "]

print("ÖĞRENCİLERİN ADINI VE SOYADINI GİRİNİZ\n")
for i in range(len(adSoyad)):
    adSoyad[i] = input("{}. öğrencinin adını ve soyadını girin : ".format(i+1))

notlar = ["vize", "final", "ödev"] # 3 adet notumuz olacak
ortalamaList = [0.0, 0.0, 0.0, 0.0, 0.0]

print()

notListesi=[
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
            ]#vize final ödev, ortalama

#her öğrenci için ayrı ayrı; vize, final, ödev notunu alıyoruz ve notListesi adlı listemizin içine aldığımız değerleri yerleştiryoruz
#notListesi'ndeki notListesi[0][3] ve notListesi[0][3] atlamamızın sebebi (satır 27) bu indexe ortalama koyacağımız için
for i in range(len(notListesi)):
    print("{} adlı öğrenci için ".format(adSoyad[i]))
    for j in range(4):
        if j == 3:
            continue
        else:
            notListesi[i][j] = int(input("{} notunu girin".format(notlar[j])))
    print()

#öğrencilerin not ortalamsını hesaplıyoruz
for i in range(len(notListesi)):
    toplam = 0
    for j in range(3):
        toplam = notListesi[i][j] + toplam

    ortalama = (toplam/3)
    notListesi[i][3] = ortalama
    ortalamaList[i] = ortalama


denemeDict ={}
denemeDict =dict(zip(adSoyad, notListesi))
print("Öğrenci Bilgileri (Ad soyad, vize, final, ödev ortalama")
print(denemeDict)

ortalamaDict = {}
ortalamaDict = dict(zip(adSoyad, ortalamaList))

ortalamaList = sorted(ortalamaList)
ortalamaList = ortalamaList[::-1]
maxOrtalama = max(ortalamaList)
print("En yüksek ortalamadan en düşük ortalamaya : ")
print(ortalamaList)

print()

for key, value in ortalamaDict.items():
    if maxOrtalama == value:
        print("Tebrikler : {}".format(key))