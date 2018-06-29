class Media:

    # id

    id=0

    # constructor

    def __init__(self, authors, title, price, publisher):

        # attributes

        self.authors = authors
        self.title = title
        self.price = price
        self.publisher = publisher
        Media.id += 1

    def get_net_price(self):
        return self.price * 1.2

    # same as toString() in Java

    def _repr_(self):
        return f"{self.authors}, \"{self.title}\""


class Book(Media):

    def __init__(self, authors, title, price, publisher, n_pages):
        super().__init__(authors, title, price, publisher)
        self.n_pages = n_pages

    def get_net_price(self):
        return self.price * 1.05


class Author:

    def __init__(self, first_name, surname):
        self.first_name = first_name
        self.surname = surname

    def __repr__(self):
        return f"{self.first_name} {self.surname}"


class Publisher:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


# Verification code


if __name__ == "__main__":

        a1 = Author("Francesco", "Bianco")
        a2 = Author("Jiri", "Spicka")

        authors1 = []
        authors2 = []

        authors1.append(a1)

        authors2.append(a1)
        authors2.append(a2)

        p1 = Publisher("Cesati")

        m1 = Media(authors1, "Breve guida alla sintassi italiana", 50, p1)
        print (f"{m1.authors}, \"{m1.title}\" (media), {m1.get_net_price()} euro (VAT incl.), {m1.publisher}")

        b1 = Book(authors2, "Perche scrivere", 50, p1, 600)
        print (f"{b1.authors}, \"{b1.title}\" (book), {b1.get_net_price()} euro (VAT incl.), {b1.publisher}, {b1.n_pages} pages")

