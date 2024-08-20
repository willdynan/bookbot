def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_word_count(text)
    char_count = get_char_count(text)
    listified = dict_list(char_count)
    report = sort_report(listified)
    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in this document")
    for i in report:
        print(f"The '{i['character']}' character was found {i['num']} times")
    print("--- End Report ---")   

#Returns the information contained in book file.
def get_book_text(path):
    with open(path) as f:
        #print(f)
        return f.read()

#Takes book string and splits on white space to count the total words
def get_word_count(text):
    words = text.split()
    num = (len(words))
    return(num)

#Takes book string and returns count of all characters in lowercase
def get_char_count(text):
    lower = text.lower()
    cc = {}
    for c in lower:
        if c not in cc:
            cc.setdefault(c, 1)
        else: cc[c] += 1
    return cc
    
def dict_list(char_count):
    listy = []
    for k in char_count:
        if k.isalpha():
            listy.append({"character": k, "num": char_count[k]})
    return(listy)

def sort_report(listified):
    def sort_key(c):
        return c["num"]
    listified.sort(reverse=True, key=sort_key)
    return listified

main()