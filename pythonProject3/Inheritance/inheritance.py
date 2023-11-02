class Calisan:
    zam_orani = 1.1
    def __init__(self,isim,soyisim,maas):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@sirket.com"
    def bilgileriGoster(self):
        return "Ad : {0} Soyad : {1} Maaş : {2} Email : {3}".format(self.isim,self.soyisim,self.maas,self.email)

class Yazilimci(Calisan):
    def __init__(self,isim,soyisim,maas,dil = "Belirtilmedi"):
        super().__init__(isim,soyisim,maas)
        self.dil = dil
    zam_orani = 1.2
    def bilgileriGoster(self):
        return ("Ad : {0} Soyad : {1} "
                "Maaş : {2} Email : {3} Bildigi Dil : {4}").format(self.isim,self.soyisim,self.maas,self.email,self.dil)
    def diliniSoyle(self):
        return f"Bildiği dil : {self.dil}"

class Yonetici(Calisan):
    def __init__(self,isim,soyisim,maas, calisanlar = None):
        super().__init__(isim,soyisim,maas)
        if calisanlar == None:
            self.calisanlar = []
        else:
            self.calisanlar = calisanlar

    def calisanEkle(self,calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)
    def calisanSil(self,calisan):
        if calisan in self.calisanlar:
            self.calisanlar.remove(calisan)
    def calisanlarıGoster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileriGoster())
    def bilgileriGoster(self):
        return f"İsim : {self.isim} Soyisim : {self.soyisim} Email : {self.email}"


calisan1 = Calisan("Mehmet","Kaya",10000)
yazılımcı1 = Yazilimci("Ayşe","Çiçek",17000)
yazılımcı2 = Yazilimci("Hasan","Sevinç",25000,"Python")
yonetici1 = Yonetici("Emre","Dağ",30000,[yazılımcı1,calisan1])
yonetici2 = Yonetici("İbrahim","Dağdelen",35000)
print(calisan1.bilgileriGoster())
print(yazılımcı1.bilgileriGoster())
print(yazılımcı2.bilgileriGoster())
print(yonetici1.bilgileriGoster())
print(yonetici2.bilgileriGoster())
yonetici1.calisanlarıGoster()
yonetici1.calisanSil(calisan1)
yonetici1.calisanlarıGoster()
