class Examen:
	def __init__(self, nombre_del_curso):
		"""
			se inicializa el objeto examen con el titulo del curso
		"""
		self.nombre_del_curso = nombre_del_curso

	def add_question(self, question ,answer):
		"""
			recive dos strings una pregunta y una respuesta, se agrega al directorio de preguntas
		"""
		self.questions[question] = (answer, True)

	def set_false_answer(self,question):
		"""
			recibe una pregunta y actualiza si es correcta o no la respuesta
		"""
		self.questions[question] = (self.questions[question][0], False)

	def answer_to_question(self,question):
		"""
			recibe una pregunta y regresa la respuesta registrada
		"""
		return self.questions[question]

	def load_test_form_file(self):
		"""
			carga las preguntas, sus respuestas y la validez de las respuestas de el archivo nombre_del_curso.txt
		"""
		file = open(f"{self.nombre_del_curso}.txt","r")
		for line in file.readlines():
			valores = line.split()
			self.questions[valores[0]] = (valoes[1],valores[2])
		file.close()

	def save_test_to_file(self):
		"""
			guarda las pregunas, respuesta y validez de las respuestas al archivo nombre_del_curso.txt 
		"""
		file = open(f"{self.nombre_del_curso}.txt","w")

		for question in self.questions.keys():
			respuesta_esatus = self.questions[question]
			file.write(f"{question} {respuesta_esatus[0]} {respuesta_esatus[1]}")
			
		file.close()

