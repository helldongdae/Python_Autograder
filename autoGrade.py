import subprocess
inp = open("input.txt", 'r')
ans = open("output.txt", 'r')
stu = open("stunum.txt", 'r')
result = open("result.txt", 'w')
exp_answers = ans.readlines()
students = stu.readlines()
line = inp.readlines()
for stunum in students:
    isCorrect = True
    stunum = stunum.rstrip('\n')
    filename = "python " + "hws/"  + stunum + ".py"
    p = subprocess.Popen(filename, stdout = subprocess.PIPE, stdin = subprocess.PIPE, universal_newlines=True)
    for i in line:
        p.stdin.write(i)
    p.stdin.close()
    for ans_exp in exp_answers:
        ans_out = p.stdout.readline()
        ans_out = ans_out.rstrip('\n')
        if ans_out != ans_exp.rstrip('\n'):
            isCorrect = False
    if isCorrect == True:
        result.write(stunum + " Correct\n")
    else:
        result.write(stunum + " Wrong\n")
inp.close()
ans.close()
stu.close()
result.close()
print("Done")
