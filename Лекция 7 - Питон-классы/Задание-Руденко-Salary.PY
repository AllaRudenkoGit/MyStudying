class employee:
  def __init__(self,id,name,position,base_salary):
    self.id=id
    self.name=name
    self.position=position
    self.base_salary=base_salary
  def calculate_salary(self,base_salary):
    self.base_salary=base_salary
    return final_salary
class manager(employee):
  def __init__(self,id,position,base_salary,bonus):
    super.__init__(id,name,position,base_salary)
    self.bonus=bonus
  def calculate_final_salary(self):
    final_salary=base_salary+bonus
    print("Зарплата менеджера:",final_salary)
class developer(employee):
  def __init__(self,id,position,hourly_rate,hours_worked):
    super.__init__(self,id,position)
    self.hourly_rate=hourly_rate
    self.hours_worked=hours_worked
  def calculate_final_salary(self):
    final_salary=hourly_rate*hours_worked
    print("Зарплата девелопера:",final_salary)
class intern(employee):
  def __init__(self,id,position,base_salary):
    super.__init__(self,id,position,base_salary)
  def calculate_final_salary(self):
    final_salary=base_salary/2
    print("Зарплата стажера:",final_salary)
