"""
реализация класса car с атрибутами и методами ввода и вывода
"""

class Car:
  def __init__(self, model, year, brand, dvij, color, cost):
    self.model = model
    self.year = year
    self.brand = brand
    self.dvij = dvij
    self.color = color
    self.cost = cost

class car(Car):
    def __init__(self, model, year, brand, dvij, color, cost):
           super().__init__( model, year, brand, dvij, color, cost)      

    def model1(self):
        return f"{self.model}"

    def year1(self):
        return f"{self.year}"
    
    def brand1(self):
        return f"{self.brand}"
        
    def dvij1(self):
        return f"{self.dvij}"

    def color1(self):
        return f"{self.color}"
    
    def cost1(self):
        return f"{self.cost}"

    def input_data(self):
     self.model = input("Введите название модели: ")
     self.year = int(input("Введите год выпуска: "))
     self.brand = input("Введите производителя: ")
     self.dvij = float(input("Введите объем двигателя: "))
     self.color = input("Введите цвет: ")
     self.price = float(input("Введите цену: "))
     print("")

if __name__ == "__main__":

    vvod=(int(input("Нажмите 1 для просмотра имеющихся машин, а для внесения нажмите 2 : ")))
    print("")
    if vvod == 1 :
     model = car("lada", 1990, "AutoVAZ" ,325, "white", 25000)
     print("модель: ",model.model1())
     print("год выпуска: ",model.year1())
     print("бренд: ",model.brand1())
     print("объем двигателя: ",model.dvij1())
     print("цвет: ",model.color1())
     print("цена: ",model.cost1())
     print("")

    else:
     new_model = car("", 0, "", 0, "", 0)
     new_model.input_data()
     print("модель: ",new_model.model1())
     print("год выпуска: ",new_model.year1())
     print("бренд: ",new_model.brand1())
     print("объем двигателя: ",new_model.dvij1())
     print("цвет: ",new_model.color1())
     print("цена: ",new_model.cost1())
     print("")
