def div(divisor, dividend):
    #Set the Quotient to 0
    quotient = 0
    is_negative = not (divisor[0] == dividend[0])
    if divisor[0] == '1':
        divisor = twos_complement(divisor)
    if dividend[0] == '1':
        dividend = twos_complement(dividend)
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
                elif dividend_bit == divisor_bit:
                    # Not done yet!
                    continue
                elif dividend_bit > divisor_bit:
                    # We can keep dividing
                    break
        # If dividend >= divisor -> add 1
        quotient += 1

        # Subtract divisor from dividend
        dividend = align_msb(sub(dividend, divisor))

    if is_negative:
        return -1 * quotient
    else:
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


def add_one(bin_data):
    result = ''
    length = len(bin_data)
    for i in range(length):
        if bin_data[-1] == '0':
            result = bin_data[:-1] + '1'
            break
        if bin_data[-1] == '1':
            i = -1
            while bin_data[i] == '1':
                result = '0' + result
                i -= 1
            else:
                if (abs(i) == length):
                    result = '1' + result
                else:
                    result = bin_data[:-i] + '1' + result
            break
    return result


def twos_complement(bin_data):
    twos_complement = ''
    for bin_digit in bin_data:
        if bin_digit == '0':
            twos_complement += '1'
        elif bin_digit == '1':
            twos_complement += '0'
    return add_one(twos_complement)

from memory_profiler import profile

@profile
def main():
    import json
    import time

    with open('inputs.json') as json_data:
        # x = div('0' + bin(2829)[2:], '0' + bin(23833)[2:])
        # y = 84861 / 92185
        data = json.load(json_data)
        sizes = data.keys()
        # for size in sizes:
        size = 'size_16'
        divisors = data[size]['divisor']
        dividends = data[size]['dividend']
        divisor_neg = False
        dividend_neg = False
        false_flag = False
        # Starting Timer
        start_time = time.time()
        for divisor in divisors:
            if divisor[2] == '1':
                divisor_neg = True
                printed_divisor = twos_complement(divisor)
            else:
                printed_divisor = divisor
            for dividend in dividends:
                if dividend[2] == '1':
                    dividend_neg = True
                    printed_dividend = twos_complement(dividend)
                else:
                    printed_dividend = dividend
                if divisor_neg and dividend_neg:
                    x = div(divisor, dividend)
                    print('-{0} divided by -{1} = {2}'.format(int(printed_dividend, 2),
                                                              int(printed_divisor, 2),
                                                              x))
                    y = int(int(dividend, 2) / int(divisor, 2))
                    if not (x == y):
                        false_flag = True
                elif divisor_neg and not dividend_neg:
                    x = div(divisor, dividend)
                    print('{0} divided by -{1} = -{2}'.format(int(printed_dividend, 2),
                                                              int(printed_divisor, 2),
                                                              x))
                    y = int(int(dividend, 2) / int(divisor, 2))
                    if not (x == y):
                        false_flag = True
                elif not divisor_neg and dividend_neg:
                    x = div(divisor, dividend)
                    print('-{0} divided by {1} = -{2}'.format(int(printed_dividend, 2),
                                                              int(printed_divisor, 2),
                                                              x))
                    y = int(int(dividend, 2) / int(divisor, 2))
                    if not (x == y):
                        false_flag = True
                else:
                    x = div(divisor, dividend)
                    print('{0} divided by {1} = {2}'.format(int(printed_dividend, 2),
                                                            int(printed_divisor, 2),
                                                            x))
                    y = int(int(dividend, 2) / int(divisor, 2))
                    if not (x == y):
                        false_flag = True
        if not false_flag:
            print('All TEST CASES PASSED')
    # End of Timer
    elapsed_time = time.time() - start_time
    print('Time Elapsed: {0}'.format(elapsed_time))

    # Potential way of doing this on a Linux Machine
    # print(resources.getrusage(resources.RUSAGE_SELF).ru_maxrss)


if __name__ == '__main__':
    main()
