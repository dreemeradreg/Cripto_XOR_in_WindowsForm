#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
from tkinter import *
from tkinter import messagebox
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

def get_message_decryption():
	try:
		result_de_coding.message_entry.delete(0, END)
		message_user_on_file = message_on_decript.message_entry.get()
		private_key_on_decript = way_privat_key.message_entry.get()

		with open(message_user_on_file, 'rb') as fobj:
			private_key = RSA.import_key(
				open("key/"+private_key_on_decript+".bin").read(),
				passphrase='nooneknows'
			)

			enc_session_key, nonce, tag, ciphertext = [fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

			cipher_rsa = PKCS1_OAEP.new(private_key)
			session_key = cipher_rsa.decrypt(enc_session_key)

			cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
			data = cipher_aes.decrypt_and_verify(ciphertext, tag)
		
		result_de_coding.message_entry.insert(0, data)
	except:
		messagebox.showinfo("Error...", "Не верно заполнены поля!")
		
def get_message_encryption():
	result_in_coding.message_entry.delete(0, END)
	result_in_coding_criete_file.message_entry.delete(0, END)
	message_on_decript.message_entry.delete(0, END)
	try:
		pub_key_user = way_pub_key.message_entry.get()
		messege_user_on_cript = message_on_cript.message_entry.get().encode('utf-8')
		name_file = name_message_on_file.message_entry.get()
		if name_file == "":
			messagebox.showinfo("Error...", "Не заполно поле имяни!!!!")
		elif pub_key_user == "":
			messagebox.showinfo("Error...", "Не заполно поле Ключа")
		elif len(messege_user_on_cript) == 0:
			messagebox.showinfo("Error...", "Ну а где сообщение?")
		else:
			newu_file = name_file + ".bin"
			with open(newu_file, 'wb') as out_file:
				recipient_key = RSA.import_key(
					open('key/'+pub_key_user+'.pem').read()
				)

				session_key = get_random_bytes(16)

				cipher_rsa = PKCS1_OAEP.new(recipient_key)
				out_file.write(cipher_rsa.encrypt(session_key))

				cipher_aes = AES.new(session_key, AES.MODE_EAX)
				ciphertext, tag = cipher_aes.encrypt_and_digest(messege_user_on_cript)

				out_file.write(cipher_aes.nonce)
				out_file.write(tag)
				out_file.write(ciphertext)

			result_in_coding.message_entry.insert(0, ciphertext+tag)
			result_in_coding_criete_file.message_entry.insert(0, newu_file)
			message_on_decript.message_entry.insert(0, newu_file)
	except:
		messagebox.showinfo("Error...", "Не заполнены поля")

def get_generet_keys():
	try:
		way_pub_key.message_entry.delete(0, END)
		size_key = int(len_keys.message_entry.get())
		pub_key = name_pub_key.message_entry.get()
		privat_key = name_privat_key.message_entry.get()
		if pub_key == "" or privat_key == "":
			messagebox.showinfo("Error...", "\nНе заданно имя ключа")
		elif size_key == 1024 or size_key == 2048 or size_key == 4096:
			key = RSA.generate(size_key)
			encrypted_key = key.exportKey(
							passphrase='nooneknows', 
							pkcs=8, 
							protection="scryptAndAES128-CBC"
							)

			with open("key/" +privat_key+".bin", 'wb') as f:
				f.write(encrypted_key)
			with open("key/"+pub_key+".pem", 'wb') as f:
				f.write(key.publickey().exportKey())
			way_pub_key.message_entry.insert(0, pub_key)
			way_privat_key.message_entry.insert(0, privat_key)
		else:
			messagebox.showinfo("Error...", "Не верное значение для длинны ключа 1024/2048/4096")
	except:
		messagebox.showinfo("Error...", "Не заполно поле размера ключа")
	
def get_clear_oll():
	for x in os.listdir("key/"):os.remove("key/"+x)
	your_list = [result_de_coding, way_privat_key, message_on_decript, result_in_coding_criete_file, result_in_coding, way_pub_key, len_keys, name_pub_key, name_privat_key, message_on_cript, name_message_on_file]
	for element in your_list:element.message_entry.delete(0, END)
	Dir = os.getcwd()
	file_liist = os.listdir(Dir)
	Double_count = 0
	i = 0
	while i < len(file_liist):
		if os.path.isfile(file_liist[i]):
			if '.bin' in file_liist[i]:
				os.remove(Dir + '\\' + file_liist[i])
				Double_count += 1
		i += 1

def get_delet_save_key():
	for x in os.listdir("key/"):os.remove("key/"+x)	

class windows_form:
	def __init__(self, message_text, message_row, message_column, element_sticky1, element_sticky2, default_value):
		self.message = StringVar()
		self.message_label = Label(text=message_text)
		self.message_label.grid(row=message_row, column=message_column, sticky=element_sticky1)
		self.message_entry = Entry(textvariable=self.message)
		self.message_entry.grid(row=message_row,column=message_column+1, padx=5, pady=5, sticky=element_sticky2)
		self.message_entry.insert(0, default_value)


class windows_form_button:
	def __init__(self, message_text_on_button, color_button, function_on_button, element_sticky1, element_sticky2, default_value):
		self.Button = Button(text=message_text_on_button, 
								background=color_button,		# фоновый цвет кнопки
								foreground="#ccc",		# цвет текста
								padx="30",				# отступ от границ до содержимого по горизонтали
								pady="10",				# отступ от границ до содержимого по вертикали
								font="16",				# высота шрифта
								command=function_on_button
								)
		self.Button.grid(row=element_sticky1, column=element_sticky2, padx=5, pady=5, sticky=default_value)

if __name__ == '__main__':
	root = Tk()
	root.title("GUI на Python")
	root.geometry("1300x360")

	label = Label(text="Программа. Пример реализации rsa")
	label.grid(row=0, column=2, sticky="w")

	len_keys = windows_form("Введите сложность ключа:", 1, 0, "e", "w", "1024")
	name_pub_key = windows_form("Введите имя для открытого ключа:", 2, 0, "e", "w", "key_pub")
	name_privat_key = windows_form("Введите имя для закрытакого ключа:", 3, 0, "e", "w", "priv_key")
	message_on_cript = windows_form("Введите сообщение для шифрования:", 2, 2, "e", "w", "")
	name_message_on_file = windows_form("Введите имя для файла передачи", 1, 2, "e", "w", "")
	way_pub_key = windows_form("Введите имя для ОТКРЫТОГО ключа:", 3, 2, "e", "w", "")
	result_in_coding = windows_form("ответ:", 6, 2, "e", "w", "")
	result_in_coding_criete_file = windows_form("был создан файл для отправки:", 7, 2, "e", "w", "")
	message_on_decript = windows_form("имя файла который принимает:", 2, 4, "e", "w", "")
	way_privat_key = windows_form("Введите имя для ЗАКРЫТОГО ключа:", 3, 4, "e", "w", "")
	result_de_coding = windows_form("Дешифровка:", 6, 4, "e", "w", "")

	generet_keys = windows_form_button("Сгенерировать ключи", "#555", get_generet_keys, 5,1,"e")
	delet_save_key = windows_form_button("Удалить ключи", "#900", get_delet_save_key, 6,1,"s")
	message_encryption = windows_form_button("Зашифровать", "#555", get_message_encryption, 5,3,"e")
	message_decryption = windows_form_button("Дешифровать", "#555", get_message_decryption, 5,5,"e")
	slear_oll = windows_form_button("Очистить ВСЁ", "#900", get_clear_oll, 7,1,"s")
	
	root.mainloop()
