


# IF/ ELSE

#Girilen hava sıcaklığına göre mesaj veren kod.

def evaluate_temp(temp):
    if temp>38:
        message="Fever!"
    else:
        message="Normal temperature."
    return message

print(evaluate_temp(27))


#ELIF

#Girilen hava sıcaklığına göre mesaj veren kod.

def evaluate_temp(temp):
    if  temp>38:
        message="Fever!"
    elif temp>35:
        message="Normal temperature."
    else:
        message="Low temperature."
    return message

print(evaluate_temp(39))


#Kişilerin kazançlarına göre vergi borçlarını hesaplayan kod.

def get_taxes(earnings):
    if earnings<12000:
        tax_owed=.25*earnings
    else:
        tax_owed=.30*earnings
    return tax_owed

print(get_taxes(15000))    



#QUESTİON_1:Girilen nota göre harf notu atayan kod.

def get_grade(score):
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    return grade

print(get_grade(80))




#QUESTION_3:Girilen galon sayısına gör 1000 galon başına ödenecek tutarın belirlenip toplam tutarın hesaplanması.

def get_water_bill(num_gallons):
    bill=1000
    if num_gallons>=30001:
        bill=num_gallons/bill*10
    elif num_gallons>=22001:
        bill=num_gallons/bill*7
    elif num_gallons>=8001:
        bill=num_gallons/bill*6
    else:
        bill=num_gallons/bill*5
    return bill

print(get_water_bill(25000))



#QUESTION_4:Aylık telefon faturası hesaplama.

def get_phone_bill(gb):
    if gb<=15:
        bill=100
    else:
        bill=100+(gb-15)*1000*0.10
    return bill

print(get_phone_bill(15.1))



#LIST

#Lenght:We can count the number of entries in any list with len()

#Indexing:We can refer to any item in the list according to its position in the list (first, second, third, etc)

#Slicing:You can also pull a segment of a list (for instance, the first three entries or the last two entries). 

#Removing items:.remove()

#Adding items:.append()


flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers))
print(flowers)


flowers_list=["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)
print(len(flowers_list))

print("First entry:",flowers_list[0])
print("Second entry:",flowers_list[1])
print("Last entry:",flowers_list[9])

print("First three entries:",flowers_list[:3])
print("Last two entries:",flowers_list[-2:])

flowers_list.remove("globe thistle")
print(flowers_list)

flowers_list.append("snapdragon")
print(flowers_list)


#MİN()/ MAX()/ SUM()


#split(): str yapısındaki tek parça bütünü parçalar ve çoklu bir veri yapısı oluşturur.

flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(flowers.split(","))
print(type(flowers.split(",")))



#QUESTION_1:

menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']
menu.remove('bean soup')
menu.append("roasted beet salad")

print(menu)



#QUESTION_2:

num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

avg_first_seven= sum(num_customers[:7])/7
avg_last_seven= sum(num_customers[-7:])/7
max_month= max(num_customers)
min_month= min(num_customers)

print(min_month)



#QUESTION_3:

alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
letters = alphabet.split(".")
formatted_address = address.split(",")



#QUESTION_4:Bir krsa verilen puanın yüzde kaçının 4 ve üzeri olduğunu hesaplar.

def percentage_liked(ratings):
    list_liked=[i>=4 for i in ratings]
    percentage_liked= sum(list_liked)/len(ratings)
    return percentage_liked



#QUESTION_5: Büyüme oranı hesaplama.

def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-1-yrs_ago]) / num_users[len(num_users)-1-yrs_ago]
    return growth

num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
