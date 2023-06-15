# Open the file in write mode
f2 = open("output2.txt", "w")

# Open the input file again and get
# the content as list to a variable data
with open("myfile.txt", "r") as myfile:
    data = myfile.readlines()

# We will just reverse the
# array using following code
data_2 = data[::-1]

# Now we will write the fully reverse
# list in the output2 file using
# following command
f2.writelines(data_2)
print(data_2)
f2.close()