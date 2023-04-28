# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["adsfsdc"])
# except FileNotFoundError:
#     file = open("a_file.txt", mode="w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File is closed")
#     raise TypeError("This is an error that I made up")

height = float(input("Height: "))
weight = float(input("Weight: "))
if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight / height ** 2
print(f"BMI: {bmi}")
