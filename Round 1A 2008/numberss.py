from decimal import *
import math

def main():
    with open("C-large-practice.in") as in_file:
        with open("numbers-large.out", "w") as fout:
            num_lines = int(in_file.readline())
            print(num_lines)
            for x in range(1, num_lines + 1):
                context = getcontext()
                context.prec = math.trunc(MAX_PREC / 20)
                num = float(in_file.readline())
                start = context.add(Decimal(3), context.sqrt(Decimal(5)))
                start = context.power(start, Decimal(num))
                start = math.trunc(start)
                start = str(start).zfill(3)
                start = start[-3:]

                fout.write("Case #{0}: {1}\n".format(x, start))

if __name__ == "__main__":
    main()
