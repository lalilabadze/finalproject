import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
            car_id INTEGER PRIMARY KEY AUTOINCREMENT,
            manufacturer TEXT NOT NULL,
            model TEXT NOT NULL)''')
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS info (
            cid INTEGER,
            color TEXT,
            date TEXT,
            price REAL,
            FOREIGN KEY(cid) REFERENCES cars(car_id))''')

        self.connection.commit()

    def close(self):
        self.connection.close()

class Car:
    def __init__(self, manufacturer, model, color=None, date=None, price=None):
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.date = date
        self.price = price
        self.car_id = None

    def insert_car(self, db):
        
        db.cursor.execute('''INSERT INTO cars (manufacturer, model) VALUES (?, ?)''', 
                          (self.manufacturer, self.model))
        db.connection.commit()
        self.car_id = db.cursor.lastrowid

        
        if self.color or self.date or self.price:
            db.cursor.execute('''INSERT INTO info (cid, color, date, price) VALUES (?, ?, ?, ?)''',
                              (self.car_id, self.color, self.date, self.price))
            db.connection.commit()

    def update_info(self, db, color=None, date=None, price=None):
        if color:
            db.cursor.execute('''UPDATE info SET color = ? WHERE cid = ?''', (color, self.car_id))
        if date:
            db.cursor.execute('''UPDATE info SET date = ? WHERE cid = ?''', (date, self.car_id))
        if price:
            db.cursor.execute('''UPDATE info SET price = ? WHERE cid = ?''', (price, self.car_id))
        db.connection.commit()

class CarManager:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def add_car(self):
        manufacturer = input("მიმდინარე მწარმოებელი: ")
        model = input("მოდელი: ")
        color = input("ფერი (თუ არ არის, დააკლიკეთ 'Enter'): ")
        date = input("წარმოების თარიღი (yyyy-mm-dd): ")
        price = input("ფასი: ")

        car = Car(manufacturer, model, color, date, float(price) if price else None)
        car.insert_car(self.db)
        print("ავტომობილი წარმატებით დაემატა!")

    def update_car_info(self):
        car_id = int(input("შეიყვანეთ car_id, რომლის ავტომობილისთვისაც გსურთ ინფორმაციის განახლება: "))
        color = input("ახალი ფერი (თუ არ არის, დააკლიკეთ 'Enter'): ")
        date = input("ახალი წარმოების თარიღი (yyyy-mm-dd): ")
        price = input("ახალი ფასი: ")

        car = Car('', '')
        car.car_id = car_id
        car.update_info(self.db, color if color else None, date if date else None, float(price) if price else None)
        print("ინფორმაცია წარმატებით განახლდა!")

    def delete_car(self):
        car_id = int(input("შეიყვანეთ car_id, რომლის ავტომობილი უნდა წაიშალოს: "))
        self.db.cursor.execute('''DELETE FROM cars WHERE car_id = ?''', (car_id,))
        self.db.cursor.execute('''DELETE FROM info WHERE cid = ?''', (car_id,))
        self.db.connection.commit()
        print("ავტომობილის მონაცემები წარმატებით წაიშალა!")

    def show_cars_by_date(self):
        year = input("შეიყვანეთ წელი (yyyy), რომლითაც დაინტერესებული ხართ: ")
        self.db.cursor.execute('''SELECT cars.manufacturer, cars.model, info.color, info.price 
                                  FROM cars 
                                  JOIN info ON cars.car_id = info.cid 
                                  WHERE info.date LIKE ? 
                                  ORDER BY info.date''', 
                               (f"{year}%",))
        rows = self.db.cursor.fetchall()
        
        if rows:
            print(f"\n{year}-წლის ავტომობილები:")
            for row in rows:
                print(f"მწარმოებელი: {row[0]}, მოდელი: {row[1]}, ფერი: {row[2]}, ფასი: {row[3]}$")
        else:
            print(f"{year}-წლისთვის არ არსებობს მონაცემები.")

    def show_menu(self):
        while True:
            print("\nმენიუ:")
            print("1. ახალი ავტომობილის დამატება")
            print("2. ავტომობილის მონაცემების განახლება")
            print("3. ავტომობილის წაშლა")
            print("4. ავტომობილების სიის გამოჩენა გამოშვების წლის მიხედვით")
            print("5. გამოსვლა")

            choice = input("აირჩიეთ მოქმედება: ")

            if choice == '1':
                self.add_car()
            elif choice == '2':
                self.update_car_info()
            elif choice == '3':
                self.delete_car()
            elif choice == '4':
                self.show_cars_by_date()
            elif choice == '5':
                self.db.close()
                break
            else:
                print("არასწორი არჩევანი, სცადეთ კვლავ.")

if __name__ == "__main__":
    car_manager = CarManager("cars.db")
    car_manager.show_menu()
