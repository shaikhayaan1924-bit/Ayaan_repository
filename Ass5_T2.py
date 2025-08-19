li = []
for i in range(1,11):
    li.append(i)
print("Original list:",li)
extracted = li[:5]
print("Extracted first five elements:",extracted)
reverse = list(reversed(extracted))
print("Reversed extracted elements:",reverse)