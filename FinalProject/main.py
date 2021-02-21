# yemek tarifi uygulaması
class Yemekler():
    anaMiktar = 0
    pismeSuresi = 0.0
    yemekAdi =" "
    def __init__(self, yemekAdi, anaMiktar, pismeSuresi):
        self.yemekAdi=yemekAdi
        self.anaMiktar = anaMiktar
        self.pismeSuresi = pismeSuresi

    def goster(self, yemekAdi):
        self.yemekAdi=yemekAdi
        print("{} yemeğini yapmaya başlayın".format(self.yemekAdi))


    def karistir(self, yemekAdi):
        self.yemekAdi=yemekAdi
        print("{} yemeğinizi karıştırın".format(self.yemekAdi))

    def tuzEkle(self, yemekAdi):
        self.yemekAdi = yemekAdi
        print("{} yemeğinize damak zevkinize göre tuz ekleyin".format(self.yemekAdi))

    def pisir(self, yemekAdi, pismeSuresi):
        self.yemekAdi = yemekAdi
        self.pismeSuresi=pismeSuresi
        print("Yemeğinizi pişirin. Süre: {} dk".format(self.pismeSuresi))

    def tadinaBak(self, yemekAdi):
        self.yemekAdi = yemekAdi
        print("{} yemeğinizin tadını ve tuzunu kontrol edin".format(self.yemekAdi))


class MercimekCorbasiYap(Yemekler):

    def __init__(self, yemekAdi, zeytinYagiKasikSayisi, kuruSogan, unBardakSayisi, havuc, patates, sicakSuMikatri):
        self.yemekAdi=yemekAdi
        self.zeytinYagiKasikSayisi=zeytinYagiKasikSayisi
        self.kuruSogan=kuruSogan
        self.unBardakSayisi=unBardakSayisi
        self.havuc=havuc
        self.patates=patates
        self.sicakSuMikatri=sicakSuMikatri

    def kavur(self):
        print("Yağda; soğanı, unu, havucu ve patatesi kavurun")

    def ekle(self):
        print("Tuzu, mercimeği ve suyu ekleyin")


class EvKoftesiYap(Yemekler):
    def __init__(self, yemekAdi, kiymaMiktariGr, sogan, maydanoz, bayatEkmek, zeytinYagiKasikSayisi):
        self.yemekAdi=yemekAdi
        self.kiymaMiktariGr=kiymaMiktariGr
        self.sogan=sogan
        self.maydanoz=maydanoz
        self.bayatEkmek=bayatEkmek
        self.zeytinYagiKasikSayisi=zeytinYagiKasikSayisi

    def rendele(self):
        print("Soğanı rendeleyin")

    def ekle(self):
        print("Tüm malzemeleri ekleyin")


class PilavYap(Yemekler):
    def __init__(self, yemekAdi, pirincSuBardagiMiktari, sicakSu, tereyagiYemekKasigiMiktari, pirincIslamakIcinSu):
        self.yemekAdi=yemekAdi
        self.pirincSuBardagiMiktari=pirincSuBardagiMiktari
        self.sicakSu=sicakSu
        self.tereyagiYemekKasigiMiktari=tereyagiYemekKasigiMiktari
        self.pirincIslamakIcinSu=pirincIslamakIcinSu

    def pirinciYika(self):
        print("pirinci yıkayın")

    def kavur(self):
        print("Tereyağında pirinci kavurun")

    def ekle(self):
        print("Sıcak suyu ekleyin")


print()

mercimekCorbasi = MercimekCorbasiYap("Mercimek Çorbası", 1, 1, 1, 1, 1, 6)
mercimekCorbasi.goster(mercimekCorbasi.yemekAdi)
mercimekCorbasi.kavur()
mercimekCorbasi.ekle()
mercimekCorbasi.tuzEkle(mercimekCorbasi.yemekAdi)
mercimekCorbasi.karistir(mercimekCorbasi.yemekAdi)
mercimekCorbasi.pisir(mercimekCorbasi.yemekAdi,40)
mercimekCorbasi.tadinaBak(mercimekCorbasi.yemekAdi)

print()

evKoftesi = EvKoftesiYap("Ev Köftesi", 500, 1, 8, 1, 3)
evKoftesi.goster(evKoftesi.yemekAdi)
evKoftesi.rendele()
evKoftesi.ekle()
evKoftesi.tuzEkle(evKoftesi.yemekAdi)
evKoftesi.karistir(evKoftesi.yemekAdi)
evKoftesi.pisir(evKoftesi.yemekAdi, 10)
evKoftesi.tadinaBak(evKoftesi.yemekAdi)

print()

pilav = PilavYap("Pilav", 2, 2.5, 3, 3)
pilav.goster(pilav.yemekAdi)
pilav.pirinciYika()
pilav.kavur()
pilav.ekle()
pilav.tuzEkle(pilav.yemekAdi)
pilav.karistir(pilav.yemekAdi)
pilav.pisir(pilav.yemekAdi, 15)
pilav.tadinaBak(pilav.yemekAdi)
