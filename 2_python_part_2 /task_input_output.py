"""
Write function which reads a number from input nth times.
If an entered value isn't a number, ignore it.
After all inputs are entered, calculate an average entered number.
Return string with following format:
If average exists, return: "Avg: X", where X is avg value which rounded to 2 places after the decimal
If it doesn't exists, return: "No numbers entered"
Examples:
    user enters: 1, 2, hello, 2, world
    >>> read_numbers(5)
    Avg: 1.67
    ------------
    user enters: hello, world, foo, bar, baz
    >>> read_numbers(5)
    No numbers entered

"""



def read_numbers(n: int) -> str:
    total = 0
    count = 0

    for i in range(n):
        value = input("Enter a value: ")
        try:
            total = total+float(value)
            
            count+=1
        except ValueError :
            pass
    if total==0 and count==0:
        print("No numbers entered")
    average = total/count
    print(f'Avg: {round(average,2)}')

        

read_numbers(5)
       



