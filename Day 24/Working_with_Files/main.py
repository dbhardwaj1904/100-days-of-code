# If file exists text can be over-written or append
# Depending on mode "w" or "a"

# For reading file (by default, it is read mode)
with open("my_file.txt") as file:
    content = file.read()

# For writing file (mode="a" -> for appending)
with open("my_file_write.txt", mode="w") as file:
    file.write("My steam name is Jimmy.")


# For writing file (mode="a" -> for appending)
with open("my_file_write.txt", mode="a") as file:
    file.write("\nI mostly play Apex Legends.")
