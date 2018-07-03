import abc


class Media(metaclass=abc.ABCMeta):

    id = 1  # global variable (accessible by all instances of the class)

    # constructor

    def __init__(self, authors, title, price, publisher):

        # attributes

        self.authors = authors
        self.title = title
        self.price = price
        self.publisher = publisher
        self.id = Media.id  # gets global variable id as instance unique id

        Media.id += 1   # increments the global variable, to give all instances a unique id

    @abc.abstractmethod
    def get_net_price(self):...

    # repr function

    def _repr_(self):
        auth = ""
        i = 0
        while i < len(self.authors):
            auth += (f"{self.authors[i]}, ")
            i += 1
        return f"{auth}\"{self.title}\", {self.get_net_price()} " \
               f"EUR (brut price {self.price} EUR), {self.publisher}"


class Book(Media):

    # constructor

    def __init__(self, authors, title, price, publisher, n_pages):
        super().__init__(authors, title, price, publisher)

        # new attributes

        self.n_pages = n_pages

    # functions

    def get_net_price(self):
        return round(self.price * 1.05)

    # repr function

    def _repr_(self):
        return f"{super()._repr_()}, {self.n_pages} pages"


class CD(Media):

    # constructor

    def __init__(self, authors, title, price, publisher, n_tracks):
        super().__init__(authors, title, price, publisher)

        # new attributes

        self.n_tracks = n_tracks

    # functions

    def get_net_price(self):
        return round(self.price * 1.20)

    # repr function

    def _repr_(self):
        return f"{super()._repr_()}, {self.n_tracks} tracks"


class DVD(Media):

    # constructor

    def __init__(self, authors, title, price, publisher, zone):
        super().__init__(authors, title, price, publisher)

        # new attributes

        self.zone = zone

    # functions

    def get_net_price(self):
        return round(self.price * 1.2 * 0.8)

    # repr function

    def _repr_(self):
        return f"{super()._repr_()}, zone {self.zone}"


class Author:

    id = 1  # global variable (accessible by all instances of the class)

    # constructor

    def __init__(self, first_name="", surname=""):

        # attributes

        self.first_name = first_name
        self.surname = surname
        self.id = Author.id # gets global variable id as instance unique id

        Author.id += 1  # increments the global variable, to give all instances a unique id

    # repr function

    def __repr__(self):
        if self.surname != "":
            return f"{self.first_name} {self.surname}"
        else:
            return self.first_name


class Publisher:

    id = 1  # global variable (accessible by all instances of the class)

    def __init__(self, name, place=""):
        self.name = name
        self.place = place

        Publisher.id += 1   # increments the global variable, to give all instances a unique id

    # repr function

    def __repr__(self):
        if self.place != "":
            return f"{self.name}, {self.place}"
        else:
            return self.name


class CartRow:

    # constructor

    def __init__(self, media = None):

        # attributes

        self.media = media
        self.quantity = 1

    # functions

    def increment(self):
        self.quantity += 1

    def decrement(self):
        self.quantity -= 1


class Cart:

    # constructor

    def __init__(self):

        # attributes

        self.cart_rows = []

    # functions

    def get_total_net_price(self):
        total_net_price = 0
        for row in self.cart_rows:
            total_net_price += row.media.get_net_price() * row.quantity
        return total_net_price

    def add_media(self, media):
        is_in_cart = False
        for row in self.cart_rows:
            if row.media == media:
                is_in_cart = True
                row.increment()
                break
        if is_in_cart == False:
            self.cart_rows.append(CartRow(media))

    def remove_media(self, media):
        for row in self.cart_rows:
            if row.media == media:
                if row.quantity < 2:
                    self.cart_rows.remove(row)
                else:
                    row.decrement()

    def get_media_copies(self):
        media_copies = 0
        for row in self.cart_rows:
            media_copies += row.quantity;
        return media_copies

    # repr function

    def __repr__(self):
        return f"Cart: {len(self.cart_rows)} medias " \
               f"({self.get_media_copies()} copies), {self.get_total_net_price()} Eur"


# Verification code (main)

if __name__ == "__main__":

        # set authors

        a1 = Author("Francesco", "Bianco")
        a2 = Author("Jiri", "Spicka")
        a3 = Author("Stefano", "Rosso")
        a4 = Author("Babalot")
        a5 = Author("Joel", "Coen")
        a6 = Author("Ethan", "Coen")

        # create empty lists of authors

        authors1 = []
        authors2 = []
        authors3 = []
        authors4 = []
        authors5 = []

        # set lists of authors
        # lists nn. 2 and 6 are composed of 2 authors each

        authors1.append(a1)

        authors2.append(a1)
        authors2.append(a2)

        authors3.append(a3)

        authors4.append(a4)

        authors5.append(a5)
        authors5.append(a6)

        # set publishers

        p1 = Publisher("Cesati", "Firenze")
        p2 = Publisher("RCA italiana")
        p3 = Publisher("Aiuola dischi")
        p4 = Publisher("Working Title Films")

        # set medias

        b1 = Book(authors1, "Breve guida alla sintassi italiana", 11, p1, 120)
        b2 = Book(authors2, "Perche scrivere", 48, p1, 600)
        c1 = CD(authors3, "Una storia disonesta", 15, p2, 11)
        c2 = CD(authors4, "Che succede quando uno muore", 20, p3, "14 (+ 1 ghost)")
        d1 = DVD(authors5, "The Big Lebowski", 30, p4, 1)

        # set a collection of medias

        medias =[b1, b2, c1, c2, d1]

        # Test n. 1: display the medias in the collection

        print ("\nMedias in the list:\n")
        for media in medias:
            print (f"Media # {media.id}:    {media._repr_()}")

        # Test n. 2: display the authors of the medias in the collection

        print ("\nAuthors in the list:\n")
        id_list = []
        for media in medias:
            for author in media.authors:
                if id_list.count(author.id) == 0:
                    id_list.append(author.id)
                    print (f"Author # {author.id}:  {author}")

        # Test n. 3: create an empty cart

        print ("\nContent of the cart:\n")

        cart1 = Cart()
        print(f"[Empty cart]                        {cart1}")

        # Test n. 4: add two copies of b1 (book) and one copy of c1 (cd)

        cart1.add_media(b1)
        cart1.add_media(b1)
        cart1.add_media(c1)
        print(f"[Add 2 copies of a book and 1 cd]   {cart1}")

        # Test n. 5: add another copy of the book

        cart1.add_media(b1)
        print(f"[Add 1 copy of the book]            {cart1}")

        # Test n. 6: remove one copy of the book

        cart1.remove_media(b1)
        print(f"[Remove 1 copy of the book]         {cart1}")



