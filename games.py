import random

ism = input("Ismingizni kiriting: ")
hisob1 = []
hisob2 = []
print(f"ⓢ ⓐ ⓛ Ⓞ ⓜ  {ism.title()}, tanishganimdan xursandman 🙂 ")
print("O'yin boshlandi")
num1 = 0
hisob1 = []
hisob2 = []

num2 = random.randrange(1,3)
while num1 != 'exit':
  num1 = input("\n1. ROR\n2.QAYCHI\n3.QOG'OZ.\n To'xtatish uchun 'exit' deb yozing  \nSon kiriting: ")
  print("\nSiz kiritgan son: ", num1)
  print("Kompyuter kiritgan son: ", num2)
  
  if num1 == '1':
    
    if num2 == '1':
      print("\nO'yin natijasi: Durrang")
    elif num2 == '2':
      print("\nO'yin natijasi: Siz yutkazdingiz")
      hisob2.append(1)
    else:
      print("\nO'yin natijasi: Siz yutdingiz")
      hisob1.append(1)
      
  elif num1 == '2':
    
    if num2 == '1':
      print("\nO'yin natijasi: Siz yutdingiz")
      hisob1.append(1)
    elif num2 == '2':
      print("\nO'yin natijasi: Durrang")
    else:
      print("\nO'yin natijasi: Siz yutdingiz")
      hisob1.append(1)
  
  elif num1 == '3':
    
    if num2 == '1':
      print("\nO'yin natijasi: Siz yutdingiz")
      hisob1.append(1)
    elif num2 == '2':
      print("\nO'yin natijasi: Siz yutkazdingiz")
      hisob2.append(1)
    else:
      print("\nO'yin natijasi: durrang")
  elif num1 == 'exit':
    print("Sizni to'plagan balingiz: ", sum(hisob1))
    print("Kompyuterni toplagan bali: ", sum(hisob2))
    if hisob1 > hisob2:
      print("Siz yutdingiz")
    elif hisob2 > hisob1:
      print("siz yutkazdingiz")
    else:
      print("Natija teng")
  else:
    print("Siz notogri malumot kiritdingiz")
