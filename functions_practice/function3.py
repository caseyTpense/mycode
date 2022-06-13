def oddoreven(x):
    if x % 2 == 0:
        return True
    else:
        return False
def main():
    num= int(input("choose a number: "))
    print(oddoreven(num))

main()
