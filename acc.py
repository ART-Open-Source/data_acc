
import os, requests
import json
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"
W = f"{w}\033[1;47m"
B = f"{w}\033[1;44m"
space = "         "
lines = space + "-"*44
pn = f"""
  █████▒ ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓      ██████ 
▓██   ▒▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ▒██    ▒ 
▒████ ░░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ░ ▓██▄   
░▓█▒  ░  ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░      ▒   ██▒
░▒█░   ▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒▒██████▒▒
 ▒ ░   ▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░▒ ▒▓▒ ▒ ░
 ░     ░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░░ ░▒  ░ ░
 ░ ░   ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ░  ░  ░  
             ░                  ░ ░      ░ ░      ░  ░      ░  
                     {w}[ FS6.PW ]{b}
                  {d}Tool to get data acc{w}
               {d}     Author by {w}{r}@u929{w}
"""
ng = "+"	
print(b+pn)
print(f"                {b}print {r}Enter {b}to start{b}")
nu = input(r+"┌──(root@FS6)-[~]" + "\n└─$ "+g)

ok = []
mail = open("user.txt","r").read().splitlines()
head1 = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
         'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
         
         'Accept':'*/*', 
         'ContentType':'application/x-www-form-urlencoded', 
         'X-Requested-With':'XMLHttpRequest', 
         'X-IG-App-ID':'936619743392459', 
         'X-Instagram-AJAX':'missing', 
         'X-CSRFToken':'missing', 
         'Accept-Language':'en-US,en;q=0.9'}
       
try:
        for lone in mail:
                req = requests.get(f'https://www.instagram.com/{lone}/?__a=1')
                user = str(req.json()["graphql"]["user"]["id"])
                
                response = requests.get(
                    "https://fs6ah.com/dataacc/?id=" + user)
                ree = (response.json()['data'])
                print(f"{space}{B} DONE {w} Data: {g}{ree}{w} User: {g}{lone}")
                
                
except KeyboardInterrupt:
        pass

print(w+lines)
print(f"{space}{b}>{w} Done cheack {str(len(ok))} Users")