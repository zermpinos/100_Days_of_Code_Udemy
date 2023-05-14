print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
input_tip = int(input('What percentage should the tip be? 10, 12 or 15?'))
math_tip = 1.00 + input_tip/100
persons = int(input('Between how many people is the bill divided?'))
result = round((total_bill / persons) * math_tip, 2)
print(f'{result:.2f}')
