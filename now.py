numbers={
  "1":"one",
  "2":"two",
  "3":"three",
  "4":"four",
  "5":"five",
  "6":"six",
  "7":"seven",
  "8":"eight"
}
namba=input("your namba  ")
for digit in namba:
  if digit in numbers:
      print(numbers[digit]+" ",end="")
  else:
      print("No mapping for number!!")