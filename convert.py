import os
import subprocess

def convert():
    source = 'Source'
    result = 'Result'
    source_path = os.listdir(source)
    if not os.path.exists(result):
        os.mkdir('Result')
    for i in source_path:
        print('Начинаю сжатие')
        subprocess.run("{} {}{} -resize 200 {}{}".format(os.path.join(os.getcwd(), 'convert.exe'),
                        os.path.join(os.getcwd(), 'Source', ''), i, os.path.join(os.getcwd(), 'Result', ''), i))
        print('Успешно')
convert()
