"""
VIN parser

Structure:
1. Validate VIN
2. Separate parts
3. Decode parts

CLI inputs:
- VIN
- Information to desire (e. g. model type, model year)

Resources:
- Country codes
- Manufacturer codes
- Vehicle type or devison codes
- Brand, body, style, engine, size and type, model serices, etc. codes
- Model year character codes
- Assembly plant codes

Functions:
- Vehicls production number (serial number) decoder
- Validation function -> Security check digit
- 1 function for each part of the VIN
- Brand, body, style, engine, size and type, model serices, etc. decoder

"""
import argparse
from validateVIN import validateVIN
from parseWmi import parseWmi
from parseModelYear import parseModelYear

# Parse arguments
def pars():
    parser = argparse.ArgumentParser()

    parser.add_argument('vin', type=str, help='Vehilce VIN')
    parser.add_argument('-v', '--validate', help='Validate VIN', action="store_true")
    parser.add_argument('-w', '--wmi', help='Get World Manufacturer Identifier from VIN', action="store_true")
    parser.add_argument('-y', '--year', help='Get model year.', action="store_true")

    args = parser.parse_args()

    if args.validate:
        validateVIN(args.vin)
    if args.wmi:
        parseWmi(args.vin)
    if args.year:
        parseModelYear(args.vin)


def main():
    pars()

if __name__ == '__main__':
    main()