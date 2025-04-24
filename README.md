# 🧠 Interactive Wikipedia Scraper

A **Python-based GUI application** for scraping and interacting with Wikipedia content using the Wikipedia API. Designed with modularity and ease-of-use in mind, this tool allows users to query Wikipedia and view clean, structured summaries with a few simple clicks.

---

## 📌 Project Overview

This project aims to develop an **interactive Python application** for retrieving Wikipedia content via its API, presented through a **user-friendly graphical user interface (GUI)**.

### 💡 Key Features

- 🔎 **Search Wikipedia** articles interactively.
- 📄 **View summaries** of articles in a clean layout.
- 🎯 **Select categories/topics** for focused information extraction.
- 🌐 **Multilingual support** (optional feature).
- 🧩 **Modular design** for easy enhancement or new feature integration.
- 💾 **Save favorites** for later access (optional enhancement).
- ❓ **Quiz mode** for learning and exploration.



## 🚀 Technologies Used

- 🐍 **Python 3.x**
- 🖼️ **Tkinter**
- 📡 **Wikipedia API**
- 🌐 **Flask** (for web integration)
- 🧰 **Requests**, **JSON**, etc.

---

## 📁 Project Structure

```
├── static/                       
│   └──  script.js                    
├── templates/              
│   └── index.html/                 
├── app.py                        # Main script for scrapping
├── README.md                     # Project documentation
├── requirements.txt              # List of dependencies for the project
└── .gitignore                    # Git ignore file (if using Git)
├── wikiGUI.py                    # optional GUI based python file 
└── wikiscrapper.py               # just basic terminal based python file
```


## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/farhat-1203/WebScrapping.git
   ```
2. Navigate to the project directory:
   ```bash
   cd WebScrapping
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4.  **Run the main script**:
    Run the flask file for accessing:
    ```bash
    python app.py
    ```
