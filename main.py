def can_place_cows(free_sections, c, min_distance):
    cows_placed = 1
    last_position = free_sections[0]
    print(last_position)

    for i in range(1, len(free_sections)):
        if free_sections[i] - last_position >= min_distance:
            print(free_sections[i])
            cows_placed += 1
            last_position = free_sections[i]

    return cows_placed >= c


def get_max_width(c, free_sections):

    if c == 2:
        return max(free_sections) - min(free_sections)

    free_sections.sort()
    result = 0
    min_distance = 0
    max_distance = free_sections[-1] - free_sections[0]

    while min_distance <= max_distance:
        mid_distance = (min_distance + max_distance) // 2
        if can_place_cows(free_sections, c, mid_distance):
            result = mid_distance
            min_distance = mid_distance + 1
        else:
            max_distance = mid_distance - 1

    return result


if __name__ == '__main__':
    print(get_max_width(4, [1, 2, 3, 4, 5, 10, 30, 40, 60, 90]))














