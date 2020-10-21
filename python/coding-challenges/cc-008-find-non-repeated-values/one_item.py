def one_item(text_list):
    item = [i for i in text_list if text_list.count(i) == 1]
    for i in item:
        print(i)