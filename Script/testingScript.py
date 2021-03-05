import pyperclip

ohm = int(input("number0:"))
ohm1 = int(input("number1:"))

result = (ohm / (ohm1 + ohm)) * 100

pyperclip.copy(result)
print(f"result {result}")
