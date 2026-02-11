import pandas as pd

AUTHORS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
LANGUAGES_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"

def load_gutenberg():
    gutenberg_authors = pd.read_csv(AUTHORS_URL)
    gutenberg_languages = pd.read_csv(LANGUAGES_URL)

    df = pd.merge(
        gutenberg_authors,
        gutenberg_languages,
        on="gutenberg_author_id",
        how="inner"
    )

    return df
