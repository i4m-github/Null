import os, time
try:
    import random
except:
    os.system('pip install random')
    pass
try:
    os.remove('/sdcard/Qamar-List.txt')
except:
    pass
logo = '''

 ██╗ █████╗  ██╗██╗  ██╗    ████████╗███╗   ███╗
███║██╔══██╗███║██║  ██║    ╚══██╔══╝████╗ ████║
╚██║╚██████║╚██║███████║       ██║   ██╔████╔██║
 ██║ ╚═══██║ ██║╚════██║       ██║   ██║╚██╔╝██║
 ██║ █████╔╝ ██║     ██║       ██║   ██║ ╚═╝ ██║
 ╚═╝ ╚════╝  ╚═╝     ╚═╝       ╚═╝   ╚═╝     ╚═╝
        [Qamar - Coder] - FB > Kak Qamar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
def qamar():
    good=0
    # User
    os.system('cls')
    print(logo)
    br = int(input('[+] Chand : '))
    for c in range(br):
        os.system('cls')
        print(logo)
        yah = "+964"
        yah2 = "0"
        ok = ["770","750","780"]
        ok2 = random.choice(ok)
        net = random.randint(1000000 ,9999999)
        kak_qamar = str(yah)+str(ok2)+str(net)+":"+str(yah2)+str(ok2)+str(net)
        xw = open(f'/sdcard/Qamar-List.txt','a')
        xw.write(f'{kak_qamar}\n')
        xw.close()
        good+=1
        print(f"Good : {good}")
def qamar2():
    good=0
    # 1122334455
    os.system('cls')
    print(logo)
    br = int(input('[+] Chand : '))
    for c in range(br):
        os.system('cls')
        print(logo)
        yah = "+964"
        yah2 = "0"
        ok = ["770","750","780"]
        xxx = '1122334455'
        ok2 = random.choice(ok)
        net = random.randint(1000000 ,9999999)
        kak_qamar2 = str(yah)+str(ok2)+str(net)+":"+str(xxx)
        xw = open(f'/sdcard/Qamar-List.txt','a')
        xw.write(f'{kak_qamar2}\n')
        xw.close()
        good+=1
        print(f"Good : {good}")
def qamar3():
    good=0
    # 1234554321
    os.system('cls')
    print(logo)
    br = int(input('[+] Chand : '))
    for c in range(br):
        os.system('cls')
        print(logo)
        yah = "+964"
        yah2 = "0"
        ok = ["770","750","780"]
        xxx = '1234554321'
        ok2 = random.choice(ok)
        net = random.randint(1000000 ,9999999)
        kak_qamar3 = str(yah)+str(ok2)+str(net)+":"+str(xxx)
        xw = open(f'/sdcard/Qamar-List.txt','a')
        xw.write(f'{kak_qamar3}\n')
        xw.close()
        good+=1
        print(f"Good : {good}")
def qamar4():
    good=0
    # 1234512345
    os.system('cls')
    print(logo)
    br = int(input('[+] Chand : '))
    for c in range(br):
        os.system('cls')
        print(logo)
        yah = "+964"
        yah2 = "0"
        ok = ["770","750","780"]
        xxx = '1234512345'
        ok2 = random.choice(ok)
        net = random.randint(1000000 ,9999999)
        kak_qamar4 = str(yah)+str(ok2)+str(net)+":"+str(xxx)
        xw = open(f'/sdcard/Qamar-List.txt','a')
        xw.write(f'{kak_qamar4}\n')
        xw.close()
        good+=1
        print(f"Good : {good}")
def qamar_tekal():
    good=0
    # Tekal
    os.system('cls')
    print(logo)
    br = int(input('[+] Chand : '))
    for c in range(br):
        os.system('cls')
        print(logo)
        yah = "+964"
        yah2 = "0"
        ok = ["770","750","780"]
        saske = ["1234512345","1122334455","1234554321"]
        ok2 = random.choice(ok)
        net = random.randint(1000000 ,9999999)
        net2 = random.choice(saske)
        #lolol = str(yah)+str(ok2)+str(net)+":"+str(yah2)+str(ok2)+str(net)
        #print(lolol)
        lolol = str(yah)+str(ok2)+str(net)+":"+str(yah2)+str(ok2)+str(net)
        haha = str(yah)+str(ok2)+str(net)+":"+str(net2)
        xw = open(f'/sdcard/Qamar-List.txt','a')
        xw.write(f'{lolol}\n')
        xw.write(f'{haha}\n')
        xw.close()
        good+=1
        print(f"Good : {good}")

def Kak_Qamar():
    os.system('cls')
    print(logo)
    print('[1] EXAM [+964770... + 0770......]\n[2] EXAM [+964770... + 1122334455]\n[3] EXAM [+964770... + 1234554321]\n[4] EXAM [+964770... + 1234512345]\n[5] EXAM [Tekall [1] [2] [3] [4] ]\n')
    lalala = input('[+] Jory Combo : ')
    if lalala=='1':
        qamar()
    elif lalala=='2':
        qamar2()
    elif lalala=='3':
        qamar3()
    elif lalala=='4':
        qamar4()
    elif lalala=='5':
        qamar_tekal()
    else:
        print('Hallat Krd ... ')
        time.sleep(5)
        Kak_Qamar()
Kak_Qamar()


