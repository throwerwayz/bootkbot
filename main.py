from pathlib import Path

def word_count(content):
    words = content.split()
    return len(words)

def count_letters(content):
    letters = {}
    for letter in content:
        if not letter.isalpha():
            continue
        if not letter in letters:
            letters[letter.lower()] = 0

        letters[letter.lower()] += 1

    output = []
    for k, v in enumerate(letters):
        output.append({
            "character": v,
            "count": k
        })


    return output

def get_content(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict['count']

def main():
    content = get_content(Path('books/frankenstein.txt'))
    words = word_count(content)
    print(f"There are {words} words in the book.\n")
    letters = count_letters(content)
    letters.sort(reverse=True, key=sort_on)

    for letter in letters:
        print(f"There are {letter['count']} {letter['character']}'s")

if __name__ == "__main__":
    main()




