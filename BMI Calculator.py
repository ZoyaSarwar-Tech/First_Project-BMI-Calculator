print("Welcome to the BMI Calculator")

weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in m? "))
bmi = weight / (height * height)
bmi=weight/(height**2)
print(f"Your BMI is:{bmi: .2f}")

if bmi < 18.5:
    advice = "You are under 18.5"
elif 18.5 <= bmi < 25:
    advice = "You are under 25"
elif 25 <= bmi < 30:
    advice = "You are under 30"
else:
    advice = "You are under 35"

print(advice)