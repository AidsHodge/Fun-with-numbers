  def main()
      print("Welcome to Fun With Numbers")
      print("Choose from the menu below")
      print(" (A)Check number features")
      print(" (B) Plot numbers")
      print(" (C) Check overall stats")
      print("\n (X) Save and exit")
      choice = input("/nChoice:").upper()

      if choice == "A":
          number feature ()
        elif choice == "B":
              plotter()
        elif choice == "C":
              stats()
        elif choice== "X":
            exit_flag = True
def number_features():
  """Displayes features of the chosen number."""
  print("This is the number features sub-routine")

def plotter():
  """Plotts numbers on a graph."""
  print("This is the plotter sub-routine")

def stats():
  """Displays statistics of numbers used in the program."""
  print("This is the stats sub-routine")

main()
