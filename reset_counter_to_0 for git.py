#resets text file counter back to 0, press alt + x when autohotkey script is loaded

h = open(r"C:\Users\nharw\Desktop\Screenshot Project\permacounter test.txt", "r")
num = h.read()
num = int(num)
num = 0
j = open(r"C:\Users\nharw\Desktop\Screenshot Project\permacounter test.txt", "w")
#print(num) #This line is not needed, can use it to bug test
j.write(f"{num}")
j.close()
