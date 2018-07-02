# Not finished on July 2nd, thus it doesn't work

import abc


class Media(metaclass=abc.ABCMeta):

    id = 1

    # constructor

    def __init__(self, authors, title, price, publisher):

        # attributes

        self.authors = authors
        self.title = title
        self.price = price
        self.publisher = publisher
        self.id = Media.id

        Media.id += 1

    @abc.abstractmethod
    def get_net_price(self):...


    def _repr_(self):
        auth = ""
        i = 0
        while i < len(self.authors):
            auth += (f"{self.authors[i]}, ")
            i += 1
        return f"Item # {self.id}: {auth}\"{self.title}\", {self.get_net_price()} EUR (brut price {self.price} EUR), {self.publisher}"


class Book(Media):

    def __init__(self, authors, title, price, publisher, n_pages):
        super().__init__(authors, title, price, publisher)
        self.n_pages = n_pages

    def get_net_price(self):
        return round(self.price * 1.05)

    def _repr_(self):
        return f"{super()._repr_()}, {self.n_pages} pages"


class CD(Media):

    def __init__(self, authors, title, price, publisher, n_tracks):
        super().__init__(authors, title, price, publisher)
        self.n_tracks = n_tracks

    def get_net_price(self):
        return round(self.price * 1.20)

    def _repr_(self):
        return f"{super()._repr_()}, {self.n_tracks} tracks"

class DVD(Media):

    def __init__(self, authors, title, price, publisher, zone):
        super().__init__(authors, title, price, publisher)
        if zone >= 0 and zone <= 8:
            self.zone = zone
        else:
            self.zone = 0

    def get_net_price(self):
        return round(self.price * 1.2 * 0.8)

    def _repr_(self):
        return f"{super()._repr_()}, zone {self.zone}"


class Author:

    id = 1

    def __init__(self, first_name="", surname=""):
        self.first_name = first_name
        self.surname = surname
        self.id = Author.id

        Author.id += 1

    def __repr__(self):
        return f"{self.first_name} {self.surname}"


class Publisher:

    def __init__(self, name, place=""):
        self.name = name
        self.place = place

    def __repr__(self):
        if self.place != "":
            return f"{self.name}, {self.place}"
        else:
            return self.name


class CartRow:

    def __init__(self, media = None):
        self.media = media
        self.quantity = 1

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1


class Cart:

    def __init__(self):

        self.cart_rows = []

    def get_total_net_price:
        total_net_price = 0
        for row in self.cart_rows:
            total_net_price += media.get_net_price()
        return total_net_price

    def add_media(self, media):
        for row in self.cart_rows:
            if row



# Verification code


if __name__ == "__main__":

        a1 = Author("Francesco", "Bianco")
        a2 = Author("Jiri", "Spicka")
        a3 = Author("Stefano", "Rosso")
        a4 = Author("Babalot")
        a5 = Author("Joel", "Coen")
        a6 = Author("Ethan", "Coen")

        authors1 = []
        authors2 = []
        authors3 = []
        authors4 = []
        authors5 = []

        authors1.append(a1)

        authors2.append(a1)
        authors2.append(a2)

        authors3.append(a3)

        authors4.append(a4)

        authors5.append(a5)
        authors5.append(a6)

        p1 = Publisher("Cesati", "Firenze")
        p2 = Publisher("RCA italiana")
        p3 = Publisher("Aiuola dischi")
        p4 = Publisher("Working Title Films")


        b1 = Book(authors1, "Breve guida alla sintassi italiana", 50, p1, 120)
        b2 = Book(authors2, "Perche scrivere", 48, p1, 600)
        c1 = CD(authors3, "Una storia disonesta", 15, p2, 11)
        c2 = CD(authors4, "Che succede quando uno muore", 20, p3, "14 (+ 1 ghost)")
        d1 = DVD(authors5, "The Big Lebowski", 30, p4, 1)

        items =[b1, b2, c1, c2, d1]

        print ("\nItems in the list:\n")

        for item in items:
            print (f"{item._repr_()}\n")

        print ("Authors in the list:\n")

        id_list = []
        for item in items:
            for author in item.authors:
                if id_list.count(author.id) == 0:
                    id_list.append(author.id)
                    print (f"{author.id} {author}")


