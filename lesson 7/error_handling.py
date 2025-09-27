try:
    result = 10/0
except ZeroDivisionError:
    print("Division isnt allowed cuz of u tryna divide by 0.")


text = "This is not a number"

try:
    text_to_int = int(text)
except Exception as e:
    print("An error occured while parsing the data: ", e)


try:
    result = 10/2
except ZeroDivisionError:
    print("Division isnt allowed cuz of u tryna divide by 0.")
else:
    print("Division succesful. The result is ", result)
