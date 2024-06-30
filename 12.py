"""
реализация класса Stadion с атрибутами и методами ввода и вывода
"""

class Stad:
  def __init__(self, name, year, count, city, big, ):
    self.name = name
    self.year = year
    self.count = count
    self.city = city
    self.big = big

class stad(Stad):
    def __init__(self, name, year, count, city, big, ):
        super().__init__( name, year, count, city, big, )      

    def name1(self):
        return f"{self.name}"

    def year1(self):
        return f"{self.year}"
    
    def count1(self):
        return f"{self.count}"
        
    def city1(self):
        return f"{self.city}"

    def big1(self):
        return f"{self.big}"
    


    def input_data(self):
     self.name = input("Введите название Стадиона: ")
     self.year = int(input("Введите год постройки: "))
     self.count = input("Введите Страну: ")
     self.city = input("Введите Город: ")
     self.big = int(input("Введите Вместительность: "))
     print("")

if __name__ == "__main__":

    vvod=(int(input("Нажмите 1 для просмотра имеющихся Стадионов, а для внесения нажмите 2 : ")))
    print("")
    if vvod == 1 :
     model = stad("Yanky Stadion", 1979, "USA", "NEW_YORK!", 1000000 )
     print("Название стадиона: ",model.name1())
     print("год постройки: ",model.year1())
     print("Страна: ",model.count1())
     print("Город: ",model.city1())
     print("Вместительность: ",model.big1())
     print("")

    else:
     new_model = stad("", 0, "", "", 0)
     new_model.input_data()
     print("Название стадиона: ",new_model.name1())
     print("год постройки: ",new_model.year1())
     print("Страна: ",new_model.count1())
     print("Город : ",new_model.city1())
     print("Вместительность: ",new_model.big1())
     print("")
