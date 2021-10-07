#cradit:geeksforgeeks
import os,time,sys
os.system("pip install numpy")
os.system("curl -LO https://its-pointless.github.io/setup-pointless-repo.sh") 
os.system("bash setup-pointless-repo.sh")
os.system("pkg install opencv")
os.system("clear")
try:
    import cv2
except:
    print('\033[1;31myou not installed cv2')
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
print("""\033[1;32m
 █████        ███████ ██   ██ ███████ ████████  ██████ ██   ██ 
██   ██       ██      ██  ██  ██         ██    ██      ██   ██ 
███████ █████ ███████ █████   █████      ██    ██      ███████ 
██   ██            ██ ██  ██  ██         ██    ██      ██   ██ 
██   ██       ███████ ██   ██ ███████    ██     ██████ ██   ██ 

                  \033[1;37m  HELLO I AM ABIR HOSSAIN
            ╔══════════════════════════════════════╗
            ║AUTHOR      : ABIR HOSSAIN            ║
            ║FACEBOOK    : Abir Hossain            ║
            ╚══════════════════════════════════════╝       
            ========================================                                                               
""")
jalan('\033[1;35m                  Conver your image to sketch ')
print()
a=input('\033[1;36mENTER YOUR IMAGE PATH : \033[1;32m')
if a=='':
    print('\033[1;31minviled')
print()
b=input('\033[1;36mENTER OUTPUT SKETCH PATH:\033[1;32m ')
if b=='':
    print('\033[1;31minviled')
print()
jalan('\033[1;35mGenerating You Sketch......')
time.sleep(5)
image = cv2.imread(a)
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite(b, sketch)
print()
jalan('\033[1;33mYour Sketch  Save as :  \033[1;37m'+b)
os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
