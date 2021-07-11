initial_quantity = int(input())
final_quantity = int(input())
periods = 0
atoms = initial_quantity
while atoms > final_quantity:
    periods += 1
    atoms *= 0.5
print(periods * 12)
