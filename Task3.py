fract_1 = input("Введите первую дробь вида “a/b”: ")
fract_2 = input("Введите вторую дробь вида “c/d”: ")
   
a, b = map(int, fract_1.split("/"))
c, d = map(int, fract_2.split("/"))
    
sum_fract_numerator = a * d + c * b
sum_fract_denom = b * d
    
multip_fract_numerator = a * c
multip_fract_denom = b * d

print(f"{fract_1} + {fract_2} = {sum_fract_numerator}/{sum_fract_denom}")
print(f"{fract_1} * {fract_2} = {multip_fract_numerator}/{multip_fract_denom}")