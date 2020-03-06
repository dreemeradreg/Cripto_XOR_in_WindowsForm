from tkinter import *
from tkinter import messagebox

def get_list_search(received_data):
	list_it_bin_asci_cod = {"А": "11000000", 
				"Б":"11000001",
				"В":"11000010",
				"Г":"11000011",
				"Д":"11000100",
				"Е":"11000101",
				"Ж":"11000110",
				"З":"11000111",
				"И":"11001000",
				"Й":"11001001",
				"К":"11001010",
				"Л":"11001011",
				"М":"11001100",
				"Н":"11001101",
				"О":"11001110",
				"П":"11001111",
				"Р":"11010000",
				"С":"11010001",
				"Т":"11010010",
				"У":"11010011",
				"Ф":"11010100",
				"Х":"11010101",
				"Ц":"11010110",
				"Ч":"11010111",
				"Щ":"11011001",
				"Ш":"11011000",
				"Ь":"11011100",
				"Ы":"11011011",
				"Ъ":"11011010",
				"Э":"11011101",
				"Ю":"11011110",
				"Я":"11011111"
				}

	len_received_data = received_data
	answer = ""
	i = 0
	while i < len(len_received_data):
		result_grep_in_list = list_it_bin_asci_cod[received_data[i]]
		answer = answer + result_grep_in_list
		i += 1

	return answer

def get_method_addition_XOR(nom1_variable, nom2_variable):
	answer = ""
	i = 0
	while i < len(nom1_variable):
		value_variable_1 = nom1_variable[i]
		value_variable_2 = nom2_variable[i]
		if value_variable_1 == value_variable_2:
			h = "0"
		else:
			h = "1"
		answer = answer + h
		i += 1
	return answer


def rot_mi_foot(text_on_cript, gamma_1, gamma_2, gamma_3):
    text_on_cript_bin = get_list_search(text_on_cript)
    gamma_1_bin = get_list_search(gamma_1)
    gamma_2_bin = get_list_search(gamma_2)
    gamma_3_bin = get_list_search(gamma_3)

    answer_bin_cod = get_method_addition_XOR(text_on_cript_bin, gamma_1_bin)
    answer_bin_cod = get_method_addition_XOR(answer_bin_cod, gamma_2_bin)
    answer_bin_cod = get_method_addition_XOR(answer_bin_cod, gamma_3_bin)

    result_coding_entry.insert(0, answer_bin_cod)
    return 0

def get_de_cod(text_on_cript_bin, gamma_1, gamma_2, gamma_3):
    gamma_1_bin = get_list_search(gamma_1)
    gamma_2_bin = get_list_search(gamma_2)
    gamma_3_bin = get_list_search(gamma_3)

    answer_bin_cod = get_method_addition_XOR(gamma_1_bin, gamma_2_bin)
    answer_bin_cod = get_method_addition_XOR(answer_bin_cod, gamma_3_bin)
    answer_bin_cod = get_method_addition_XOR(answer_bin_cod, text_on_cript_bin)

    result_de_coding_entry.insert(0, answer_bin_cod)
    return 0

def get_clear_cod():
	gamma_1_entry.delete(0, END)
	gamma_2_entry.delete(0, END)
	gamma_3_entry.delete(0, END)
	name_entry.delete(0, END)
	bin_name_entry.delete(0, END)
	result_coding_entry.delete(0, END)
	result_de_coding_entry.delete(0, END)
	bin_de_code_entry.delete(0, END)


def get_coding_xor():
	result_coding_entry.delete(0, END)

	text_on_cript = name_entry.get().upper()
	gamma_1 = gamma_1_entry.get().upper()
	gamma_2 = gamma_2_entry.get().upper()
	gamma_3 = gamma_3_entry.get().upper()

	if len(text_on_cript) == len(gamma_1) and len(gamma_1) == len(gamma_2) and len(gamma_2) == len(gamma_3):
		otv = rot_mi_foot(text_on_cript, gamma_1, gamma_2, gamma_3)
	else:
		messagebox.showinfo("GUI Python", "Error... \nдлинна между введёнными значениями не одинаковая")


def get_incoding_xor():
	result_de_coding_entry.delete(0, END)

	text_on_cript = bin_name_entry.get()
	gamma_1 = gamma_1_entry.get().upper()
	gamma_2 = gamma_2_entry.get().upper()
	gamma_3 = gamma_3_entry.get().upper()

	if len(text_on_cript) / 8 == len(gamma_1) and len(gamma_1) == len(gamma_2) and len(gamma_2) == len(gamma_3):
		otv = get_de_cod(text_on_cript, gamma_1, gamma_2, gamma_3)
	else:
		messagebox.showinfo("GUI Python", "Error... \nдлинна между введёнными значениями не одинаковая")

def get_de_cod_bin_in_text():
	bin_de_code_entry.delete(0, END)

	text_bin_revers = result_de_coding_entry.get()

	if len(text_bin_revers) / 8:
		iteration_on_dlobal = 0
		
		mass = ""
		list_itt = {"11000000": "А", 
				"11000001":"Б",
				"11000010":"В",
				"11000011":"Г",
				"11000100":"Д",
				"11000101":"Е",
				"11000110":"Ж",
				"11000111":"З",
				"11001000":"И",
				"11001001":"Й",
				"11001010":"К",
				"11001011":"Л",
				"11001100":"М",
				"11001101":"Н",
				"11001110":"О",
				"11001111":"П",
				"11010000":"Р",
				"11010001":"С",
				"11010010":"Т",
				"11010011":"У",
				"11010100":"Ф",
				"11010101":"Х",
				"11010110":"Ц",
				"11010111":"Ч",
				"11011001":"Щ",
				"11011000":"Ш",
				"11011100":"Ь",
				"11011011":"Ы",
				"11011010":"Ъ",
				"11011101":"Э",
				"11011110":"Ю",
				"11011111":"Я"
				}

		while iteration_on_dlobal < len(text_bin_revers):
			iteration_on_8_elements = 0
			otvet = ""

			while iteration_on_8_elements < 8:
				otvet = otvet + text_bin_revers[iteration_on_dlobal+iteration_on_8_elements]
				iteration_on_8_elements += 1

			otvet_result = list_itt[otvet]
			mass = mass + otvet_result 
			iteration_on_dlobal += 8

		bin_de_code_entry.insert(0, mass)
	else:
		messagebox.showinfo("GUI Python", "Error... \nнет значения")



if __name__ == '__main__':
	print("*"*37,"\n","*"*6+"Cripto progect work Tioma"+"*"*6,"\n","*"*37)
	print("программа активна")

	root = Tk()
	root.title("GUI на Python")
	root.geometry("850x360")

	name = StringVar()
	gamma_1 = StringVar()
	gamma_2 = StringVar()
	gamma_3 = StringVar()
	bin_name = StringVar()
	result_coding = StringVar()
	result_de_coding = StringVar()
	bin_de_code = StringVar()

	label = Label(text="Программа на кодирование XOR")
	gamma_1_label = Label(text="Введите гамму 1: ")
	gamma_2_label = Label(text="Введите гамму 2: ")
	gamma_3_label = Label(text="Введите гамму 3: ")
	name_label = Label(text="введи имя: ")
	bin_name_label = Label(text="введи bin код: ")
	result_coding_label = Label(text="результат кодирования: ")
	result_de_coding_lable = Label(text="результат декодирования: ")
	bin_de_code_lable = Label(text="bin dacod: ")

	label.grid(row=0, column=2, sticky="w")
	gamma_1_label.grid(row=1, column=1, sticky="w")
	gamma_2_label.grid(row=2, column=1, sticky="w")
	gamma_3_label.grid(row=3, column=1, sticky="w")
	name_label.grid(row=5, column=0, sticky="w")
	bin_name_label.grid(row=5, column=2, sticky="w")
	result_coding_label.grid(row=7, column=0, sticky="w")
	result_de_coding_lable.grid(row=7, column=2, sticky="w")
	bin_de_code_lable.grid(row=10, column=2, sticky="w")

	name_entry = Entry(textvariable=name)
	gamma_1_entry = Entry(textvariable=gamma_1)
	gamma_2_entry = Entry(textvariable=gamma_2)
	gamma_3_entry = Entry(textvariable=gamma_3)
	bin_name_entry = Entry(textvariable=result_coding, width="30")
	result_coding_entry = Entry(textvariable=result_coding, width="30")
	result_de_coding_entry = Entry(textvariable=result_de_coding, width="30")
	bin_de_code_entry = Entry(textvariable=bin_de_code, width="30")
	# result_coding_entry = Entry(textvariable=message)

	gamma_1_entry.grid(row=1,column=2, padx=5, pady=5)
	gamma_2_entry.grid(row=2,column=2, padx=5, pady=5)
	gamma_3_entry.grid(row=3,column=2, padx=5, pady=5)
	name_entry.grid(row=5,column=1, padx=5, pady=5)
	bin_name_entry.grid(row=5,column=3, padx=5, pady=5)
	result_coding_entry.grid(row=7,column=1, padx=5, pady=5)
	result_de_coding_entry.grid(row=7,column=3, padx=5, pady=5)
	bin_de_code_entry.grid(row=10,column=3, padx=5, pady=5)


	# вставка начальных данных
	name_entry.insert(0, "мав")
	gamma_1_entry.insert(0, "ока")
	gamma_2_entry.insert(0, "схи")
	gamma_3_entry.insert(0, "бин")


	display_button = Button(text="шифровать", 
					background="#555",		# фоновый цвет кнопки
					foreground="#ccc",		# цвет текста
					padx="30",				# отступ от границ до содержимого по горизонтали
					pady="10",				# отступ от границ до содержимого по вертикали
					font="16",				# высота шрифта
					command=get_coding_xor
					)

	clear_button = Button(text="дешифровать", 
					background="#555",
					foreground="#ccc",
					padx="30",
					pady="10",
					font="16",
					command=get_incoding_xor
					)

	de_cod_button = Button(text="дешифровать", 
					background="#555",
					foreground="#ccc",
					padx="30",
					pady="10",
					font="16",
					command=get_de_cod_bin_in_text
					)
	clear_cod_button = Button(text="ОЧИСТИТЬ ВСЁ", 
					background="#900",
					foreground="#ccc",
					padx="30",
					pady="10",
					font="16",
					command=get_clear_cod
					)

	display_button.grid(row=6, column=1, padx=5, pady=5, sticky="e")
	clear_button.grid(row=6, column=3, padx=5, pady=5, sticky="e")
	de_cod_button.grid(row=8, column=3, padx=5, pady=5, sticky="e")
	clear_cod_button.grid(row=10, column=1, padx=5, pady=5, sticky="e")

	root.mainloop()
	print("*"*37,"\n","*"*7+"clouse consol programm"+"*"*7,"\n","*"*37)
