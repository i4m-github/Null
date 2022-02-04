import os,wget
try:
    import pyfiglet
except:
    os.system('pip install pyfiglet')
    pass
os.system('cls')
os.system('pyfiglet MUSIC')
sss = "[1] English\n[2] Kurdish\n[3] Persian"
print(sss)
sss2 = input('\n[+] Halzhera : ')
def music():
    if sss2 == '1':
        wget.download("https://raw.githubusercontent.com/i4m-github/Null/main/1.mp3")
        os.system("termux-media-player play 1.mp3")
    elif sss2 == '2':
        wget.download("https://raw.githubusercontent.com/i4m-github/Null/main/2.mp3")
        os.system("termux-media-player play 2.mp3")
    elif sss2 == '3':
        wget.download("https://raw.githubusercontent.com/i4m-github/Null/main/3.mp3")
        os.system("termux-media-player play 3.mp3")
music()
