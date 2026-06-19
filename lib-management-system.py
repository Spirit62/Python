"Welcome to Samriddha's Library Management System"
Library_Books=[]

while True:
  print("Choose a number from 1 to 4\n")
  print("1. Add Book\n2. View Books\n3. Search Book\n4. Exit\n")
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input! Please enter an integer number (1-4).")
    continue 
  match choice:
    case 1:
      book_id = input("Enter the book id")
      book_title = input("Enter the title")
      book_author = input("Enter the author")
      book_category = input("Enter category")
      bookadd={
              "id":book_id,
              "title":book_title,
              "author":book_author,
              "category":book_category
          }
      id_exists = False
      for book in Library_Books:
        if book["id"] == book_id:
            id_exists = True
            break
      if id_exists == True:
        print("Book has already been added, invalid!")
      else:
        Library_Books.append(bookadd)
        print("Book Added Successfully")
    case 2:
      print("id\ttitle\tauthor\tcategory")
      for i in Library_Books:
        print(f"{i['id']}\t{i['title']}\t{i['author']}\t{i['category']}")
    case 3:
      search_title = input("Enter the title of the book to search: ")
      found = False
      for book in Library_Books:
          if book["title"].lower() == search_title.lower():
              print("\nBook Found!")
              print(f"ID: {book['id']}\tTitle: {book['title']}\tAuthor: {book['author']}\tCategory: {book['category']}")
              found = True
              break
      if not found:
          print("Book not found in the library.")
    case 4:
      print("Thank you for using Samriddha's Library Management System. Goodbye!")
      break
    case _:
      print("Invalid choice! Please enter a number between 1 and 4.")
        
    
