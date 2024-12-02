def read_input(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def part1(data):
    list1 = []
    list2 = []
    for i in data:
       a = i.split()
       list1.append(a[0])
       list2.append(a[1])
    list1.sort()
    list2.sort()
    b = 0
    for i in range(0, len(list1)):
        print(f"Part 1 iteration {i}:")  # labeled print
        b += abs(int(list1[i])-int(list2[i]))
    return b

def part2(data):
    list1 = []
    list2 = []
    for i in data:
       a = i.split()
       list1.append(a[0])
       list2.append(a[1])
    list1.sort()
    list2.sort()
    c = 0
    for i in list1:
        a = list2.count(i)
        print(f"Part 2 - number {i} appears {a} times")  # labeled print
        b = int(i)*a
        print(f"Number {i} appears {a} times, adding {b} to total")
        if b:
            c += int(b)
    return c

if __name__ == "__main__":
    input_data = read_input("input_day_1")
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
