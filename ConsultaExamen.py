examenes = []
nombre_archivo = "examenes_guardados"
from examen import Examen

def carge_tests_names():
	file = open("test.txt","w")
	for line in file.readlines():
		examenes.append(line)

def charge_test(test_name):
	return Examen(test_name)

def main_menu_options():
	try: 
		return int(input( "\n\t Menu\n0.-Salir\n1.-Listar examenes\n2.-Elejir examen\n3.-Agregar Examen\n: "))
	except:
		return 10
def examen_options():
	try:
		return int(input( "\n\t\t4.-Agregar preguntas\n\t\t5.-Consultar respuestas\n\t\t6.-Actualizar estatus respuestas\n\t\t7.-Regresar\n\t\t: "))
	except:
		return 10

def examen_menu_acctions(seted_test,opcion):
	if opcion == 4:
		add_questions_to_test(seted_test)
	elif opcion == 5:
		check_answers(seted_test)
	elif opcion == 6:
		update_question_status(seted_test)
	elif opcion == 7:
		print("regresando menu principal...")
	elif opcion == 10:
		print("\t\tingrese una opcion")
	else:
		print(f"Opcion {opcion} no valida")

def add_questions_to_test(seted_test):
	question = ""
	print("agregar pregntas(regresar)")
	while (not (question == "regresar")):
		question = input("Pregunta: ")
		if (not(question  == "regresar")):
			aswer = input("Respuesta: ")
			seted_test.add_question(question,aswer)
		else:
			print(":D")

def check_answers(seted_test):
	opcion = ""
	print("revisar respuestas (regresar)")
	while not (opcion == "regresar"):
		opcion = input("pregunta(regresar): ")
		if not opcion == "regresar":
			seted_test.see_answer(opcion)


def update_question_status(seted_test):
	opcion = ""
	print("actualizar status de respuesta (regresar)")
	while not (opcion == "regresar"):
		opcion = input("pregunta(regresar): ")
		if not opcion == "regresar":
			seted_test.set_answer_stats(opcion)

	
def examen_menu(seted_test):
	opcion = 0
	while(opcion != 7):
		opcion = examen_options()
		examen_menu_acctions(seted_test,opcion)


def main_menu_acctions(opcion):
	if(opcion == 0):
		save_tests_to_file()
		print("adios :D")
	elif(opcion == 1):
		mostrar_titulos_examenes()		
	elif(opcion == 2):
		set_test()		
	elif(opcion == 3):
		add_new_test()
	elif opcion == 10:
		print("ingrese una opcion")
	else:
		print(f"opcion {opcion} no valida")

def mostrar_titulos_examenes():
	no_test = len(examenes)
	if no_test > 0 :
		for i in range(no_test):
			print(f"{i}.-{examenes[i]}")
	else:
		print("aun no hay examenes registrados")

def set_test():
	if len(examenes) > 0:
		try:
			indice_examen_selecionado = int(input("numero de examen: "))
			examen = Examen(examenes[indice_examen_selecionado])
			examen.load_test_form_file()
			examen_menu(examen)
		except:
			print("examen inexistente")
	else:
		print("aun no hay examenes registrados")

def add_new_test():
	test_name = input("como se llama el curso?\n:")
	examenes.append(test_name)
	examen = Examen(test_name)
	examen_menu(examen)
	examen.save_test_to_file()


def main_menu():
	opcion = 9
	isTestSeted = False
	while(opcion != 0):
		opcion =  main_menu_options()
		main_menu_acctions(opcion)

def load_Tests_from_file():
	try:
		file = open(f"{nombre_archivo}.txt","r")
		lines = file.readlines()
		for i in range(len(lines)):
			examenes.append(lines[i])
		file.close()
	except:
		print("Bienvenido aun no hay examenes agregados")

def save_tests_to_file():
	file = open(f"{nombre_archivo}.txt","w")
	for examen in examenes:
		file.write(f"{examen}\n")
		
	file.close()
	print(f"Examenes guardado en archivo")

if __name__ == "__main__":
	load_Tests_from_file()
	main_menu()





	