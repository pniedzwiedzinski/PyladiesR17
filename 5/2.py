class Czlowiek:
    def __init__(self):
        imie = "noname"
        wzrost = 0
        waga = 0

    def speak(self):
        print("Mowie prawde")

    def count_bmi(self):
        pass

    def diff_to_norm(self):
        pass

    def save_data(self):
        pass

    def to_burn(self):
        pass

    def to_eat(self):
        pass

    def what_to_do(self):
        pass

class Polityk(Czlowiek):
    def speak(self):
        if self.recive_bribe()==True:
            super().speak()
        else:
            print("Klamie, bo moge")

    def recive_bribe(self):
        return True


czlowiek = Polityk()
czlowiek.recive_bribe()
czlowiek.speak()
czlowiek.wzrost=154
czlowiek.waga = 70
print(czlowiek.count_bmi())