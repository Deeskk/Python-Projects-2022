def main():
    print ("This program converts us dollars to pounds sterling")
    print ("")
    while True:
        dollars= eval(input("Enter amount in dollars: "))
        pounds = convert_to_pounds(dollars)
        print ("that is", pounds, "pounds")

convert_to_pounds = lambda dollars: dollars* 0.82
main()