class Airplane:
	def __init__(self, make,model,year,max_speed,odometr,is_flying=False):
		self.make=make
		self.model=model
		self.year=year
		self.max_speed=max_speed
		self.odometr=odometr
		self.is_flying=is_flying
	def take_off(self):
		if self.is_flying == True:
			print(f'Cамолёт {self.make}, модель которой {self.model} и выпущенный в {self.year} году')
	def land(self):
		if self.is_flying ==False:
			print(f'Cамолёт {self.make}, модель которой {self.model} и выпущенный в {self.year} году')
			print("Самолёт сейчас не в полёте")
	def fly(self):
		if self.is_flying == True:
			print(f'и с максимальной скоростью {self.max_speed} км/ч,пролетел около {self.odometr} км')

airplane=Airplane('Сухой','Sukhoi Superjet 100',2008,860,100000,True)
airplane.take_off()
airplane.land()
airplane.fly()