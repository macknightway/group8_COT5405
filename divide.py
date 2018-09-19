
def div(divisor, dividend):
    #Set the Quotient to 0
    quotient = 0

    divisor = align_msb(divisor)
    dividend = align_msb(dividend)

    while len(dividend) >= len(divisor):
        if len(dividend) == len(divisor):
            for i in range(len(dividend)):
                dividend_bit = dividend[i]
                divisor_bit = divisor[i]
                if dividend_bit < divisor_bit:
                    # We're done!
                    return quotient
                elif dividend_bit >= divisor_bit:
                    # Not done yet!
                    break
        # If dividend >= divisor -> add 1
        quotient += 1

        # Subtract divisor from dividend
        dividend = align_msb(sub(dividend, divisor))

    return quotient

def align_msb(bin_data):
    length = len(bin_data)
    for i in range(length):
        if bin_data[0] != '1':
            #Shift <- left
            bin_data = bin_data[1:]
        else:
            break
    return bin_data

def bit_flip(bin_data):
    flipped_data = ''
    for i in range(len(bin_data)):
        if bin_data[-(i+1)] == '0':
            flipped_data = '1' + flipped_data
        else:
            if (i+1) == len(bin_data):
                # We are at the msb
                flipped_data = '0' + flipped_data
            else:
                # We are not at the msb (make sure to keep all leftmost bits)
                flipped_data = bin_data[:-(i+1)] + '0' + flipped_data
                break
    return flipped_data

def sub(dividend, divisor):
    # Dividend: 1011 -> 11
    # Divisor:   100 -> 4
    # Answer: 111 -> 7
    result = ''
    length = len(dividend)
    for i in range(length - len(divisor)):
        divisor = '0' + divisor
    for i in range(length):
        if dividend[-1] == '1' and divisor[-1] == '0':
            result = '1' + result
        elif dividend[-1] == '0' and divisor[-1] == '0':
            result = '0' + result
        elif dividend[-1] == '1' and divisor[-1] == '1':
            result = '0' + result
        elif dividend[-1] == '0' and divisor[-1] == '1':
            #Note that for us to be in this function there must exist
            #at least one 1 in the dividend string to borrow from
            dividend = bit_flip(dividend)
            result = '1' + result
        dividend = dividend[:-1]
        divisor = divisor[:-1]
    return result

if __name__ == '__main__':
    import json

    with open('inputs.json') as json_data:
        data = json.load(json_data)
        sizes = data.keys()
        #for size in sizes:
        size = 'size_16'
        divisors = data[size]['divisor']
        dividends = data[size]['dividend']
        for divisor in divisors:
            for dividend in dividends:
                print('{0} divided by {1} = {2}'.format(int(dividend,2), int(divisor,2), div(divisor, dividend)))