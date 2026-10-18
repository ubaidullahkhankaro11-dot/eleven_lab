import socket, hashlib
from urllib.parse import urlparse

G = "\033[92m"; R = "\033[91m"; C = "\033[96m"; Y = "\033[93m"; M = "\033[95m"; RST = "\033[0m"

print(f"{M}╔══════════════════════════════════════╗")
print(f"║ ███████╗██╗ ███████╗██╗ ██╗ ║")
print(f"║ ██╔════╝██║ ██╔════╝██║ ██║ ║")
print(f"║ █████╗ ██║ █████╗ ██║ ██║ ║")
print(f"║ ██╔══╝ ██║ ██╔══╝ ╚██╗ ██╔╝ ║")
print(f"║ ███████╗███████╗ ╚████╔╝ ║")
print(f"║ ╚══════╝╚══════╝╚══════╝ ╚═══╝ ║")
print(f"║ LAB v5 - ULTIMATE ║")
print(f"╚══════════════════════════════════════╝{RST}")

while True:
    print(f"\n{C}[1]{RST} Fake Link Check {C}[4]{RST} Website Banner")
    print(f"{C}[2]{RST} My IP {C}[5]{RST} Port Scanner")
    print(f"{C}[3]{RST} Password Check {C}[6]{RST} Hash Generator (NEW!)")
    print(f"{R}[0] Exit{RST}")
    ch = input(f"{Y}eleven_lab@Ubaid:~$ {RST}")

    if ch == "6":
        text = input(f"{C}Text likho jiska Hash banana hai: {RST}")
        print(f"{G}[MD5] {hashlib.md5(text.encode()).hexdigest()}{RST}")
        print(f"{G}[SHA256] {hashlib.sha256(text.encode()).hexdigest()}{RST}")
        print(f"{Y}Ye hashing hackers password store karne ke liye use karte hain{RST}")
    elif ch == "5":
        target = input(f"{C}Target (localhost): {RST}").strip() or "localhost"
        target = target.replace("https://","").split("/")[0]
        ip = socket.gethostbyname(target)
        print(f"{Y}[*] Scanning {ip}...{RST}")
        for p in [21,22,53,80,443,8000,8080,8022,3306]:
            s=socket.socket(); s.settimeout(0.8)
            if s.connect_ex((ip,p))==0: print(f"{G}[OPEN] {p}{RST}")
            else: print(f"{R}[CLOSED] {p}{RST}")
            s.close()
    elif ch == "4":
        site = input(f"{C}Site (google.com): {RST}").replace("https://","").split("/")[0]
        try:
            ip=socket.gethostbyname(site)
            print(f"{G}IP: {ip}{RST}")
            s=socket.socket(); s.settimeout(2); s.connect((ip,80))
            s.send(b"HEAD / HTTP/1.0\r\n\r\n")
            print(s.recv(512).decode(errors='ignore')[:300]); s.close()
        except Exception as e: print(f"{R}{e}{RST}")
    elif ch == "3":
        pwd=input(f"{C}Password: {RST}")
        print(f"{G}MAZBOOT{ RST}" if len(pwd)>=8 and any(c.isdigit() for c in pwd) else f"{R}KAMZOR{RST}")
    elif ch == "2":
        print(f"{G}{socket.gethostbyname(socket.gethostname())}{RST}")
    elif ch == "1":
        link=input(f"{C}Link: {RST}")
        print(f"{R}KHATARNAK{RST}" if "@" in link else f"{G}SAF{RST}")
    elif ch=="0":
        print(f"{M}Allah Hafiz! Lab Closed.{RST}"); break
