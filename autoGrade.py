import subprocess
from tkinter import *

t = Tk()
inputFileName = "NONE"
outputFileName = "NONE"
studentIDFileName = "NONE"
init = True
def askInputFile():
    global inputFileName
    t.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("text files","*.txt"),("all files","*.*")))    
    inputFileName = t.filename
    nameOfInputFile.set(inputFileName)
    
def askOutputFile():
    global outputFileName
    t.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("text files","*.txt"),("all files","*.*")))    
    outputFileName = t.filename
    nameOfOutputFile.set(outputFileName)

def askStuIDFile():
    global studentIDFileName
    t.filename =  filedialog.askopenfilename(initialdir = "E:/Images",title = "choose your file",filetypes = (("text files","*.txt"),("all files","*.*")))    
    studentIDFileName = t.filename
    nameOfStunumFile.set(studentIDFileName)

def autoGrade():
    global init, inputFileName, outputFileName, studentIDFileName
    if inputFileName == "NONE" :
        messagebox.showinfo( "WARNING", "No input file given")
        return
    if outputFileName == "NONE" :
        messagebox.showinfo( "WARNING", "No output file given")
        return
    if studentIDFileName == "NONE": 
        messagebox.showinfo( "WARNING", "No student id file given")
        return
    inp = open(inputFileName, 'r')
    ans = open(outputFileName, 'r')
    stu = open(studentIDFileName, 'r')
    result = open("result.txt", 'w')
    exp_answers = ans.readlines()
    students = stu.readlines()
    line = inp.readlines()
    solution = ""
    for i in exp_answers:
        solution+=i
    for stunum in students:
        isCorrect = True
        stunum = stunum.rstrip('\n')
        filename = "python " + "hws/"  + stunum + ".py"
        p = subprocess.Popen(filename, stdout = subprocess.PIPE, stdin = subprocess.PIPE, universal_newlines=True)
        s = ""
        for i in line:
            s += i
        try:
            q = p.communicate(s, timeout = 1)
        except subprocess.TimeoutExpired:
            result.write(stunum + " Time Out\n")
            p.kill()
            continue
        if solution == q[0]:
            result.write(stunum + " Correct\n")
        else:
            result.write(stunum + " Wrong\n")
    inp.close()
    ans.close()
    stu.close()
    result.close()
    print("Done")
    
inputBtn = Button(t, text = "Provide Input", command = askInputFile)
label = Label(t, text = "Input file name")
nameOfInputFile = StringVar()
label2 = Label(t, textvariable = nameOfInputFile , relief = RAISED)
nameOfInputFile .set("NONE")

nameOfOutputFile = StringVar()
label3 = Label(t, text = "Output file name")
label4 = Label(t, textvariable = nameOfOutputFile , relief = RAISED)
nameOfOutputFile.set("NONE")
outputBtn = Button(t, text = "Provide Output", command = askOutputFile)

nameOfStunumFile = StringVar()
label5 = Label(t, text = "Stunum file name")
label6 = Label(t, textvariable = nameOfStunumFile , relief = RAISED)
nameOfStunumFile.set("NONE")
stunumBtn = Button(t, text = "Provide StudentIDs", command = askStuIDFile)

calcBtn = Button(t, text = "Calculate", command = autoGrade)

label.grid(row = 0, column = 0)
label2.grid(row = 0, column = 1)
inputBtn.grid(row = 1, column = 0)

label3.grid(row = 2, column = 0)
label4.grid(row = 2, column = 1)
outputBtn.grid(row = 3, column = 0)

label5.grid(row = 4, column = 0)
label6.grid(row = 4, column = 1)
stunumBtn.grid(row = 5, column = 0)

calcBtn.grid(row = 7, column = 0)
t.mainloop()