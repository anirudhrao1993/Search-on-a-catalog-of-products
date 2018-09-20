To run the program:
$ python search.py

This program consists of two parts : "read_file.py" and "search.py".

"read_file.py" preprocesses the products.csv file. The csv file is converted into a few key-value pairs, where the key is a possible keyword for which a user might search.

The output of "read_file.py" is three hash tables; on that maps brands to product numbers, one that maps product types to product numbers and one that maps general keywords from all fields to product numbers.

"search.py" allows the user to search by keyword, brands, or product types. When the user enters a keyword, the program searches the appropriate hash table and displays all the search results.
