line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure with an X marks the spot.")
position = input("Enter the position on the map: ") 

letter = position[0].lower();
abc = ["a","b","c"]
letter_index = abc.index(letter)
num_index = int(position[1]) - 1
map[num_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")