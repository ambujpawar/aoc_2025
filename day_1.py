from utils.read_input import read_input


START_POS = 50


def part_1(input_data: list[str]) -> int:
    count = 0
    pos = START_POS


    for d in input_data:
        dir, steps = d[0], int(d[1:])
        if dir == 'L':
            pos = (pos - steps) % 100
        elif dir == 'R':
            pos = (pos + steps) % 100    
        if pos == 0:
            count += 1
        
        print(f"Dial is rotated {dir} dir by {steps} steps to position: {pos}" )
    
    print(f"Number of times passed 0: {count}")


def part_2(input_data: list[str]) -> int:
    crossed_zero = 0
    pos = START_POS

    for i, d in enumerate(input_data):
        dir, steps = d[0], int(d[1:])
        og_pos = pos

        if dir == 'L':
            A = pos - steps      # left visited interval start
            B = pos - 1          # left visited interval end
        else:  # 'R'
            A = pos + 1          # right visited interval start
            B = pos + steps      # right visited interval end

        # Count multiples of 100 in [A, B]: floor(B/100) - floor((A-1)/100)
        zeros_this_turn = (B // 100) - ((A - 1) // 100)
        crossed_zero += zeros_this_turn

        # update position modulo 100
        if dir == 'L':
            pos = (pos - steps) % 100
        else:
            pos = (pos + steps) % 100

        print(f"Turn {i+1}: OG pos {og_pos} moved in {dir} {steps} steps to position: {pos}" )
        print(zeros_this_turn, crossed_zero)

    print(f"Number of times passed 0: {crossed_zero}")
    return crossed_zero


if __name__ == "__main__":
   # part_1(read_input("data/day_1.txt"))
    part_2(read_input("data/day_1.txt"))