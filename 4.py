def divideAndSort(numInt):
    string = str(numInt)
    i = 0
    # menyimpan bilangan setelah diurutkan
    integer = ""

    while i < len(string):
        if string[i] == '0':
            i += 1
        else:
            arrayTemp = []
            j = i
            while j < len(string):
                if string[j] == '0':
                    break
                else:
                    arrayTemp.append(int(string[j]))
                    j += 1
            arrayTemp.sort()
            for k in range(0,len(arrayTemp)):
                integer += str(arrayTemp[k])
            x = j-i # biar tidak out of index
            i += x

    print(int(integer))

divideAndSort(5956560159466056)

# source:
# -https://www.journaldev.com/23689/python-string-append
# -https://realpython.com/convert-python-string-to-int/
