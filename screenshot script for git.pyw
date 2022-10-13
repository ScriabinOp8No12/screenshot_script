import pyautogui
import os.path
import datetime

#press alt + a when autohotkey is loaded to run this script
#The following 7 lines of code reads and writes to a text file (located on the desktop) to update the persistent counter!
g = open(r"C:\Users\nharw\Desktop\Screenshot Project\permacounter test.txt", "r")
num = g.read()
num = int(num)
num+=1
h = open(r"C:\Users\nharw\Desktop\Screenshot Project\permacounter test.txt", "w")
#print(num) #This line is not needed, can use it to bug test
h.write(f"{num}")
h.close()

#Change student_name to student name you want in file name before running program
student_name = "Aaron"
#datetime.date.today is in the format of year, month, day
todays_date = datetime.date.today()
file_name = student_name + " " + str(num) + " " + str(todays_date) + ".png"
#Takes screenshot of specific region of computer screen using pyautogui
my_screenshot = pyautogui.screenshot(region=(5, 97, 915, 921))
#Saves the screenshot to the specified folder, uses "r" to make it a raw string literal
#so that the \ (escape character) doesn't need to be written as \\ (\\ actually works too)
my_screenshot.save(rf'C:\Users\nharw\Desktop\Screenshot Project\Stored Screenshots\{file_name}')


