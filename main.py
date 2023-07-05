num1 = float(input("Enter Targeting Range: "))
num2 = int(input("Enter Dampeners: "))
num3 = float(input("Enter Dampener Power: "))

power_reduction = 0.85
targeting_range = num1

for _ in range(num2):
    targeting_range = (targeting_range * num3 + num1 * (1 - num3)) / 100
    num3 *= power_reduction

print("Targeting Range with {} dampeners, each with a power of {}: {:.6f}".format(num2, num3, targeting_range* 100))
