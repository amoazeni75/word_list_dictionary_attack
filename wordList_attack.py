from itertools import permutations

print("please input your target words, to finish enter @finish@")
input_words = []
output_words = []
while 1:
    inp = input()
    if inp.__eq__("@finish@"):
        break
    else:
        input_words.append(inp)

for i in range(0, input_words.__len__()):
    perm = permutations(input_words, i + 1)
    for j in list(perm):
        str = ""
        for k in range(0, j.__len__()):
            str += j[k]
        output_words.append(str)

with open("output.txt", "w") as txt_file:
    for line in output_words:
        txt_file.write("".join(line) + "\n")