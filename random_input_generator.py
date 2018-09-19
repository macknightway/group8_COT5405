import random
import json


FILE_NAME = "inputs.json"


def get_random_bits_of_size(n):
    '''
    :param n: is the size of binary block
    :return: function returns every integer s (example '5') in binary block as '0b0101',
             where, if needed, every block is padded with leading '0' upto size n
             and 0b is preceded in every binary block
    '''
    s = random.randrange(0, 2**n)  # b is not inclusive in rand(a,b)
    return format(s, "0"+str(n)+'b')


def generate_inputs(num_of_inputs, list_of_size_of_inputs):
    '''

    :param num_of_inputs: is the total number of inputs needed in one array of either divisor or dividends
    :param list_of_size_of_inputs: is the array of different input size, eg:4bit, 8 bit, 16 bit and so on
    :return: function returns a dictionary of random inputs
    '''
    dict = {}
    for size_of_input in list_of_size_of_inputs:
        key = "size_{}".format(size_of_input)
        dict[key] = {"divisor":[],
                     "dividend":[]}
        for i in range(0, num_of_inputs):
            divisor = get_random_bits_of_size(size_of_input)
            dividend = get_random_bits_of_size(size_of_input)
            dict[key]["divisor"].append(divisor)
            dict[key]["dividend"].append(dividend)

    return dict

def write_to_file(content):
    with open(FILE_NAME, 'w') as f:
        f.write(content)


if __name__=="__main__":
    num_of_inputs = 1000
    list_of_size_of_inputs = [4, 8, 16, 32, 64, 128, 256, 512]

    dict_of_inputs = generate_inputs(num_of_inputs, list_of_size_of_inputs)
    write_to_file(json.dumps(dict_of_inputs, indent=4))
