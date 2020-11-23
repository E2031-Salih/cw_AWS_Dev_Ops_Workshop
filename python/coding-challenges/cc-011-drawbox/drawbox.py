def drawbox(entry):
    for i in range(entry):
        if i == 0 or i == entry-1:
            print('#'*entry)
        else:
            print('#' + ' ' * (entry - 2) + '#')
drawbox(3)