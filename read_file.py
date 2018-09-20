import csv
import pickle

filename = "products.csv"

stop_words = ['a', 'the', 'and', 'to', '&', 'for', 'with', 'on', 'or']

word_dict = {}

products = []

brand_dict = {}

type_dict = {}

brand_index = 1

type_index = 3

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            products.append(row)
            brand = row[brand_index].strip().lower().split()
            p_type = row[type_index].strip().lower()
            words_in_row = " ".join(row[1:]).lower().strip().split()
            for word in words_in_row:
                if word not in stop_words and word not in word_dict:
                    word_dict[word] = [line_count]

                elif word in word_dict:
                    word_dict[word].append(line_count)

            for word in brand:
                if word not in brand_dict:
                    brand_dict[word] = [line_count]
                else:
                    brand_dict[word].append(line_count)

            if p_type not in type_dict:
                type_dict[p_type] = [line_count]
            else:
                type_dict[p_type].append(line_count)

            line_count += 1

with open('word_dict.pickle', 'wb') as handle:
    pickle.dump(word_dict, handle)

with open('products.pickle', 'wb') as handle:
    pickle.dump(products, handle)

with open('brand_dict.pickle', 'wb') as handle:
    pickle.dump(brand_dict, handle)

with open('type_dict.pickle', 'wb') as handle:
    pickle.dump(type_dict, handle)

print brand_dict
