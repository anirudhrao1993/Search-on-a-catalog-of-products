import pickle

products = []
word_dict = {}
type_dict = {}
brand_dict = {}


with open('products.pickle', 'rb') as handle:
    products = pickle.load(handle)

with open('word_dict.pickle', 'rb') as handle:
    word_dict = pickle.load(handle)

with open('type_dict.pickle', 'rb') as handle:
    type_dict = pickle.load(handle)

with open('brand_dict.pickle', 'rb') as handle:
    brand_dict = pickle.load(handle)


print("Enter a number to search by category:")
print("1. Keyword search")
print("2. Search by brand")
print("3. Search by type")

search_type = int(raw_input().strip())

key = str(raw_input("Enter a search term\n")).strip().lower()

search_dict = word_dict

if search_type == 2:
    search_dict = brand_dict
if search_type == 3:
    search_dict = type_dict

if key in search_dict:
    product_ids = search_dict[key]
    for pid in product_ids:
        print products[pid]

else:
    print("Search term not found in database")
