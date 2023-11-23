def read_file(file_path):
    tribes = {}
    girls = set()
    boys = set()

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if i == 0:
                continue

            number1, number2 = map(int, line.split())

            if number1 % 2 == 0:
                girls.add(number1)
            else:
                boys.add(number1)

            if number2 % 2 == 0:
                girls.add(number2)
            else:
                boys.add(number2)

            if i == 0:
                tribes[number1] = 0
                tribes[number2] = 0
            else:
                if number1 in tribes:
                    tribes[number2] = tribes[number1]
                elif number2 in tribes:
                    tribes[number1] = tribes[number2]
                else:
                    tribes[number1] = i
                    tribes[number2] = i
    return tribes, boys, girls


def group_by_tribe(tribes, boys, girls):
    tribe_groups = {"boys": {}, "girls": {}}

    for boy in boys:
        tribe = tribes.get(boy)
        if tribe is not None:
            if tribe not in tribe_groups["boys"]:
                tribe_groups["boys"][tribe] = []
            tribe_groups["boys"][tribe].append(boy)

    for girl in girls:
        tribe = tribes.get(girl)
        if tribe is not None:
            if tribe not in tribe_groups["girls"]:
                tribe_groups["girls"][tribe] = []
            tribe_groups["girls"][tribe].append(girl)

    return tribe_groups


def count_possible_pairs(tribe_groups):
    count = 0
    boys_tribes = tribe_groups["boys"]
    girls_tribes = tribe_groups["girls"]
    possible_pairs = []

    for boy_tribe in boys_tribes:
        for girl_tribe in girls_tribes:
            if boy_tribe != girl_tribe:
                count += len(boys_tribes[boy_tribe]) * len(girls_tribes[girl_tribe])
                possible_pairs.extend([(b, g) for b in boys_tribes[boy_tribe] for g in girls_tribes[girl_tribe]])
    return count, possible_pairs


def output(file_path, count):
    with open(file_path, "w") as file:
        file.write("Результат: " + str(count))


if __name__ == "__main__":
    input_file = "test/input.txt"
    output_file = "test/output.txt"

    tribes, boys, girls = read_file(input_file)
    tribe_groups = group_by_tribe(tribes, boys, girls)
    count = count_possible_pairs(tribe_groups)
    output(output_file, count)