class Cat:
  """ Define the Student """
  def __init__(self, name, year_of_birth):
    """Initialize the student"""
    self.name = name
    self.year = year_of_birth

  def century(self):
    """ Caculate the student century based on their year of birth"""
    if self.year < 2000:
      return "20th"
    else:
      return "21st"

  def welcome(self):
    """ Return a welcome message """
    return f"Wecome {self.name}, you were born in the {self.century()} century"
  

luiza = Cat("Luiza", 2005)
print(luiza.welcome())