


# Blackjack

Blackjack (21), hem şansa hem de matematiksel stratejiye dayanan, kasaya (dealer) karşı oynanan bir kart oyunudur.
 Kaggle egzersizindeki kod mantığını oturtmak için oyunun işleyişini bilmek çok önemlidir.İşte en basit haliyle kurallar ve kod yazarken kuracağın mantık:
 
 ## 🃏 1. Blackjack Nedir ve Nasıl Oynanır?
 Amaç: Elindeki kartların sayısal toplamı ile 21'i geçmeden kasanın elinden daha yüksek bir sayıya ulaşmak.
 Kart Değerleri:
 2'den 10'u kadar olan kartlar kendi değerindedir.
 Vale (J), Kız (Q) ve Papaz (K) 10 puan değerindedir.
 As (Ace) ise duruma göre 1 ya da 11 puan yerine geçebilir (Esnek karttır, seni yakmayacak değeri alır).
 Oyunun Akışı: Kasa ve oyuncuya ikişer kart dağıtılır. Kasanın kartlarından biri açık (görünür), diğeri kapalıdır. Oyuncu sırayla kart isteyebilir (Hit) veya elindeki sayıya güvenip durabilir (Stay). Eğer kart çekip 21'i geçerseniz anında kaybedersiniz (Bust).
 
 ## 💻 2. Kod Yazarken Kuracağın Mantık (İpuçları)Kaggle'daki should_hit fonksiyonunda Python'a bir yapay zeka stratejisi yazıyorsun. Fonksiyon senden True (kart çek) veya False (dur) döndürmeni bekliyor. Karar verirken şu 3 veriyi analiz etmelisin:
 
 ### A. Kendi Elinin Toplamı (player_total)
 11 ve altı: Kesinlikle kart çekmelisin (True). Çünkü hangi kart gelirse gelsin 21'i geçip yanma (bust) ihtimalin sıfırdır.
 17 ve üstü: Durmalısın (False). Çünkü yeni bir kart çekersen büyük ihtimalle 21'i geçer ve yanarsın.
 
 ### B. Kasanın Açık Kartı (dealer_total
 Kasa, kurallar gereği eli en az 17 olana kadar kart çekmek zorundadır.
 Eğer kasanın açık kartı 2, 3, 4, 5 veya 6 gibi zayıf bir kartsa, kasanın 21'i geçip yanma ihtimali çok yüksektir. Bu durumda senin elin 12-16 arasında bile olsa risk almayıp durman (False) mantıklıdır. Kasa kart çekip kendi kendini yaksın diye beklersin.Kasanın açık kartı 7, 8, 9, 10 veya As gibi güçlüyse, senin daha agresif oynaman ve elini yükseltmek için kart istemen (True) gerekir.

 ### C. As (Ace) Kartlarının Durumu (player_high_aces)
 Eğer elinde 11 puan değerinde bir As varsa (player_high_aces > 0), elin çok güvendedir.Çünkü sonraki kartta 21'i geçsen bile, o As otomatik olarak 1 puana düşer ve elin yanmaz. Bu yüzden elinde yüksek As varken daha cesurca kart isteyebilirsin.



 ## Kart Puanlamaları:

1. Sayı Kartları (2 - 10):Bu kartlar üzerinde yazan rakam kadar puan verirler.

   2 = 2 puan

   5 = 5 puan

   10 = 10 puan

2. Resimli Kartlar (J, Q, K):
Vale, Kız ve Papaz'ın hepsi aynı değerdedir.

   J (Vale) = 10 puan

   Q (Kız) = 10 puan

   K (Papaz) = 10 puan

3. As (A) - En Özel Kart:
As kartı, elinin durumuna göre iki farklı değer alabilir. Oyun bunu senin lehine otomatik ayarlar:

   11 Puan: Eğer 11 olarak sayıldığında toplamın 21'i geçmiyorsa 11 sayılır (Buna High Ace 
denir).

   1 Puan: Eğer 11 sayıldığında 21'i geçiyorsan, yanmaman için değeri 1'e düşer (Buna Low Ace denir).
