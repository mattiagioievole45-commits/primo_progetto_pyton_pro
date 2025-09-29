import random 
elementi = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

caratteri = int(input('quanto deve essere lunga la password?'))
password = ''


'''
password = 'f'
print(password)
password = random.choice(elementi)
print(password)
'''


for i in range (caratteri):
    #password = random.choice(elementi)
    password=password +  random.choice(elementi)
      #  'b'    = ''  + 'b'
      # 'bc'     = 'b' + 'c'
      # 'bca'      = 'bc'  + 'a'
    
print(password)

    
