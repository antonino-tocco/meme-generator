class QuoteModel:
    """A class to represent a quote."""
    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'QuoteModel: {self.body} - {self.author}'