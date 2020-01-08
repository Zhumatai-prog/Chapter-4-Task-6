class House():
	def __init__(self, total_area):
		self.total_area = total_area

	def furniture(self, **kwargs):
		self.fur = kwargs.keys()
		self.area = kwargs.values()
		self.new_list =[i for i in self.fur]
		print(f"{self.total_area}m square - {self.total_area - sum(self.area)}m square left - {self.new_list}")


h1 = House(100)
h1.furniture(bed=4, shkaf=2, stol = 1.5)