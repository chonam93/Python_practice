inputFileName ='C:\\Users\\Admin\\Desktop\\Python_vs\\Python_hanyang\\employees.txt'
inputFile = open(inputFileName, 'r')

BONUS = 0.3
print('Reading from', inputFileName)

for line in inputFile:
    name, job, income = line.split(',')
    last, first = name.split(' ')
    income = int(income)
    income = income + (income * BONUS)
    print('name: ', last, first, '\t\t job: ', job, '\t\tIncome: ', income)

print('completed reading of file input.txt')
inputFile.close()
