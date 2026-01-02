f = open("data.txt", "w")
f.write("Hello")
f.close() # If an error happens before this line, the file stays open in memory!

with open("data.txt", "w") as f:
    f.write("Hello")
# The file closes automatically here, even if an error occurs inside the block.