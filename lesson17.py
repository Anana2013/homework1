age = int(input("შეიყვანეთ თქვენი ასაკი: "))

if age <= 12:
    print("ბავშვი")
elif age <= 19:
    print("თინეიჯერი")
elif age <= 59:
    print("ზრდასრული")
else:
    print("პენსიონერი")


number = int(input("შეიყვანეთ რიცხვი: "))

if number < 0:
    print("უარყოფითი")
elif number == 0:
    print("ნული")
elif number < 100:
    print("პატარა რიცხვი")
else:
    print("დიდი რიცხვი")


score = int(input("შეიყვანეთ თქვენი ქულა (0–100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


day_number = int(input("შეიყვანეთ კვირის დღე რიცხვი (1–7): "))

if day_number == 1:
    print("ორშაბათი")
elif day_number == 2:
    print("სამშაბათი")
elif day_number == 3:
    print("ოთხშაბათი")
elif day_number == 4:
    print("ხუთშაბათი")
elif day_number == 5:
    print("პარასკევი")
elif day_number == 6:
    print("შაბათი")
elif day_number == 7:
    print("კვირა")
else:
    print("არასწორი რიცხვი")


temperature = float(input("შეიყვანეთ ტემპერატურა ცელსიუსში: "))

if temperature < 0:
    print("ძალიან ცივა")
elif temperature <= 15:
    print("გრილია")
elif temperature <= 30:
    print("თბილია")
elif temperature <= 40:
    print("ცხელა")
else:
    print("უაღრესად ცხელა")