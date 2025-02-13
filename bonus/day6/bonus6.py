contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The carrots was well preserved.",
            "This is the first part of one of the most longest paragraphs"
            "its neccesary not put commas at the end of the line, and open double quotes"]

filenames = ["doc.txt", "report.txt", "presentation.txt", "presentation2.txt"]

# Zip explanation
# https://www.w3schools.com/python/ref_func_zip.asp
# example
# >>> a = [1, 2, 3]
# >>> b = [4, 5, 6]
# >>> c = [7, 8, 9]
# >>> list(zip(a, b, c))
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

for content, filename in zip(contents, filenames):
    file = open(f"../../files/bonus/{filename}", "w")
    file.writelines(content)
    file.close()