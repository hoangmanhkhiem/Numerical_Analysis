# AUTHOR
# Name: Hoàng Mạnh Khiêm ( Skromnyy )
# Github : https://github.com/hoangmanhkhiem/Giai_Tich_So/
# Facebook : https://www.facebook.com/hoangmankhiem.IT
# Contact : khiemhm04@gmail.com


import numpy as np
import matplotlib.pyplot as plt
import math
import sympy as sym

#Các hàm phụ trợ

#Tính sai phân
def saiphan(a): # a là một array hoặc list
  n = len(a)
  result = []
  for i in range(n-1):
    result.append(np.round(a[i+1] - a[i],4))
  return result
# input = [1, 3, 4, 5]
# output = [2, 1, 1]

# Tính bảng sai phân
def bangsaiphan(x, y):
  n = len(x)
  # tạo bảng sai phân
  table = [y]
  # thêm n - 1 cột của bảng sai phân
  for i in range(n - 1):
    table.append(saiphan(table[i]))
  return table

#Các hàm sau dựa theo pp Horner

# Nhân đa thức với một số
def mulConst(a:list, c:float): # nhân đa thức với 1 số
  ans = []
  for i in a:
    ans.append(i*c)
  return ans

# Cộng hai đa thức
def sumHorner(a:list, b:list): # cộng hai đa thức
  if(len(a)>len(b)):
    for i in range(len(b)):
      a[i] = a[i] + b[i]
    return a
  else:
    for i in range(len(a)):
      b[i] = a[i] + b[i]
    return b

# Phục vụ để tính phần tích t(t-1)(t+1)... theo Horner
def mulHorner(a:list, m:float, case:int): #nhân với đa thức bậc 1 dạng (x+int(m/2))
  c = int(m/2)
  ans = []
  if((m%2==1 and case==1) or (m%2==0 and case==2)):
    for j in range(len(a)):
      if(j==0):
        ans.append(a[j]*c)
      else:
        ans.append(a[j-1]+a[j]*c)
    ans.append(1)
  else:
    for j in range(len(a)):
      if(j==0):
        ans.append(a[j]*(-c))
      else:
        ans.append(a[j-1]+a[j]*(-c))
    ans.append(1)

  return ans

# Tính giá trị đa thức
def horner(poly, x): # tính giá trị đa thức
    # poly.reverse()
    # result = poly[0]
    # for i in range(1, len(poly)):
    #     result = result*x + poly[i]
    # poly.reverse()

    n = len(poly)
    result = poly[n-1]
    for i in range(n-2,-1,-1):
      result = result*x + poly[i]
    return result

# dùng sybolic để đưa ra đa thức theo x từ t
def display_poly_gauss_1(poly_t, x):
  # đa thức theo t
  t = sym.Symbol('t')
  ans = 0
  for i in range(len(poly_t)):
    ans = ans + np.round(poly_t[i],4)*t**i

  ans1 = sym.expand(ans)

  # đa thức theo x
  n = len(x)
  h = x[1] - x[0]
  if(n%2==1):
    x0 = x[int(n/2)]
  else:
    x0 = x[int((n-1)/2)]
  x = sym.Symbol('x')
  ans2 = sym.expand(ans.subs(t, (x-x0)/h))
  return ans1, ans2

def display_poly_gauss_2(poly_t, x):
  # đa thức theo t
  t = sym.Symbol('t')
  ans = 0
  for i in range(len(poly_t)):
    ans = ans + np.round(poly_t[i],4)*t**i
  ans1 = sym.expand(ans)

  # đa thức theo x
  n = len(x)
  h = x[1] - x[0]
  x0 = x[int(n/2)]
  x = sym.Symbol('x')
  ans2 = sym.expand(ans.subs(t, (x-x0)/h))
  return ans1, ans2