def main():
	book_path = "books/frankenstein.txt"
	text = get_book_text(book_path)
	word_count = get_word_count(text)
	char_count = get_char_count(text)
	report = get_report(char_count, word_count)

	
	print(report)

def get_word_count(text):
	lines = text.split()
	return len(lines)



def get_book_text(path):
	with open(path) as f:
		return f.read()
	

def get_char_count(text):
	lower = text.lower()
	letters = {}
	letter_list = [chr(x) for x in range(97, 123)]
	for char in lower:
		if char in letter_list:
			letters[char] = letters.get(char, 0) + 1

			
	return dict(sorted(letters.items()))

def sort_on(dict):
	return dict["num"]

def get_report(char_count, word_count):
	# create a list of dictionaries
	char_list = []
	for char in char_count:
		char_list.append({"char": char, "num": char_count[char]})
	#sort after the loop is complete
	char_list.sort(reverse = True, key = sort_on)
	
	report = "--- Begin report of books/frankenstein.txt ---\n"
	report += f"{word_count} words found in the document\n\n"

	for char_dict in char_list:
		report += f"The '{char_dict['char']}' character was found {char_dict['num']} times\n"
	
	report += "--- End report ---"
	return report


main()
