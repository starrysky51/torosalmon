response = ''

import sys

while True:
    print('終了するにはexitと入力してください。')
    responde = input()
    if response == 'exit':
        sys.exit()
    print(response + 'と入力されました。')
