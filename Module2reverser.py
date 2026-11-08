def reverse_words(text: str) -> str:
    """กลับลำดับคำในข้อความ (แยกคำด้วยช่องว่าง)"""
    words = text.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# ตัวอย่างการทดสอบการทำงาน
if __name__ == "__main__":
    print(reverse_words("hello first year"))  # ผลลัพธ์: "year first hello"
    print(reverse_words("a b"))               # ผลลัพธ์: "b a"
    print(reverse_words("A B"))                  # ผลลัพธ์: "B A"