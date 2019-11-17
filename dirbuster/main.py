#project rewriting of dirbbuster
#required modules date:17/11/2019 time:4:56


import requests
import sys
import socket
from time import time 
s = str(round(time() * 1000))
fobj_out = open("Tabelle" + s + ".txt", "w")
"""
sys - Used to take command line arguments and exit when needed.
socket - Used to test for a valid URL.
requests - Used to make HTTP requests and receive response code.
"""
rhost=sys.argv[1]
wordlist=sys.argv[2]
store=[]
"""
When we took the input, 
we set a variable named rhost. 
Short for remote host, this is the target.
But, since we're brute forcing directories here,
this needs to be a URL.
First we need to test to see if the given URL exists and is reachable. We can verify this by making a test connection to it using sockets. We'll simply make a socket, and use the connect_ex() method to test the URL. This method returns a zero if the connection was successful, and an error otherwise. 
"""



print('[*] Checking for Rhost:...')
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    status=s.connect_ex((rhost,80))
    s.close()

    if status==0:
        print('done')
    else:
        print('fail')
        print('[!error]:cannot reach rhost')
        sys.exit(1)    
except socket.error as e:
        print('fail')
        print(f'[!error]:cannot reach rhost {rhost}')
        sys.exit(1) 

#Read the Specified Word List

print('[*] parsing wordlist')
try:
    with open(wordlist) as file:
        to_check=file.read().strip().split('\n')
    print('DONE')
    print(f'[*]total path to check {len(to_check)}')        
except IOError:
    print("[!] error:failed to read specified file")
    sys.exit(1)

#a utility function to check the path of website
def checkpath(path):
    try:
        response=requests.get('http://'+rhost+'/'+path).status_code

    except Exception:
        print('[!] Error:An unexpected error occured')
        sys.exit(1)
    if response==200:
        print('[*] valid path Found')


print('[*] beginning scan...')
try:
    for i in to_check:
        checkpath(i)
        store.append('http://'+rhost+'/'+i)
        fobj_out.write('\n'+'http://'+rhost+'/'+i)
    print('[*] Scan completed')
    fobj_out.close()
except KeyboardInterrupt:
    print('[!] Error:use interrupted scan')
    print(store)
    fobj_out.close()
    sys.exit(1)


    





