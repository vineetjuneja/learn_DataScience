# complex list comprehension
print(
    [i*6 if i%2==0 else i*5 if i%5==0 else i*3 for i in range (1,11)]
)