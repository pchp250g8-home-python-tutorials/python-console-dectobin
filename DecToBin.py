# --conding:utf-8--
import os

os.system("cls")
print("Input an unsigned integer number:")
MAX_INT = 2 ** 32 - 1
nDecNum = int(input())
strLine = ""
if (nDecNum < 0 or nDecNum > MAX_INT):
    print("Invalid number format")
nTempVal = nDecNum
while (nTempVal > 0):
    strLine = str(nTempVal % 2) + strLine
    nTempVal //= 2
if (len(strLine) == 0):
    strLine = "0"
print(f"The binary equivalent of the decimal number {nDecNum} is {strLine}")
