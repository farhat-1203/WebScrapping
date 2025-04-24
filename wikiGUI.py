import wikipedia
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

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
        result = f"\nTitle: {page.title}\nSummary: {page.summary}\nURL: {page.url}"
        result_text.set(result) 
    except wikipedia.exceptions.PageError as e:
        result_text.set(f"Error: {e}")
    except wikipedia.exceptions.DisambiguationError as e:
        result_text.set(f"DisambiguationError: This term may refer to multiple articles. Please specify.\nSuggestions: {', '.join(e.options)}")

def random_page():
    try:
        page = wikipedia.random()
        page = wikipedia.page(page)
        result_text.set(f"\nRandom Wikipedia Page:\nTitle: {page.title}\nSummary: {page.summary}\nURL: {page.url}")
        result_label.config(font=("Arial", 12))  # Adjust font size here
    except Exception as e:
        result_text.set(f"Error: {e}")

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

    # Select two random questions
    quiz_questions = random.sample(questions, 2)

    score = 0
    for question, answer in quiz_questions:
        user_answer = simpledialog.askstring("Quiz", question)
        if user_answer and user_answer.lower() == answer.lower():
            score += 1

    messagebox.showinfo("Quiz Result", f"Your score: {score}/{len(quiz_questions)}")

    result_label.config(font=("Arial", 14))  # Adjust font size here


def manage_favorites():
    global favorite_articles
    manage_favorites_window = tk.Toplevel(root)
    manage_favorites_window.title("Manage Favorite Articles")

    def add_favorite():
        article_title = article_entry.get()
        favorite_articles.append(article_title)
        messagebox.showinfo("Success", f"'{article_title}' has been added to favorites.")

    def remove_favorite():
        article_title = article_entry.get()
        if article_title in favorite_articles:
            favorite_articles.remove(article_title)
            messagebox.showinfo("Success", f"'{article_title}' has been removed from favorites.")
        else:
            messagebox.showinfo("Error", f"'{article_title}' is not in favorites.")

    def view_favorites():
        favorites_text.set("\nFavorite Articles:\n" + '\n'.join(favorite_articles))

    article_label = tk.Label(manage_favorites_window, text="Enter the title of the article:")
    article_label.pack()
    article_entry = tk.Entry(manage_favorites_window)
    article_entry.pack()

    add_button = tk.Button(manage_favorites_window, text="Add to favorites", command=add_favorite)
    add_button.pack()
    remove_button = tk.Button(manage_favorites_window, text="Remove from favorites", command=remove_favorite)
    remove_button.pack()
    view_button = tk.Button(manage_favorites_window, text="View favorites", command=view_favorites)
    view_button.pack()

    favorites_text = tk.StringVar()
    favorites_label = tk.Label(manage_favorites_window, textvariable=favorites_text)
    favorites_label.pack()

    result_label.config(font=("Arial", 14))  # Adjust font size here


def set_language():
    def set_lang():
        language_code = language_entry.get()
        if language_code in languages:
            wikipedia.set_lang(language_code)
            messagebox.showinfo("Success", f"Wikipedia language set to '{languages[language_code]}'.")
        else:
            messagebox.showinfo("Error", "Invalid language code.")

    set_language_window = tk.Toplevel(root)
    set_language_window.title("Language Selector")

    language_label = tk.Label(set_language_window, text="Enter the language code:")
    language_label.pack()
    language_entry = tk.Entry(set_language_window)
    language_entry.pack()

    set_button = tk.Button(set_language_window, text="Set Language", command=set_lang)
    set_button.pack()

    result_label.config(font=("Arial", 14))  # Adjust font size here


def search():
    query = query_entry.get()
    search_wikipedia(query)

root = tk.Tk()
root.title("Wikipedia Explorer")

query_label = tk.Label(root, text="Enter your search query:", font=("Arial", 14))  # Increase font size
query_label.pack()
# Elongated search bar with bigger font size
query_entry = tk.Entry(root, width=70, font=("Arial", 14))  # Adjust the width and font size of the entry field
query_entry.pack()

search_button = tk.Button(root, text="Search", command=search, width=20, height=2)  # Adjust the width and height of the button
search_button.pack()

options_frame = tk.Frame(root)
options_frame.pack()

random_page_button = tk.Button(options_frame, text="View Random Wikipedia Page", command=random_page, width=30, height=2)  # Adjust the width and height of the button
random_page_button.grid(row=0, column=0, padx=5, pady=5)

quiz_button = tk.Button(options_frame, text="Take Wikipedia Quiz", command=quiz, width=30, height=2)  # Adjust the width and height of the button
quiz_button.grid(row=0, column=1, padx=5, pady=5)

manage_favorites_button = tk.Button(options_frame, text="Manage Favorite Articles", command=manage_favorites, width=30, height=2)  # Adjust the width and height of the button
manage_favorites_button.grid(row=0, column=2, padx=5, pady=5)

set_language_button = tk.Button(options_frame, text="Set Language", command=set_language, width=20, height=2)  # Adjust the width and height of the button
set_language_button.grid(row=0, column=3, padx=5, pady=5)

exit_button = tk.Button(options_frame, text="Exit", command=root.quit, width=20, height=2)  # Adjust the width and height of the button
exit_button.grid(row=0, column=4, padx=5, pady=5)

result_text = tk.StringVar()
# Adjust the layout of the result_label to display multiple lines of text
result_label = tk.Label(root, textvariable=result_text, wraplength=500, justify="left", anchor="w")
result_label.pack(fill="both", padx=10, pady=10, expand=True)

root.mainloop()