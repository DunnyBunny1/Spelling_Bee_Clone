# Assume the first character is the "golden" letter that must be in all words
valid_chars = 'humidfe'

def main():
    words = []
    pangrams = []
    with open('./words.txt') as f: 
        for line in f: 
            words.append(line.lower().strip())
        valid_words = [word for word in words if is_valid_word(word)]
        valid_words.sort(key = lambda word : len(word))

        pangrams = [word for word in valid_words if is_pangram(word)]
    
        print(f'Valid words: {valid_words}')
        print(f'Pangrams: {pangrams}')

def is_valid_word(word : str):
    golden_letter = valid_chars[0]
    if len(word) < 4 or golden_letter not in word:
        return False
    for char in word:
        if char not in valid_chars: 
            return False 
    return True 

def is_pangram(word : str):
    for char in valid_chars: 
        if char not in word: 
            return False
    return True


if __name__ == '__main__':
    main()