class ContactoAgenda:
	name=""
	surname=""
	city=""
	phone=""

	def __init__(self,name,surname,city,phone):
		self.name=name
		self.surname=surname
		self.city=city
		self.phone=phone
    
	def getName(self):
		return self.name
	def getSurname(self):
		return self.surname
	def getCity(self):
		return self.city
	def getPhone(self):
		return self.phone
	def __str__(self):
		return self.name + self.surname + self.city + self.phone
