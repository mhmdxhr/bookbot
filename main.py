def main():
    book_path ="books/frankenstein.txt"
    text = get_book_text(book_path)
    dict = count_letters(text)
    sorted_dict=dict_sort(dict)
    print(f"--------Report of {book_path}--------")
    print(f"{count_words(text)} words found in the book")
    print()

    for items in sorted_dict:
        if not items["char"].isalpha():
            continue
        print(f"The {items['char']} charachter was found {items['num']} times")

    
    print("--------End of report--------")

def get_book_text(path):
    with open(path) as f:
        return f.read()
def count_words(text):
    return len(text.split())
def count_letters(text):
    chars={}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
         
def sort_on(dict):
    return dict["num"]
def dict_sort(dict):
    sorted_list=[]
    for ch in dict:
        sorted_list.append({"char": ch, "num": dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()