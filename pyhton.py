
def bmi_calculator(weight_kg,height_m):
  bmi = weight_kg / (height_m ** 2)
  print("Bmi: ")
  print(bmi)
  if bmi <25:
    print("the person is not oveweight!")
  else:
    print("the person is overweight !")


weight_kg = int(input("enter you weight_kg: "))
height_m = float(input("enter your height_m: "))
bmi_calculator(weight_kg, height_m)
