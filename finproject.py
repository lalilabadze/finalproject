"""ამოცანა N1: (10 ქულა)შექმენით კლასი “CalcCentury”. რომელიც განახორციელებს ექზემპლიარის(ობიექტის) ინიციალიზაციას და
 ინტერაქტიულ რეჟიმში მიიღებს პიროვნების დაბადების წელს.


კლასში გაწერეთ  “calcAge()” მეთოდი, რომელიც დაიანგარიშებს პიროვნების ასაკს. ასევე, 
იმავე კლასში გაწერეთ მეთოდი “century()”, რომელიც დაიანგარიშებს თუ რომელ საუკუნეს
 ეკუთვის პიროვნების შეტანილი დაბადების წელი. პროგრამაში გააკონტროლეთ შეტანილი მნიშვნელობების სისწორე,
  მაგ. სადაც ციფრულ მნიშვნელობის შეტანას ველოდებით, არ უნდა მოხდეს სიმბოლოების შეტანა და ა.შ.

პროგრამის მუშაობის მაგალითი:

ვთქვათ შეტანილია 1985 წელი. “CalcCentury” კლასის ბაზაზე ექზემპლიარის შექმნის შემდეგ, გამოიძახეთ 
“calcAge()” და “century()” მეთოდები, რომლებიც გამოითვლის პიროვნების ასაკს და საუკუნეს. 
შედეგებს კი გამოიტანს ეკრანზე შემდეგი სახით:

“პიროვენება დაიბადა მე-20 საუკუნეში და არის 38 წლის“."""

class CalcCentury:
    def __init__(self):
        self.birth_year = 0  
    
    def calcAge(self):
       
        current_year = 2025
        age = current_year - self.birth_year
        return age
    
    def century(self):
        
        century = (self.birth_year - 1) // 100 + 1
        return century

    def setBirthYear(self):
       
        while True:
            try:
                self.birth_year = int(input("გთხოვთ შეიყვანოთ თქვენი დაბადების წელი: "))
                if self.birth_year <= 0 or self.birth_year > 2025:
                    print("შეიყვანეთ სწორი დაბადების წელი (0-დან 2025-მდე).")
                else:
                    break
            except ValueError:
                print("გთხოვთ, შეიყვანოთ ციფრული მნიშვნელობა.")
    
    def displayInformation(self):
        age = self.calcAge()
        century = self.century()
        print(f"თქვენი ასაკი არის: {age} წელი")
        print(f"თქვენი დაბადების წელი ეკუთვნის {century}-ე საუკუნეს.")


if __name__ == "__main__":
    calc = CalcCentury()
    calc.setBirthYear()
    calc.displayInformation()
