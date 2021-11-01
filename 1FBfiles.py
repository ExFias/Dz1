    filename = "fizzbuzz.txt"
    file_io_wrapper = open(filename, "r")
    for line in file_io_wrapper:
        fizz, buzz, tazz = line.split()
        fizz = int(fizz)
        buzz = int (buzz)
        tazz = int (tazz)

        for i in range(1, tazz):
            if i % fizz and i % buzz:
                print('FB')
            elif i % buzz:
                print('B')
            elif i % fizz:
                print('F')
        else:
            print(i)

    file_io_wrapper.close()