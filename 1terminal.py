import ctypes
import os
import pyautogui as py
from time import sleep
import subprocess
import sys

print("""VERIFIQUE A SUA VERSÃO DO WINDOWS:
      [1]PARA : Windows 10 Home
      [2]PARA : Windows 10 Home N
      [3]PARA : Windows 10 Home Single Language
      [4]PARA : Windows 10 Home Country Specific
      [5]PARA : Windows 10 Professional 
      [6]PARA : Windows 10 Professional N
      [7]PARA : Windows 10 Enterprise
      [8]PARA : Windows 10 Enterprise N
      [9]PARA : Windows 10 Education
      [10]PARA : Windows 10 Education N
      [11]PARA : Windows 10 Enterprise 2015 LTSB
      [12]PARA : Windows 10 Enterprise 2015 LTSB N""")

inpt = int(input('DIGITE QUAL VERSÃO QUE REPRESENTA SEU COMPUTADOR: '))


class auto():
    def __init__(self):
        self.opcoes_slmgr_ipk = {
            1: 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99',
            2: '3KHY7-WNT83-DGQKR-F7HPR-844BM',
            3: '7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH',
            4: 'PVMJN-6DFY6-9CCP6-7BKTT-D3WVR',
            5: 'W269N-WFGWX-YVC9B-4J6C9-T83GX',
            6: 'MH37W-N47XK-V7XM9-C7227-GCQG9',
            7: 'NPPR9-FWDCX-D2C8J-H872K-2YT43',
            8: 'DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4',
            9: 'NW6C2-QMPVW-D7KKK-3GKT6-VCFB2',
            10: '2WH4N-8QGBV-H22JP-CT43Q-MDWWJ',
            11: 'WNMTR-4C88C-JK8YV-HQ7T2-76DF9',
            12: '2F77B-TNFGY-69QQF-B8YKP-D69TJ',
        }

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def comando(self):
        comando = 'ipconfig'
        
        if self.is_admin():
            resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
            print("Saída do comando:")
            print(resultado.stdout)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                

    def main(self):
        self.is_admin()
        self.comando()


ativa = auto()
ativa.main()


