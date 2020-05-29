import sys

dct_modelyear = {
    "1" : "2000",
    "2" : "2001",
    "3" : "2002",
    "4" : "2003",
    "5" : "2004",
    "6" : "2005",
    "7" : "2006",
    "8" : "2007",
    "9" : "2008",
    "A" : "2009",
    "B" : "2010",
    "C" : "2011",
    "D" : "2012",
    "E" : "2013",
    "F" : "2014",
    "G" : "2015",
    "H" : "2016",
    "J" : "2017",
    "K" : "2018",
    "L" : "2019",
    "M" : "2020",
    "N" : "2021",
    "P" : "2022",
    "R" : "2023",
    "S" : "2024",
    "T" : "2025",
    "V" : "2026",
    "W" : "2027",
    "X" : "2028",
    "Y" : "2029"
}

def parseModelYear(s_vin):
    s_vin = s_vin.upper()

    if len(s_vin) is not 17:
        print("[*] Invalid VIN. Length must be 17 but was {}.".format(len(s_vin)))
        sys.exit("[*] Exit program.")

    if s_vin[9] in dct_modelyear:
        print("[*] Modelyear is {}.".format(dct_modelyear[s_vin[9]]))
    else:
        print("[*] Modelyear is unkown. Vehicle is either older than 2000 or invalid.")