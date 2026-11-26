def count_words(text):
    return len(text.split())

if __name__ == "__main__":
    print(count_words("a b c"))  # ผลลัพธ์ต้องได้ 3
    print(count_words(""))       # ผลลัพธ์ต้องได้ 0