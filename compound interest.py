business_name = "yusuf & sons"
p = float(input("enter principal: "))
r = float(input("enter rate: "))
t = float(input("enter time: "))

simple_interest = p * r * t / 100
compound_interest = p * (1 + r/100)**t


print(business_name)
print('simple interest is: %f'% (simple_interest))
print('compound interest is: %f'% (compound_interest))