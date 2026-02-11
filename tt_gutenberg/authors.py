from tt_gutenberg.data import load_gutenberg

def list_authors(by_languages=True, alias=True):
    df = load_gutenberg()

    alias_counts = (
        df
        .dropna(subset=["alias", "language"])
        .groupby("alias")
        .size()
        .sort_values(ascending=False)
    )

    return alias_counts.index.tolist()



