

# class metotları , instance metotları , static metotlar

class calisan5:
    zam_orani = 1.1                                 # / class veriable
    kisi_sayisi=0                                   # / class veriable
    def __init__(self,isim,soyisim,meslek):
        self.isim=isim                              # / instance veriable
        self.soyisim=soyisim                        # / instance veriable
        self.meslek=meslek                          # / instance veriable
        calisan5.kisi_sayisi += 1
    def bilgileri_soyle(self):                      # / parantez içine self aldığı için instance metot denir.
        return ("isim :  {} , soyisim : {} , meslek : {}".format(self.isim,self.soyisim,self.meslek))
    
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi

calisan51=calisan5("İdris","Topçu","Öğretmen")
calisan52=calisan5("kemal","topal","mühendis")
calisan53=calisan5("ali","ihsan","memur")

print(calisan51.bilgileri_soyle())              # / isim :  İdris , soyisim : Topçu , meslek : Öğretmen
print(calisan52.bilgileri_soyle())              # / isim :  kemal , soyisim : topal , meslek : mühendis
print(calisan53.bilgileri_soyle())              # / isim :  ali , soyisim : ihsan , meslek : memur
# print(calisan5.bilgileri_soyle())             # / TypeError: bilgileri_soyle() missing 1 required positional argument: 'self' ( instance metot olduğu için hata verdi)


print(calisan5.kisi_sayisini_soyle())           # / 3 

# bir veri tabanına veri kaydetmemiz gerekiyor ancak ihtiyacımız olan veriler bize istediğimiz tarzda gelmeyebilir.
# istediğimiz formata çeirebilmek için class metot kullanabiliriz.
# şablon dosyamızda isim,soyisim,meslek ancak başka bir yerden daha farklı formatlarda dosya gelebilir.
# aşağıdaki senaryoda isim-soyisim-meslek verilerinin string olarak geldiğini varsayarsak 


class calisan6:
    zam_orani = 1.1                                 # / class veriable
    kisi_sayisi=0                                   # / class veriable
    def __init__(self,isim,soyisim,meslek):
        self.isim=isim                              # / instance veriable
        self.soyisim=soyisim                        # / instance veriable
        self.meslek=meslek                          # / instance veriable
        calisan6.kisi_sayisi += 1
    def bilgileri_soyle(self):                      # / parantez içine self aldığı için instance metot denir.
        return ("isim :  {} , soyisim : {} , meslek : {}".format(self.isim,self.soyisim,self.meslek))
    
    @classmethod
    def kisi_sayisini_soyle(cls):
        return cls.kisi_sayisi
    
    @classmethod                                    # / yukarıdaki senaryodaki verileri almak için bir class metot yazdık
    def stringe_gore_olustur(cls,str_):             # / çağırşım yapacağı bir isim verdik. (cls anahta kelimesi yukarıdaki self ,  str_ anahtar kelimesi ise şablon dışı dosyalarımıza verilen takma isim)
        isim,soyisim,meslek = str_.split("-")       # / "-" işaretinden bölerek isim,soyisim,meslek değişkenlerine atama yaptık,
        return cls(isim,soyisim,meslek)             # / en nihayetinde metotun ne yapacağını tanıttık

calisan61 = "derya-yanık-garson"                  # bu değişik formatta gelen verileri 61 numaralı çalışan olarak kaydedeceğiz 
calisan62 = "engin-düz-piyanist"                  # bu değişik formatta gelen verileri 62 numaralı çalışan olarak kaydedeceğiz 

print(calisan6.kisi_sayisini_soyle())

calisan61 = calisan6.stringe_gore_olustur("derya-yanık-garson")
calisan62 = calisan6.stringe_gore_olustur("engin-düz-piyanist")


print(calisan61.bilgileri_soyle())
print(calisan62.bilgileri_soyle ())
print(calisan6.kisi_sayisini_soyle())



# static method

# içerisine herhangi bir parametre almadan da çalışabilir. class dan da içindekilerden de bağımsız olarak tanımlanabilme özelliğine sahiptir.

from datetime import date

class calisan_yasli:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas
        
    @staticmethod                                                           # / bir statik metot oluşturduk.
    def dogum_yili_hesapla(calisan_yasli):                                  # / parantez içinde class ismi olması gerekiyor.  
        return date.today().year - calisan_yasli.yas                        # / date modülünü import ettik . return ile statik metot a ne yapacağını söyledik.


calisan71 = calisan_yasli("Kemal",30)
calisan72 = calisan_yasli("Nuh",43)
calisan73 = calisan_yasli("merve",29)

print(calisan_yasli.dogum_yili_hesapla(calisan71))

print("71 numaralı çalışanın doğum yılı : {} ".format(calisan_yasli.dogum_yili_hesapla(calisan71)))
print("72 numaralı çalışanın doğum yılı : {} ".format(calisan_yasli.dogum_yili_hesapla(calisan72)))
print("73 numaralı çalışanın doğum yılı : {} ".format(calisan_yasli.dogum_yili_hesapla(calisan73)))