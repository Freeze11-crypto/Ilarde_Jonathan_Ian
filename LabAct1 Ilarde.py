def is_palindrome(text):
    cleaned = text.replace(" "," ").lower()
    return cleaned == cleaned[::-1]

def get_grades(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 90:
        return "B"
    elif 70 <= score <= 80:
        return "C"
    elif 60 <= score <= 70:
        return "D"
    else: 
        return "E"
    
def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product

def print_formatted_info(title, **kwargs):
    print(title.upper())
    for key, value in kwargs.items():
        print(f"{key}: {value}")

#Task 1
print(is_palindrome("Boss!"))
print(is_palindrome("Bitch!"))

#Task 2
print(get_grades(95))
print(get_grades(75))

#Task 3
print(multiply_all("2, 3, 4"))
print(multiply_all("5, 10"))

#Task 4
print_formatted_info("report", name="Theo", score=84, status="Passed")