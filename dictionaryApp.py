import json
from difflib import get_close_matches


# data = json.load(open("data1.json"))
data = json.load(open("data.json"))

def translate(w):
	w = w.lower() #change into lower case(use with data.json)
	# w = w.upper() #change into upper case (use with data1.json)

	if w in data:
		return data[w]
	elif w.title() in data: #if user entered "texas" this will check for "taxas" this check for "Texas" as well
		return data[w.title()]

	elif w.upper() in data: #to get definition of Acronyms(such as USA or NATO0)
		return data[w.upper()]

	elif len(get_close_matches(w, data.keys())) > 0 :

		yn = input("Did you mean %s instead? Enter Y id yes, or N if no." % get_close_matches(w,data.keys())[0])
		if yn =="Y":
			return data[get_close_matches(w,data.keys())[0]]
		elif yn =="N":
			return "The word doesn't exist. Please double check it."
		else:
			return "We didn't understan your entry."

	else:
		return "The word \"{}\" does not exist.Please double check it.".format(w)

# def main():
# 	while True:
# 		word = input("Enter word: ")
# 		print(translate(word))
# 		done = input("Do you want to continue? \nType \'N\' to exit, \'Y\' to continue : ")

# 		if done =='n':
# 			break
# 		else:
# 			continue


# if __name__ == "__main__":
# 	main()
word = input("Enter word: ")

output = translate(word)
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
