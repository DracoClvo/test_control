class Pregunta:
	def __init__(self,pregunta_string,respuesta):
		"""
		crea la pregunta con una respuesta 
		"""
		self.pregunta_string = pregunta_string
		self.respuesta = respuesta

	def set_validez_respuesta(self,validez):
		""" 
			se resive si la pregunta fue correcta (true) o incorrecta (false)
		"""
		self.validez = validez

	def get_validez_respuesta(self):
		"""
			regresa el estado de la respuesta true si es correcta o false si no 
		"""
		return self.validez
