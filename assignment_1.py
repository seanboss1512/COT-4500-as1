# Sean Alves
# 1-28-23
# COP-4500-as1

import numpy as py
import math



    # By using this method of creating the S, exponent, and mantissa values,
    # we ensure that the program can be used for other binary values
    # easily by just pasting the binary following the digit "9" in the variable "binary"
binary= str(9010000000111111010111001)
s= binary[1]
s_string= [str(i) for i in s]
final_s_string= "".join(s_string)
s_int= int(final_s_string)
exp=[binary[2:13]]
string_exp=[str(i) for i in exp]
final_string_exp="".join(string_exp)
int_exp=int(final_string_exp)
mant=[binary[14:64]]
string_mant=[str(i) for i in mant]
final_string_mant="".join(string_mant)
int_mant= int(final_string_mant)
i=0
while(int_exp>0):
    conv_exp= (int_exp % 10) * pow(2,i)
    int_exp= int_exp//10
    i+=1
conv_exp= conv_exp-1023
conv_mant=0
i=0
for j in (str(int_mant)):
    conv_mant= conv_mant+ i * (0.5**(i+1))
    i+=1
conv_value= ((-1)**s_int)*(2**(conv_exp))*((1+conv_mant))
print (conv_value,"\n")

# Three digit chopping arithmetic 
conv_value_chopping= conv_value*(10**-1)
three_chopping= (math.floor(conv_value_chopping*1000))/1000
print(three_chopping,"\n")
# Three digit rounding arithmetic
three_rounding= conv_value * (10**-1) +.0005
three_rounding= round(three_rounding,3)
print(three_rounding,"\n")
# Absolute error
abs_error= abs(conv_value-(three_rounding*10))
print (abs_error,"\n")
# Relative error
rel_error= abs((conv_value-(three_rounding*10))/ conv_value)
print (rel_error,"\n")
# Series itterations count
def inf_series(x,k):
    return abs((((-1)**k) * ((x**k)/(k**3))))
itterations=1
while((inf_series(1,itterations))>10**-4):
    itterations+=1
print (itterations-1)


