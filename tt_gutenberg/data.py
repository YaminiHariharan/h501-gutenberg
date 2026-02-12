import pandas as pd

AUTHORS_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
LANGUAGES_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

def load_gutenberg():
    gutenberg_authors = pd.read_csv(AUTHORS_URL)
    gutenberg_meta = pd.read_csv(LANGUAGES_URL)

    df = pd.merge(
        gutenberg_authors,
        gutenberg_meta,
        on="gutenberg_author_id",
        how="inner"
    )

    return df
