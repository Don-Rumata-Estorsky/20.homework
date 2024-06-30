"""
реализация класса book с атрибутами и методами ввода и вывода
"""

class Book:
  def __init__(self, name, year, izdatel, typee, autor, cost):
    self.name = name
    self.year = year
    self.izdatel = izdatel
    self.typee = typee
    self.autor = autor
    self.cost = cost

class book(Book):
    def __init__(self, name, year, izdatel, typee, autor, cost):
        super().__init__( name, year, izdatel, typee, autor, cost)      

    def name1(self):
        return f"{self.name}"

    def year1(self):
        return f"{self.year}"
    
    def izdatel1(self):
        return f"{self.izdatel}"
        
    def typee1(self):
        return f"{self.typee}"

    def autor1(self):
        return f"{self.autor}"
    
    def cost1(self):
        return f"{self.cost}"

    def input_data(self):
     self.name = input("Введите название книги: ")
     self.year = int(input("Введите год выпуска: "))
     self.izdatel = input("Введите  издателя: ")
     self.typee = input("Введите жанр: ")
     self.autor = input("Введите автора: ")
     self.price = input("Введите цену: ")
     print("")

if __name__ == "__main__":

    vvod=(int(input("Нажмите 1 для просмотра имеющихся книг, а для внесения нажмите 2 : ")))
    print("")
    if vvod == 1 :
     model = book("Трудно быть богом", 1963, "АТС" , "научная фантастика", "Братья Стругатские", 500)
     print("Книга: ",model.name1())
     print("год выпуска: ",model.year1())
     print("Издатель: ",model.izdatel1())
     print("Жанр: ",model.typee1())
     print("Автор: ",model.autor1())
     print("цена: ",model.cost1())
     print("")

    else:
     new_model = book("", 0, "", "", "", 0)
     new_model.input_data()
     print("Книга: ",new_model.name1())
     print("год выпуска: ",new_model.year1())
     print("Издатель: ",new_model.izdatel1())
     print("Жанр : ",new_model.typee1())
     print("Автор: ",new_model.autor1())
     print("цена: ",new_model.cost1())
     print("")
