import sys

#eu_weights = [9, 8, 7, 6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
eu_weights = [8, 7, 6, 5, 4, 3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
eu_values = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, 
    "H": 8, "I": "9", "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, 
    "O": "6", "P": 7, "Q": "8", "R": 9, "S": 2, "T": 3, "U": 4, 
    "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9
}

"""
na_weights = [8, 7, 6, 5, 4, 3, 2, 10, 9, 8, 7, 6, 5, 4, 3, 2]
na_values = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, 
    "H": 8, "I": "", "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, 
    "O": "", "P": 7, "Q": "", "R": 9, "S": 2, "T": 3, "U": 4, 
    "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9
}
"""

# test vin:     w a u z z z 8 v 4 l a 0 5 5 8 1 0
# values:       6 1 4 9 9 9 8 5 _ 3 1 0 5 5 8 1 0
# weights:      8 7 6 5 4 3 2 10_ 9 8 7 6 5 4 3 2
# product:      54 8 28 54 45 36 24 10 27 8 0 30 25 32 3 0
# sum:          384
# reminder:     10

def mapValues(l_vin, loc_values):
    res = []

    for i in l_vin:
        if i.isdigit():
            res.append(i)
        else:
            res.append(loc_values[i])
    return res

def mapWeights(loc_weights):
    res = list(map(int, loc_weights))
    res = [int(x) for x in res]

def validateVIN(s_vin):
    s_vin = s_vin.upper()

    if len(s_vin) is not 17:
        print("[*] Invalid VIN. Length must be 17 but was {}.".format(len(s_vin)))
        sys.exit("[*] Exit program.")

    l_vin = list(s_vin)
    l_vin_org = list(s_vin)         # copy for later
    l_vin.pop(8)                    # remove checksum

    l_values_res = []

    l_values_res = mapValues(l_vin, eu_values)
    l_values_res = [int(x) for x in l_values_res]

    # calculate checksum
    sum_products = sum([a*b for a,b in zip(l_values_res, eu_weights)])

    reminder = sum_products % 11
    if reminder == 10:
        l_vin.insert(8, 'X')
    else:
        l_vin.insert(8, str(reminder))
    
    if l_vin == l_vin_org:
        print("[*] The VIN {} is valid.".format(''.join(l_vin_org)))
    else:
        print("[*] The VIN {} is invalid.".format(''.join(l_vin_org)))