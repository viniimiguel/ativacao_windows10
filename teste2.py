import ctypes
import os

def run_as_admin(command):
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            os.system(command)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/K " + command, None, 1)
    except Exception as e:
        print(f"Erro ao executar como administrador: {str(e)}")

# Resto do seu código aqui...

# Comando que você deseja executar no Prompt de Comando como administrador
comando = "slmgr -rearm"

# Chama a função para executar o comando como administrador
run_as_admin(comando)