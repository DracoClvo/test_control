from examen import Examen


def test_add_question():
	examen = Examen("Test")
	examen.add_question("pregunta 1", "respuesta 1")
	examen.show_questions()

def test_show_questions():
	examen = Examen("Test")
	examen.show_questions()

def test_set_answer_stats():
	examen = Examen("Test")
	examen.add_question("pregunta 1", "respuesta 1")
	examen.add_question("pregunta 2", "respuesta 2")
	examen.add_question("pregunta 3", "respuesta 3")
	examen.set_answer_stats("pregunta 1")
	examen.set_answer_stats("pregunta 5")
	examen.show_questions()

def test_answer_to_question():
	examen = Examen("Test")
	examen.add_question("pregunta 1", "respuesta 1")
	examen.add_question("pregunta 2", "respuesta 2")
	examen.add_question("pregunta 3", "respuesta 3")
	examen.answer_to_question("pregunta 3")
	examen.answer_to_question("pregunta 4")

def test_save_test_to_file():
	examen = Examen("Test")
	examen.add_question("pregunta 1", "respuesta 1")
	examen.add_question("pregunta 2", "respuesta 2")
	examen.add_question("pregunta 3", "respuesta 3")
	examen.save_test_to_file()



def test_load_test_form_file():
	examen = Examen("Test")
	examen.load_test_form_file()
	examen.show_questions()



def test_see_answer():
	examen = Examen("Test")
	examen.add_question("pregunta 1", "respuesta 1")
	examen.add_question("pregunta 2", "respuesta 2")
	examen.add_question("pregunta 3", "respuesta 3")
	examen.see_answer("pregunta 1")
	examen.see_answer("pregunta 4")






print("\ntest de agregar preguntas")
test_add_question()
print("\ntest de mostrar preguntas")
test_show_questions()
print("\ntest de cambiar status")
test_set_answer_stats()
print("\ntest de mostrar la respuesta a pregunta x")
test_answer_to_question()
print("\ntest de guardar examen en archivo")
test_save_test_to_file()
print("\ntest de cargar examen de un archivo")
test_load_test_form_file()
print("\ntest de ver respuesta")
test_see_answer()