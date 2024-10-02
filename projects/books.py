title = "Wiedźmin ostatnie życzenie"
print(title)
author = "Andrzej Sapkowski"
print(author)
year = 1993
print(year)
is_published_after_2000 = False
print(is_published_after_2000)
current_year = 2024
age = current_year - year
print(age)
characters = ["Geralt", "Yennefer", "Jaskier", "Ciri"]
print(characters) 
print(characters[0])
print(characters [1])
favourite_book = {
    "title" : "Wiedźmin ostatnie życzenie",
    "author" : "Andrzej Sapkowski",
    "year" : 1993,
    "is_published_after_2000" : False,
    "characters" : ["Geralt", "Yennefer", "Jaskier", "Ciri"]
}
print(favourite_book)
print(favourite_book["author"])
print(favourite_book["year"])
favourite_books = {
    "title" : "Niewinne ofiary",
    "author" : "Katarzyna Wolwowicz",
    "year" : 2023,
    "is_published_after_2000" : True,
    "characters" : ["Olga Balicka", "Kornel Murecki", "Adam Pawłowski", "Katarzyna Sarnecka"]
}
print(favourite_books)
print(favourite_books["title"])


age_difference = favourite_books["year"] - favourite_book["year"]
print(age_difference)
