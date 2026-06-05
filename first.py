import sys

def tr(list):
    return min(list), max(list), sum(list) / len(list)

if __name__ == "__main__":
    numbers = [float(x) for x in sys.argv[1:]]
    mn, mx, sr = tr(numbers)
    print(f"Минимум: {mn}")
    print(f"Максимум: {mx}")
    print(f"Среднее: {sr}")