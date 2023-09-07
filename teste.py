import ctypes
import os

class auto():
    def __init__(self) -> None:
        pass

    def run_as_admin(self, command):
        try:
            if ctypes.windll.shell32.IsUserAnAdmin():
                os.system(f'cmd.exe /K "{command}"')
            else:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/K {command}", None, 1)
        except Exception as e:
            print(f"Erro ao executar como administrador: {str(e)}")

opcoes_slmgr_ipk = {
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

comandos_sequenciais = [
    'slmgr /ipk {}',  
    'slmgr.vbs /skms kms.lotro.cc',
    'slmgr.vbs /ato',
    'slmgr.vbs /dli'
]

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

vers = int(input('DIGITE QUAL NÚMERO ACIMA REPRESENTA A VERSÃO DO SEU WINDOWS: '))

ativa = auto()

if vers in opcoes_slmgr_ipk:
    chave_produto = opcoes_slmgr_ipk[vers]
    comando_slmgr_ipk = 'slmgr /ipk {}'.format(chave_produto)
    comandos_sequenciais[0] = comando_slmgr_ipk

    # Concatene todos os comandos com o operador '&&' para executá-los em um único prompt de comando
    comando_total = " && ".join(comandos_sequenciais)
    print(f"Executando comandos: {comando_total}")
    ativa.run_as_admin(comando_total)
else:
    print("Opção inválida.")
