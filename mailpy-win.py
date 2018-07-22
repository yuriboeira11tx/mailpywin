#coding: utf-8
# Developer: Derxs
# Version: 1.0
import wx, smtplib

class ClasseJanela(wx.Frame):
	def __init__(self, *args, **kwargs):
		super(ClasseJanela, self).__init__(*args, **kwargs)
		self.basic_gui()

	def basic_gui(self):
		title = 'MailPy Win 1.0'

		def get_email():
			emailDialog = wx.TextEntryDialog(None, 'Digite seu e-mail', title)

			if emailDialog.ShowModal() == wx.ID_OK:
				email = emailDialog.GetValue()
				
				if ('@' not in email) or (email.strip() == ''):
					erroBox = wx.MessageBox('Digite seu e-mail, por favor', 'Erro', wx.OK | wx.ICON_ERROR)
					get_email()

				return email
			else:
				exit(0)

		def get_password():
			passwordDialog = wx.PasswordEntryDialog(None, 'Digite sua senha', title)

			if passwordDialog.ShowModal() == wx.ID_OK:
				password = passwordDialog.GetValue()
				
				if password.strip() == '':
					erroBox = wx.MessageBox('Digite sua senha, por favor', 'Erro', wx.OK | wx.ICON_ERROR)
					get_password()
			
				return password
			else:
				exit(0)

		def send_email():
			email = get_email()
			password = get_password()
			
			serv = smtplib.SMTP()
			
			serv.connect('smtp.gmail.com', 587)
			serv.starttls()

			try:
				serv.login(email, password)
				
				wx.MessageBox('Logado com sucesso!', title, wx.ICON_INFORMATION)

				emailsDialog = wx.TextEntryDialog(None, 'Digite os destinatários separados por vírgula', title)
				
				if emailsDialog.ShowModal() == wx.ID_OK:
					lista = emailsDialog.GetValue().split(',')

				messageDialog = wx.TextEntryDialog(None, 'Digite o texto do e-mail', title)
				
				if messageDialog.ShowModal() == wx.ID_OK:
					messageEmail = messageDialog.GetValue()

				try:
					for so_vai in lista:
						serv.sendmail(email, so_vai, messageEmail.encode('utf-8'))

					serv.quit()
					
					wx.MessageBox('E-mail enviado com sucesso!', title, wx.OK | wx.ICON_INFORMATION)
					
					exit(0)
				except:
					serv.quit()
					
					wx.MessageBox('Erro ao enviar e-mails, verifique sua conexão com a internet!', title, wx.OK | wx.ICON_ERROR)

					send_email()

			except:
				serv.quit()
				
				wx.MessageBox('Erro ao fazer login!', title, wx.OK | wx.ICON_ERROR)
				wx.MessageBox('Verifique seus dados de e-mail e senha!', title, wx.OK | wx.ICON_EXCLAMATION)

				send_email()

		send_email()

def main():
	app = wx.App()
	ClasseJanela(None)
	app.MainLoop()

main()
