def remove_duplicates():
	items=input("Enter a list of items seperated by space:").split()
	unique_items=list(set(items))
	print("List after removing duplicates:",unique_items)
	
remove_duplicates()
