#--conding:utf-8--
import math
import os

os.system("cls")
print("Input an unsigned integer number:")
nDecNum = int(input())
strLine = ""
if(nDecNum < 0):
    print("Invalid number format")
nTempVal = nDecNum
while (nTempVal > 0):
    strLine = str(nTempVal % 2)  + strLine
    nTempVal //= 2
if(len(strLine) == 0):
    strLine = "0"
print(f"The binary equivalent of the decenary number {nDecNum} is {strLine}")