def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())

if __name__ == "__main__":
    print(capitalize_words("hello first year"))  # ผลลัพธ์ต้องได้ Hello First Year
    print(capitalize_words("a b"))               # ผลลัพธ์ต้องได้ A B