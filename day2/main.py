def safe(num: int, next: list[int], desc: bool = None) -> bool:
    if len(next) == 0:
        return True

    curr = num
    next_num = next[0]
    diff = abs(next_num - curr)

    if diff < 1 or diff > 3:
        return False

    if desc is None:
        if next_num > curr:
            return safe(next_num, next[1:], False)
        else:
            return safe(next_num, next[1:], True)

    if desc:
        if next_num >= curr:
            return False
        return safe(next_num, next[1:], True)
    else:
        if next_num <= curr:
            return False
        return safe(next_num, next[1:], False)

def might_be_safe(levels: list[int]) -> bool:
    if safe(levels[0], levels[1:]):
        return True

    # brute force since it's only the next item
    for i in range(len(levels)):
        new_sequence = levels[:i] + levels[i+1:]
        if safe(new_sequence[0], new_sequence[1:]):
            return True

    return False

with open("data.txt") as file:
    part1_count = 0
    part2_count = 0

    for line in file:
        levels = [int(x) for x in line.split()]
        if safe(levels[0], levels[1:]):
            part1_count += 1
        elif might_be_safe(levels):
            part2_count += 1

    print("Solution Part 1:", part1_count)
    print("Solution Part 2:", part1_count + part2_count)