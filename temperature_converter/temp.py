import sys

def convert_temp(celsius):
    fahre = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahre, kelvin

if __name__ == "__main__":        
    celsius = float(sys.argv[1])
    f, k = convert_temp(celsius)

    print(f"Фаренгейт: {f}")
    print(f"Кельвин: {k}")
