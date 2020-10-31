def one_item(text_list):
    for j in [i for i in text_list if text_list.count(i) == 1]:
        print(j)

one_item(["a", "a", "b"])