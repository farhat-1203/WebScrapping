import wikipedia
import random
import sys

# Dictionary mapping language codes to language names
languages = {
    "en": "English",
    "ko": "Korean",
    "hi": "Hindi",
    "ar": "Arabic"
    # Add more languages as needed
}

favorite_articles = []

def search_wikipedia(query):
    try:
        page = wikipedia.page(query)
        print("\nTitle:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
        print("References:", page.references)
    except wikipedia.exceptions.PageError as e:
        print("Error:", e)
    except wikipedia.exceptions.DisambiguationError as e:
        print("DisambiguationError: This term may refer to multiple articles. Please specify.")
        print("Suggestions:", e.options)


def random_page():
    try:
        # Get a random Wikipedia page
        page = wikipedia.random()
        # Search for the random page
        page = wikipedia.page(page)
        print(f"\nRandom Wikipedia Page:")
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except Exception as e:
        print("Error:", e)

def quiz():
    questions = [
        ("What is the main programming language used for building web applications?", "JavaScript"),
        ("What does HTML stand for?", "Hypertext Markup Language"),
        ("Which programming language is known for its simplicity and readability?", "Python"),
        ("What is the primary function of a compiler?", "Translate code from high-level language to machine code"),
        ("What is the term for a data structure that consists of a collection of elements, each identified by at least one array index or key?", "Array"),
        ("What does CSS stand for?", "Cascading Style Sheets"),
        ("Which programming language is commonly used for building mobile applications?", "Java"),
        ("What is the process of finding errors and fixing them in a program called?", "Debugging"),
        ("What does SQL stand for?", "Structured Query Language"),
        ("Which programming language is used for statistical computing and graphics?", "R"),
    ]

    print("\nWelcome to the Programming Quiz!\n")
    score = 0
    for question, answer in random.sample(questions, k=2):
        user_answer = input(question + "\nYour answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is:", answer)
    
    print("\nQuiz completed!")
    print("Your score:", score)

def manage_favorites():
    global favorite_articles
    print("\nManage Favorite Articles:")
    print("1. Add an article to favorites")
    print("2. Remove an article from favorites")
    print("3. View favorite articles")
    choice = input("Enter your choice: ")

    if choice == '1':
        article_title = input("Enter the title of the article to add to favorites: ")
        favorite_articles.append(article_title)
        print(f"'{article_title}' has been added to favorites.")
    elif choice == '2':
        article_title = input("Enter the title of the article to remove from favorites: ")
        if article_title in favorite_articles:
            favorite_articles.remove(article_title)
            print(f"'{article_title}' has been removed from favorites.")
        else:
            print(f"'{article_title}' is not in favorites.")
    elif choice == '3':
        print("\nFavorite Articles:")
        for idx, article in enumerate(favorite_articles, start=1):
            print(f"{idx}. {article}")
    else:
        print("Invalid choice.")

def set_language():
    print("Available Languages:")
    for code, language in languages.items():
        print(f"{code}: {language}")
    language_code = input("Enter the language code: ")
    if language_code in languages:
        wikipedia.set_lang(language_code)
        print(f"Wikipedia language set to '{languages[language_code]}'.")
    else:
        print("Invalid language code.")

def main():
    wikipedia.set_lang('en')  # Set English as default language
    print("Welcome to the Wikipedia Explorer!")
    while True:
        print("\nOptions:")
        print("1. Search Wikipedia")
        print("2. View a Random Wikipedia Page")
        print("3. Take a Wikipedia Quiz")
        print("4. Manage Favorite Articles")
        print("5. Language Selector")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            query = input("Enter your search query: ")
            search_wikipedia(query)  # Pass the query to the function
        elif choice == '2':
            random_page()
        elif choice == '3':
            quiz()
        elif choice == '4':
            manage_favorites()
        elif choice == '5':
            set_language()
        elif choice == '6':
            print("Exiting program.")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please try again.")

if "__name__"== "_main_":
    main()