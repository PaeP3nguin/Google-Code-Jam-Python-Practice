def main():
    with open("A-large-practice.in") as in_file:
        with open("min-scalar-prod-out-large.txt", "w") as fout:
            num_lines = int(in_file.readline())
            print(num_lines)
            for x in range(1, num_lines + 1):
                vector_len = int(in_file.readline())
                v1 = [int(x) for x in in_file.readline().split(' ')]
                v1.sort()
                v2 = [int(x) for x in in_file.readline().split(' ')]
                v2.sort()
                v2 = v2[::-1]
                prod = scalar_prod(v1, v2)
                fout.write("Case #{0}: {1}\n".format(x, prod))

def scalar_prod(vec1, vec2):
    prod = 0
    for x in range(len(vec1)):
        prod += vec1[x]*vec2[x]
    return prod

if __name__ == "__main__":
    main()
