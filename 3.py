def createTri(n):
    for i in range(n):
        count = 0
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
            if count<i:
                print("*",end=" ")
                count += 1
        print("\r")

createTri(5)

# source: https://www.youtube.com/watch?v=TdgoIdDvGIw
