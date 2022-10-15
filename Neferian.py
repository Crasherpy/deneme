from curses import raw
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("Neferian")
print("""
Welcome to the Neferian Pentest Tool
1) Paramspider
2)Dalfox
3)SQL Scanner
Telegram:Neferian
""")
Scanning = raw_input("Select the tool you will use")
if(Scanning == "1"):
    target = raw_input("Target:")
    os.system(python3 paramspider.py -d + target)
elif(Scanning=="2"):
    os.system(./dalfox file prodaft.txt -b hahwul.xss.ht)
elif(Scanning=="3"):
    target2 = raw_input("Dork:")
    os.system("python3 main.py -d + target2")