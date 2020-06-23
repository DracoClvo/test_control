examenes = []
from examen import Examen

def carge_tests_names():
	file = open("test.txt","w")
	for line in file.readlines():
		examenes.append(line)

def charge_test(test_name):
	return Examen(test_name)

def main_menu_options():
	return int(input( "\t Menu\n0.-Salir\n1.-Listar examenes\n2.-Elejir examen\n3.-Agregar Examen\n: "))

def examen_options():
	return int(input( "\t\t4.-Agregar preguntas\n\t\t5.-Consultar respuestas\n\t\t6.-Actualizar estatus respuestas\n\t\t7.-Regresar\n: "))


def examen_menu_acctions(seted_test,opcion):
	if opcion == 4:
		add_questions_to_test(seted_test)
	elif opcion == 5:
		check_answers(seted_test)
	elif opcion == 6:
		update_question_status(seted_test)
	elif opcion == 7:
		print("regresando menu principal...")
	else:
		print(f"Opcion {opcion} no valida")

def add_questions_to_test(seted_test):
	question = ""
	while (not (question == "fin")):
		question = input("Pregunta: ")
		if (not(question  == "fin")):
			aswer = input("Respuesta: ")
			seted_test.add_question(question,aswer)
		else:
			print(":D")

def check_answers(seted_test):
	opcion = ""
	while (opcion != -1 ):
		no_questions = seted_test.show_questions()
		opcion = int(input(": "))
		if (opcion >= 0 and opcion < no_questions):
			seted_test.see_answer(opcion)



def update_question_status(seted_test):
	opcion = ""
	while (opcion != -1 ):
		no_questions = seted_test.show_questions()
		opcion = int(input(": "))
		if (opcion > 0 and opcion < no_questions):
			seted_test.set_answer_stats(opcion)

	
def examen_menu(seted_test):
	opcion = 0
	while(opcion != 7):
		opcion = examen_options()
		examen_menu_acctions(seted_test,opcion)


def main_menu_acctions(opcion):
	if(opcion == 0):
		print("adios :D")
	elif(opcion == 1):
		mostrar_titulos_examenes()		
	elif(opcion == 2):
		set_test()		
	elif(opcion == 3):
		add_new_test()
	else:
		print(f"opcion {opcion} no valida")

def mostrar_titulos_examenes():
	no_test = len(examenes)
	if no_test > 0 :
		for i in range(len(no_test)):
			print(f"{i}.-{examenes[i]}")
	else:
		print("aun no hay examenes registrados")

def set_test():
	if len(examenes) > 0:
		indice_examen_selecionado = int(input("numero de examen: "))
		examen = Examen(examenes[indice_examen_selecionado])
		examen.load_test_form_file()
		examen_menu(examen)
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


if __name__ == "__main__":
	main_menu()



	