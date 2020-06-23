class Examen:
	def __init__(self, nombre_del_curso):
		"""
			se inicializa el objeto examen con el titulo del curso
		"""
		self.nombre_del_curso = nombre_del_curso
		self.questions = {}

	def add_question(self, question ,answer):
		"""
			recive dos strings una pregunta y una respuesta, se agrega al directorio de preguntas
		"""
		self.questions[question] = (answer, True)

	def set_answer_stats(self,question):
		"""
			recibe una pregunta y actualiza si es correcta o no la respuesta
		"""
		try:
			self.questions[question] = (self.questions[question][0], not self.questions[question][1])
		except:
			print(f" set_answer_stats No existe la pregunta {question}")

	def answer_to_question(self,question):
		"""
			recibe una pregunta y regresa la respuesta registrada
		"""
		try:
			print(self.questions[question])
		except:
			print(f" answer_to_question No existe la pregunta {question}")

	def load_test_form_file(self):
		"""
			carga las preguntas, sus respuestas y la validez de las respuestas de el archivo nombre_del_curso.txt
		"""
		file = open(f"Tests/{self.nombre_del_curso}.txt","r")
		lines = file.readlines()
		for i in range(len(lines)):
			
			valores = lines[i].split(',')
			self.questions[valores[0]] = (valores[1],bool(valores[2]))
		file.close()

	def see_answer(self,question):
		"""
			recibe una pregunta y muestra su respuesta y su validez
		"""
		try:
			print(self.questions[question])
		except:
			print(f" see_answer No existe la pregunta {question}")
	def show_questions(self):
		"""
			muestra todas las preguntas sin su respuesta
		"""
		i = 0
		keys = self.questions.keys()
		if len(keys) > 0 :
			for key in keys:
				print(f"{i}.-{key} {self.questions[key][0]} {self.questions[key][1]}")
				i = i + 1
		else:
			print("aun no hay preguntas agregadas")
		return i

	def save_test_to_file(self):
		"""
			guarda las pregunas, respuesta y validez de las respuestas al archivo nombre_del_curso.txt 
		"""
		file = open(f"Tests/{self.nombre_del_curso}.txt","w")

		for question in self.questions.keys():
			respuesta_esatus = self.questions[question]
			file.write(f"{question},{respuesta_esatus[0]},{respuesta_esatus[1]},\n")
			
		file.close()
		print(f"Examen {self.nombre_del_curso} guardado en archivo")

