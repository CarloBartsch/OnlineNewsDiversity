from csv import reader
# read csv file as a list of lists
with open('C:/Users/admin/Documents/Dissertation/Diversity of News/Files/bild/Corpus/Test.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)
    res = str(list_of_rows)[1:-1]
