#!usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")
os.system("Figlet Neferian")
print("""
Welcome to the Neferian Pentest Tool
1) Paramspider
2)Dalfox
3)SQL Scanner
Telegram:Neferian
""")
scanning = input("Select the tool you will use:")
if(scanning == "1"):
    target = input("Target:")
    os.system("cd ParamSpider-master")
    os.system("python3 paramspider.py -d" + target)
elif(scanning=="2"):
    os.system("./dalfox file prodaft.txt -b hahwul.xss.ht")
elif(scanning=="3"):
    target2 = input("Dork:")
    os.system("cd SQL-scanner-master")
    os.system("python3 main.py -d" + target2)
