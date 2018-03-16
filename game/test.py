import re


def safe_pawns(pawns):
    count = 0
    right = ""
    apl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, 9):
        for j in range(apl.__len__()):
            if i % 2 == 0:
                if j % 2 == 1:
                    right += apl[j]
                    right += str(i)
            else:
                if j%2==0:
                    right+=apl[j]
                    right+=str(i)
    for item in pawns:
        if re.findall(item, right).__len__()!=0:
            print(re.findall(item,right))
            count += 1
    print(count)
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})
    safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"})
