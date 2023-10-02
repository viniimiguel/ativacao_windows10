import ctypes
import subprocess
import sys

class Auto:
    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def comando(self):
        if self.is_admin():
            
            comando_ipk = f'slmgr /ipk {inpt}'
            resultado_ipk = subprocess.run(comando_ipk, shell=True, capture_output=True, text=True)
            print("Saída do comando slmgr /ipk:")
            print(resultado_ipk.stdout)

        
            comando_skms = 'slmgr.vbs /skms kms.lotro.cc'
            resultado_skms = subprocess.run(comando_skms, shell=True, capture_output=True, text=True)
            print("Saída do comando slmgr.vbs /skms:")
            print(resultado_skms.stdout)

        
            comando_ato = 'slmgr.vbs /ato'
            resultado_ato = subprocess.run(comando_ato, shell=True, capture_output=True, text=True)
            print("Saída do comando slmgr.vbs /ato:")
            print(resultado_ato.stdout)

            
            comando_dli = 'slmgr.vbs /dli'
            resultado_dli = subprocess.run(comando_dli, shell=True, capture_output=True, text=True)
            print("Saída do comando slmgr.vbs /dli:")
            print(resultado_dli.stdout)
        else:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

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

ativa = Auto()
ativa.comando()
