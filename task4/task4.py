import sys

def read_array(file_path):
    with open(file_path, 'r') as file:
        array = [int(line) for line in file]
        return array


def calculate_moves(array):
    nums.sort()
    mediana = nums[len(nums) // 2]
    moves = 0
    for num in array:
        moves += abs(num - mediana)
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]
    nums = read_array(input_file)
    nums.sort()
    mediana = nums[len(nums)//2]
    moves = calculate_moves(nums)
    print(moves)