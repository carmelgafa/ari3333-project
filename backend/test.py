import pandas as pd

# Define the data for the DataFrame
data = {
    "id": range(1, 11),
    "book title": [
        "To Kill a Mockingbird", "Pride and Prejudice", "1984",
        "The Great Gatsby", "Moby Dick", "War and Peace",
        "The Catcher in the Rye", "The Hobbit", "Crime and Punishment",
        "The Adventures of Huckleberry Finn"
    ],
    "author": [
        "Harper Lee", "Jane Austen", "George Orwell",
        "F. Scott Fitzgerald", "Herman Melville", "Leo Tolstoy",
        "J.D. Salinger", "J.R.R. Tolkien", "Fyodor Dostoevsky",
        "Mark Twain"
    ],
    "genre": [
        "Fiction", "Romance", "Dystopian",
        "Fiction", "Adventure", "Historical",
        "Fiction", "Fantasy", "Crime",
        "Adventure"
    ],
    "summary": [
        "A novel about racial injustice in the Deep South.",
        "A story of love and social standing in 19th century England.",
        "A dystopian social science fiction novel and cautionary tale.",
        "A critique of the American Dream set in the Roaring Twenties.",
        "A sailor's narrative of the obsessive quest of Ahab.",
        "A depiction of Russian society during the Napoleonic Era.",
        "The challenges of teenage rebellion and identity.",
        "A fantasy about a hobbit's quest to reclaim a lost kingdom.",
        "The psychological depth of a man's struggle with morality.",
        "A journey down the Mississippi River with a runaway slave."
    ]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('books.csv', index=False)
