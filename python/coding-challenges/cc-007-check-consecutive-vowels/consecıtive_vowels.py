def consecutive(text):
    vowels = "aeiou"
    j = 1
    for i in text:
        if j == len(text):
            return "Negative"
        if i in 'aeio':
            if text[j] == vowels[vowels.find(i) + 1]:
                return "Positive"
        j += 1
        
consecutive('a')