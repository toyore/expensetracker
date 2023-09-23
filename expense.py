class Expense:
   def __init__(self, name, category, amount) -> None:
      self.name = name
      self.category = category
      self.amount = amount

#a default function that tells us how to represent a string when we are trying to  
# print it out
   def __repr__(self):
     return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
   
    