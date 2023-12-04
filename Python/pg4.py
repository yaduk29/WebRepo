def count_display_second_char():
	text=input("Enter a line of text:")
	print(f"Number of characters:{len(text)}")
	if len(text)>=2:
		print(f"The second character is:{text[1]}")
	
count_display_second_char()
