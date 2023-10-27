def lot():
 while True:
  x = int(input("Na jakiej wysokości lecimy? (w metrach): "))
  y = 5000 - x
  if x < 5000:
     print("Lecisz",(y / 1000),"km za nisko!")
     continue
  else:
     print("Na tej wysokości jesteś już bezpieczny!")
     break

lot()


