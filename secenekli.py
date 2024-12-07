hak = 2  # Kullanıcı Yanlış Giriş Hak Değişkeni Ekliyoruz.
print("Uygulamamıza Hoş Geldiniz Lütfen Bilgilerinizi Giriniz: ")
ad = str(input("Adınızı Giriniz: "))
soyad = str(input("Soyadınızı Giriniz: "))
Username = str(input("Kullanıcı Adı Oluşturunuz: ")).lower()
sifre = int(input("Sayıdan Şifre Oluşturunuz: "))
print("Başarıyla Oluşturuldu", Username, "")
# Giriş yap
print("\nGiriş Yapmak İçin Bilgilerinizi Giriniz: ")
girissorgu = False  # Giriş durumunu kontrol etmek için bir değişken ekliyoruz.
while hak > 0:
    kullanici = str(input("Kullanıcı Adınızı Giriniz: ")).lower()
    sifre2 = int(input("Şifrenizi Giriniz: "))
    if kullanici == Username and sifre2 == sifre:
        print("Hoş Geldin", Username)
        girissorgu = True  #
        break
    else:
        hak -= 1
        if hak > 0:
            print("Kullanıcı adı veya şifre hatalı. Kalan hakkınız:", hak)
        else:
            print("Hesabınız askıya alındı. Lütfen admin ile iletişime geçiniz.")
            break
#Seçenekler
if girissorgu:
    while True:
        print("\n1: Şifre Değişme \n2: Kullanıcı Verilerini Gör")
        secenek = int(input("Seçeneklerden Birini Seçiniz: "))
        if secenek == 2:
            print("Adınız:", ad)
            print("Soyadınız:", soyad)
            print("Kullanıcı Adınız:", Username)
            break
        elif secenek == 1:
            while True:
                degistirme = input("\nŞifre Değiştirmek İster misiniz? (Evet/Hayır): ").lower()
                if degistirme == 'evet':
                    yenisifre = input("Yeni Şifrenizi Giriniz: ")
                    sifre = yenisifre  # Yeni şifreyi atıyoruz.
                    print("Şifre başarıyla değiştirildi.")
                    break
                elif degistirme == 'hayır':
                    print("Hoşgeldiniz!")
                    break
                else:
                    print("\nLütfen Geçerli Bir Cevap Giriniz.")
                    continue           
        else:
            print("Geçersiz seçenek. Lütfen geçerli bir seçenek giriniz.")
            break
