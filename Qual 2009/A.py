#! python3

def main():
    with open("A-small-practice.in") as in_file:
        with open("A-small-practice.out", "w") as fout:
            info = in_file.readline().replace('\n', '').split(' ')
            print(info)
            num_words = int(info[1])
            num_cases = int(info[2])
            words = []
            for x in range(num_words):
                words.append(in_file.readline())
            for x in range(1, num_cases + 1):
                case = in_file.readline().replace('\n', '')
                tokens = case.replace('(', ' ').replace(')', ' ').split(' ')
                print(tokens)

                fout.write("Case #{0}: {1}\n".format(x, case))

if __name__ == "__main__":
    main()
