class Numbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.sequence = self._calc()
    def _calc(self):
        sequence = []
        total = 0
        cur_min = None
        for num in self.numbers:
            cur_min = num if cur_min is None else min(cur_min, num)
            total += cur_min
            sequence.append(total)
        return sequence

    def get_elements(self):
        return self.sequence

    def show_elements(self):
        print(self.sequence)

    def __iter__(self):
        return iter(self.sequence)

    def __add__(self, other):
        return Numbers(self.numbers + other.numbers)

def main():
    print("Введите первую последовательность: ")
    input1 = input().strip()
    print("Введите вторую последовательность: ")
    input2 = input().strip()
    try:
        nums1 = list(map(int, input1.split()))
        nums2 = list(map(int, input2.split()))
    except ValueError:
        print("Введите числа!")
        return

    seq1 = Numbers(nums1)
    seq2 = Numbers(nums2)
    combo = seq1 + seq2
    print("\nРезультат объединения последовательностей: ")
    for num in combo:
        print(num, end=' ')
main()




