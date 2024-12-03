import re

with open("data.txt") as file:
    contents = file.read()
    regex = r"mul\((0|[1-9][0-9]*),(0|[1-9][0-9]*)\)"
    matches = re.findall(regex, contents)
    total = 0
    # Part 1
    for match in matches:
        first, second = int(match[0]), int(match[1])
        total += first * second
    print("Part 1 Solution:", total)

    # Part 2
    enabled = True
    total2 = 0
    pos = 0

    while pos < len(contents):
        do_pos = contents.find("do()", pos)
        dont_pos = contents.find("don't()", pos)
        mul_match = re.search(regex, contents[pos:])
        mul_pos = mul_match.start() + pos if mul_match else -1
        next_positions = [p for p in [do_pos, dont_pos, mul_pos] if p != -1]
        if not next_positions:
            break

        next_pos = min(next_positions)

        if next_pos == do_pos:
            enabled = True
            pos = do_pos + 4 # hardcoded length of do
        elif next_pos == dont_pos:
            enabled = False
            pos = dont_pos + 6
        else:
            if enabled:
                match = mul_match.groups()
                first, second = int(match[0]), int(match[1])
                total2 += first * second
            pos = mul_pos + len(mul_match.group())
    print("Part 2 Solution:", total2)