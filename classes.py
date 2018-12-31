class Musician(object):
  def __init__ (self, sounds):
    self.sounds = sounds
  def solo(self, length):
      for i in range(length):
          print(self.sounds[i % len(self.sounds)], end=" ")
      print()

class Bassist(Musician):
  def __init__(self):
    super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
  def __init__(self):
    super().__init__(["Boink", "Bow", "Boom"])
  
  def tune(self):
    print("Be with oyu in a moment")
    print("Twoing, sproing, splang")

class Drummer(Musician):
  def __init__(self):
    super().__init__(["Slam", "Clang", "Brrrrrr"])
  
  def countDown(self):
    print("1, 2 ,3, 4")

  def gettingHot(self): 
    print("wow is it ever hot in here")

  def combust(self):
    print("BLAAAMMM")

john_bonham = Drummer()
robert_plant = Bassist()
jimmy_page = Guitarist()

def playConcert():
  john_bonham.countDown()
  jimmy_page.tune()
  john_bonham.countDown()
  jimmy_page.solo(3)
  robert_plant.solo(3)
  john_bonham.solo(8)
  john_bonham.gettingHot()
  john_bonham.solo(2)
  john_bonham.combust()
playConcert()
