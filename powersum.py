def main():
  a = 0
  b = 0
  maximum = 0
  while(a<100):
  	while(b<100):
  		newnum = a**b
  		b+=1
  	a+=1


def sumdigits(num):
  place = 1
  sumdigits = 0
  while (num>0):
    sumdigits += num%10
    num = num//10
  return sumdigits

