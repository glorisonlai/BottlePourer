import readline
import copy

class Bottle_Level:
    bottles = []
    max_depth = 0
    checksums = set()
    retry_flag = False

    def parse_input(self):
        bottles_raw = input()
        bottles_raw = bottles_raw.split(" ")
        empty_bottles = int(bottles_raw.pop())
        new_bottles = list(map(lambda b: b.split(','), bottles_raw))
        for _ in range(empty_bottles):
            new_bottles.append([])

        self.bottles = new_bottles
        self.max_depth = len(self.bottles[0])

    def solve(self):
        return self.aux_solve(self.bottles, self.max_depth)
        
    def aux_solve(self, bottles, max_depth, steps = []):
        for b_index, bottle in enumerate(bottles):
            last_index = len(bottle) - 1

            if last_index == -1:
                continue
            last_letter = bottle[last_index]
            if last_letter == '?':
                if self.bottles[b_index][last_index] != '?':
                    bottles[b_index][last_index] = self.bottles[b_index][last_index]
                    continue
                print(steps)
                print(b_index, last_index)
                new_letter = input()
                bottles[b_index][last_index] = new_letter
                self.bottles[b_index][last_index] = new_letter
                print(self.bottles)
                self.retry_flag = True
                break

        if self.is_solved(bottles):
            return (True, steps)

        self.checksums.add(self.gen_checksum(bottles))

        moves, valid_moves = self.valid_moves(bottles, max_depth)

        if len(moves) == 0:
            return (False, steps)
        
        for (move, valid_move) in zip(moves, valid_moves):
            res = self.aux_solve(valid_move, max_depth, steps + [move])
            if res[0]:
                return res

        return (False, steps)

    def gen_checksum(self, bottles):
        checksum = 0
        for bottle in bottles:
            bottle_checksum = 1
            for i, letter in enumerate(bottle):
                bottle_checksum *= (ord(letter)) ** (i + 1)
            checksum += bottle_checksum
        return checksum % 2111379

    def valid_moves(self, bottles, max_depth):
        moves = []
        new_bottles = []
        for (src_index, src_bottle) in enumerate(bottles):
            if len(src_bottle) == 0:
                continue

            src_bottle_spaces = 0
            first_col = last(src_bottle)
            for col_index in range(-1, -1*(len(src_bottle)+1), -1):
                if src_bottle[col_index] == first_col:
                    src_bottle_spaces += 1
                else: 
                    break

            for (end_index, end_bottle) in enumerate(bottles):
                if src_index == end_index:
                    continue
                if (len(end_bottle) == 0 or last(src_bottle) == last(end_bottle)) and max_depth - len(end_bottle) >= src_bottle_spaces:
                    new_bottle = copy.deepcopy(bottles)
                    for _ in range(src_bottle_spaces):
                        new_bottle[src_index].pop()
                        new_bottle[end_index].append(first_col)
                    checksum = self.gen_checksum(new_bottle)
                    if checksum in self.checksums:
                        continue
                    new_bottles.append(new_bottle)
                    moves.append((src_index, end_index))
        return (moves, new_bottles)

        

    # Check each bottle has same color, or no colors
    def is_solved(self, bottles):
        return all(map(lambda ls: len(set(ls)) <= 1 and (len(ls) == self.max_depth or len(ls) == 0), bottles))

def last(ls):
    return ls[len(ls) - 1]
        

if __name__ == '__main__':
    level = Bottle_Level()
    level.parse_input()
    res = level.solve()
    if (res[0]):
        print(res)
    else:
        i = 0
        while ((i < 5 and level.retry_flag)):
            print("RESETTING...")
            res = level.solve()
            if (res[0]):
                print(res)
                break
            i += 1
