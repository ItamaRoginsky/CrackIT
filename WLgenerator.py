import itertools
import random
import os
import time

def word_variations(word, include_symbols=True, include_numbers=True):
    if not word:
        return set()
    
    vari = set()
    symbols = ['$', '@', '!', '#', '%', '&', '*']
    
    vari.add(word)
    vari.add(word[::-1])
    vari.add(word.upper())
    vari.add(word.capitalize())
    vari.add(word.lower())
    vari.add(word.title())
    vari.add(word.swapcase())

    if include_numbers:
        for num in range(1000):
            vari.add(f"{word}{num}")
            vari.add(f"{num}{word}")
            vari.add(f"{word[::-1]}{num}")
            vari.add(f"{num}{word[::-1]}")
    
    if include_symbols:
        for symbol in symbols:
            vari.add(f"{word}{symbol}")
            vari.add(f"{symbol}{word}")
            vari.add(f"{word[::-1]}{symbol}")
            vari.add(f"{symbol}{word[::-1]}")
            if include_numbers:
                for num in range(1000):
                    vari.add(f"{word}{num}{symbol}")
                    vari.add(f"{symbol}{word}{num}")
                    vari.add(f"{num}{word}{symbol}")
                    vari.add(f"{symbol}{num}{word}")
                    vari.add(f"{num}{symbol}{word}")
                    vari.add(f"{word}{symbol}{num}")
                    vari.add(f"{word[::-1]}{num}{symbol}")
                    vari.add(f"{symbol}{word[::-1]}{num}")
                    vari.add(f"{num}{symbol}{word[::-1]}")
    
    return vari

def capitalize_variations(word):
    capitalized_variations = {
        word.capitalize(),
        word.upper(),
        word.title(),
        word[::-1].capitalize(),
        word[::-1].upper(),
        word[::-1].title()
    }
    return capitalized_variations

def generate_combinations(base_words, include_symbols=True, include_numbers=True):
    wordlist = set()

    for word in base_words:
        wordlist.update(word_variations(word, include_symbols, include_numbers))
        wordlist.update(capitalize_variations(word))

    for combo in itertools.combinations(base_words, 2):
        combined = ''.join(combo)
        reversed_combined = ''.join([c[::-1] for c in combo])
        
        wordlist.add(combined)
        wordlist.add(reversed_combined)
        wordlist.update(capitalize_variations(combined))
        wordlist.update(capitalize_variations(reversed_combined))
        
        for num in range(1000):
            wordlist.add(f"{combined}{num}")
            wordlist.add(f"{num}{combined}")
            wordlist.add(f"{reversed_combined}{num}")
            wordlist.add(f"{num}{reversed_combined}")
            for symbol in ['$', '@', '!', '#', '%', '&', '*']:
                wordlist.add(f"{combined}{symbol}")
                wordlist.add(f"{symbol}{combined}")
                wordlist.add(f"{reversed_combined}{symbol}")
                wordlist.add(f"{symbol}{reversed_combined}")

    for combo in itertools.combinations(base_words, 3):
        combined = ''.join(combo)
        reversed_combined = ''.join([c[::-1] for c in combo])
        
        wordlist.add(combined)
        wordlist.add(reversed_combined)
        wordlist.update(capitalize_variations(combined))
        wordlist.update(capitalize_variations(reversed_combined))
        
        for num in range(1000):
            wordlist.add(f"{combined}{num}")
            wordlist.add(f"{num}{combined}")
            wordlist.add(f"{reversed_combined}{num}")
            wordlist.add(f"{num}{reversed_combined}")
            for symbol in ['$', '@', '!', '#', '%', '&', '*']:
                wordlist.add(f"{combined}{symbol}")
                wordlist.add(f"{symbol}{combined}")
                wordlist.add(f"{reversed_combined}{symbol}")
                wordlist.add(f"{symbol}{reversed_combined}")

    final_list = list(wordlist)
    random.shuffle(final_list)
    return final_list

def main():
    name = input("Enter victim's name 🡆 ").strip()
    last_name = input("Enter victim's last name 🡆 ").strip()
    birth_year = input("Enter victim's birth year 🡆 ").strip()
    birth_month = input("Enter victim's birth month 🡆 ").strip()
    birth_day = input("Enter victim's birth day 🡆 ").strip()
    partner = input("\nEnter victim's partner name 🡆 ").strip()
    pet_name = input("\nEnter victim's pet name 🡆 ").strip()
    father = input("\nEnter victim's father name 🡆 ").strip()
    mother = input("Enter victim's mother name 🡆 ").strip()

    extra = input("\nDo you want to add extra keywords/dates/numbers? (y/n) 🡆 ").strip().lower()
    words = [name, last_name, pet_name, birth_year, birth_day, birth_month, partner, father, mother]
    
    if extra == 'y':
        item = input("Enter key word (q to stop) 🡆 ").strip()
        while item != 'q':
            words.append(item)
            item = input("Enter key word (q to stop) 🡆 ").strip()

    words = [word for word in words if word]
    os.system('cls' if os.name == 'nt' else 'clear')
    custom_path = input("Enter a directory to save the file (press Enter to save in current directory) 🡆 ").strip()
    include_symbols = input("Include symbols (y/n)? 🡆 ").strip().lower() == 'y'
    include_numbers = input("Include numbers (y/n)? 🡆 ").strip().lower() == 'y'

    wordlist = generate_combinations(words, include_symbols, include_numbers)
    
    if custom_path:
        if not os.path.exists(custom_path):
            os.makedirs(custom_path)
        wordlist_path = os.path.join(custom_path, "generated-wordlist.txt")
    else:
        wordlist_path = os.path.join(os.getcwd(), "generated-wordlist.txt")

    with open(wordlist_path, 'w') as file:
        for word in wordlist:
            file.write(f"{word}\n")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Wordlist saved to: {wordlist_path}")
    print(f"Total words generated: {len(wordlist)}")

if __name__ == "__main__":
    main()