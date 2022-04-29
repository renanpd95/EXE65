import os,random,time


result = 0

for i in range(50):
  n = (random.randint (-1000,1000)) 
  print(n)
  time.sleep(0.1)
  
  if( n < 0):
    result = result+1

else:
  os.system('clear')
  print("\nO total de números negativos é :",result)
  
  
  
 