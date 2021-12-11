class yemek_kitabi:
    def tarif_olustur(self) :
        tarifi = input("tarif ismi : ")
        tarif.append(tarifi)
        while True :  
            tarif_asama = input("tarif asama(asamalar bittiyse -1 giriniz) : ")
            if tarif_asama == "-1" :
                tarifler_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarif_asama)
            

    def sirala(self) :
        sayi = len(tarifler_listesi)
        print("Kayitli Tarifler:")    
        for adim in tarif :
                print(adim)



        
def ana_sayfa() :
    while True :
        print("\nYeni tarif eklemek icin : 1\nVar olan tarifleri listelemek icin : 2\n Cikis yapmak icin : 3 ")
        secim = input("Islem no gir : ")
        islem = yemek_kitabi()
        if secim == "1" :
            islem.tarif_olustur()
        elif secim == "2" :
            islem.sirala()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatali islem yaptiniz. Tekrar deneyiniz.")



tarifler_listesi = []
tarif = []

ana_sayfa()