
def div(a, b):
    #Set the Quotient to 0 (empty string '')
    quotient = ''

    divisor = a
    dividend = b

    while dividend >= divisor:

        # If dividend >= divisor -> shift 1
        quotient += '1'

        # Subtract divisor from dividend
        dividend = sub(dividend, divisor)

        # Shift divisor -> right one
        dividend = dividend[1:]

    else:
        # If dividend < divisor -> shift 0
        quotient += '0'
        break

def sub(dividend, divisor):
    pass


if __name__ == '__main__':
    a = 10
    b = 01
    #div(a, b)