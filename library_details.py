from mysql import connector


class Dbconnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="ajiThh**#110",
                database="library_db"
            )
            return self.connection
        except Exception as e:
            return None


class LibraryManager(Dbconnect):

    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = """
            INSERT INTO library
            (book_name, author_name, category, price, quantity, published_year)
            VALUES (%s, %s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connect.commit()

            print("New book added successfully")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM library"
            self.cursor.execute(query)

            records = self.cursor.fetchall()
            return records

        except Exception as e:
            return []

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()

            query = "SELECT * FROM library WHERE id = %s"
            values = (id,)

            self.cursor.execute(query, values)
            record = self.cursor.fetchone()

            return record

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is None:
                print("Book not found..!")
            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            if record is not None:
                query = "DELETE FROM library WHERE id = %s"
                values = (id,)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Book deleted successfully..!")
            else:
                print("Book not found..!")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record is not None:
                self.cursor = self.connect.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                placeholder = placeholder.rstrip(",")

                query = f"UPDATE library SET {placeholder} WHERE id = %s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connect.commit()

                print("Book updated successfully..!")
            else:
                print("Book not found..!")

        except Exception as e:
            print(e)


connection_instance = Dbconnect()
print(connection_instance.get_connection())

library_instance = LibraryManager()
library_instance.post(
    book_name="happpiect man on earth",
    author_name="Eddie Jaku",
    category="Biography",
    price="350",
    quantity=10,
    published_year=1999
)
library_instance.get()
print("_____________________")
library_instance.retrieve(1)
print("-------------")
library_instance.delete(2)
print("-------------")
library_instance.get()
print("-------------")
# library_instance.put(1, book_name="Wings of Fire", author_name="A.P.J. Abdul Kalam", category="Autobiography", price="400", quantity=15, published_year=1999)
library_instance.retrieve(1)