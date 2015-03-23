# import itertools
import pdb

class Customer:
    def __init__(self, pref_count, prefs):
        self.pref_count = pref_count
        self.prefs = prefs

    def isSatisfied(self, batches):
        # pdb.set_trace()
        for b in range(0, len(batches)):
            for pref in self.prefs:
                if b + 1 == pref[0] and batches[b] == pref[1]:
                    return True
        return False

def main():
    with open("B-large-practice.in") as in_file:
        with open("milkshakes-out-large.txt", "w") as fout:
            num_cases = int(in_file.readline())
            print(num_cases)
            for x in range(1, num_cases + 1):
                num_flavors = int(in_file.readline())
                num_customers = int(in_file.readline())
                un_customers = []
                prelim_batch = [-1] * num_flavors
                impossible = False
                for y in range(num_customers):
                    cust_line = in_file.readline().replace('\n', '').split(' ')
                    pref_count = int(cust_line[0])
                    i = 1
                    if pref_count is 1:
                        flavor = int(cust_line[i])
                        pref = int(cust_line[i + 1])
                        if prelim_batch[flavor - 1] != -1 and prelim_batch[flavor - 1] != pref:
                            impossible = True
                        else:
                            prelim_batch[flavor - 1] = pref
                    else:
                        customer = Customer(pref_count, [])
                        for z in range(pref_count):
                            flavor = int(cust_line[i])
                            pref = int(cust_line[i + 1])
                            customer.prefs.append((flavor, pref))
                            i += 2
                            un_customers.append(customer)

                if impossible is True:
                    fout.write("Case #{0}: {1}\n".format(x, "IMPOSSIBLE"))
                    continue

                all_satisfied = False
                possible = True
                best_batch = [y if y != -1 else 0 for y in prelim_batch]
                while not all_satisfied and possible:
                    all_satisfied = True
                    for cust in un_customers:
                        if not cust.isSatisfied(best_batch):
                            all_satisfied = False
                            for pref in cust.prefs:
                                if pref[1] == 1:
                                    best_batch[pref[0] - 1] = 1
                            if not cust.isSatisfied(best_batch):
                                possible = False

                if possible is False:
                    best_batch = "IMPOSSIBLE"
                else:
                    best_batch = ' '.join([str(x) for x in best_batch])
                fout.write("Case #{0}: {1}\n".format(x, best_batch))

def checkSatisfaction(batches, customers):
    for customer in customers:
        if not customer.isSatisfied(batches):
            return False
    return True

if __name__ == "__main__":
    main()
