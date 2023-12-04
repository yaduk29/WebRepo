def check_word_presence():
	text=input("Enter a text:")
	word=input("Enter a  word to check its presence:")
	if word in text:
		print(f"'{word}'is present in the text.")
	else:
		print(f"'{word}'is not present in the text.")
		
check_word_presence()
