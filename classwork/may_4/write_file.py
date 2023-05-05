def main():
    write()
    read_all()
    read_lines()

def write():
    outfile = open(r'C:/Users/Owner/Desktop/Programming Concepts/python practice/classwork/may_4/test.txt', 'w')

    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    outfile.write('Ayn Rand\n')

    outfile.close()

def read_all():
    infile = open('philosophers.txt', 'r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)

def read_lines():
    infile = open('philosophers.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()

    print(line1 + "\n" + line2 + "\n" + line3 + '\n' + line4)

main()