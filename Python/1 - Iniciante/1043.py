# coding: UTF - 8
# Funcional no URI

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)
if abs(B - C) < A < (B + C) and (A - C) < B < (A + C) and (A - B) < C < (A + B):
    print("Perimetro = {:.1f}".format(A + B + C))
else:
    print("Area = {:.1f}".format(((A+B)/2)*C))
