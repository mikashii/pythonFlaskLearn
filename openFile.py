#fileName = open("readme.md").read()
#print(fileName)

fileName = open("readme.md", "a").write("\n## This is a new line into the file")
print(fileName)