import random   


class Game:     # Skapar klassen "Game" för OOP

    def __init__(self):     # Skapar init metoden som alltid behövs vid början av en class för att instansiera objekt.
        self.playerHand = []
        self.dealerHand = []
        self.deck = ['A', 'A', 'A', 'A', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'K', 'K', 'K', 'K', 'Q', 'Q', 'Q', 'Q']


    def dealOutCard(self, person):  # Metod som delar ut kort till personens hand (antingen spelaren eller dealern)
        card = random.choice(self.deck)     # Använder random som är imported tidigare för att slumpvist välja ett kort från kortleken
        person.append(card)     # Lägger till det slumpade kortet i personens hand
        self.deck.remove(card)      # Tar bort kortet från kortleken


    def startingHand(self):     # Metod som körs i början av programmet och delar då ut 2 kort till båda personers hand
        for i in range(2):
            self.dealOutCard(self.playerHand)
            self.dealOutCard(self.dealerHand)

        if self.playerHand[0] == 'A':    # Om första kortet är ett ESS, byt plats på korten. Annars kan total bli > 21 i början ifall man får A som första kort och andra J, K eller Q (total: 24)
            self.playerHand[0], self.playerHand[1] = self.playerHand[1], self.playerHand[0]
        if self.dealerHand[0] == 'A':
            self.dealerHand[0], self.dealerHand[1] = self.dealerHand[1], self.dealerHand[0]


    def anotherCard(self):      # Metod för att fråga spelaren om denne vill dra nytt kort, samt delar ut kort till dealern
        while True:
            while self.totalHandValue(self.dealerHand) < 16:     # Delar ut kort till dealern så länge den har total under 16
                self.dealOutCard(self.dealerHand)
            newCard = input(f"Your hand consists of {self.playerHand} for a total of {self.totalHandValue(self.playerHand)}, while the dealer has a {self.dealerHand[0]} and X. Do you want another card? (y/n) ").lower()      # Frågar om man vi dra ett nytt kort
            if newCard == 'y':
                self.dealOutCard(self.playerHand)       # Delar ut kort till spelaren om denne valt ja
                if self.totalHandValue(self.playerHand) > 21:      # Om spelaren får en total över 21 förlorar denne och därmed går vi till winner metoden som informerar om det och loopen stoppas med break
                    self.winner()
                    break
            elif newCard == 'n':        # Om spelaren inte vill dra ett nytt kort anropas också winner funktionen som visar vem som vann och loopen stoppas
                self.winner()
                break
            else:
                print('Wrong input. Enter "y" for yes or "n" for no\n')     # Om spelaren skriver något annat än y eller n kommer loopen att köra om och man väljer igen


    def totalHandValue(self, person):       # Metod för att räkna ut total value för respektive persons hand
        personTotal = 0     
        for personCard in person:       # For loop som går igenom varje kort i personens hand
            if personCard == 'A':
                if personTotal > 8:    # Ess värt 1 om playertotal är över 8 (så att man inte går över 21)
                    personTotal += 1
                else:
                    personTotal += 14   # Annars ess värt 14 (som stod i instruktionerna för uppgiften)
            elif personCard == 'J' or personCard == 'K' or personCard == 'Q':       # Klätt kort är värt 10
                personTotal += 10
            else:
                personTotal = personTotal + int(personCard)     # Annars är det ett nummer, och det plussas då på totalen
        return personTotal


    def winner(self):       # Metoden som anropas vid spelets slut som visar vem som vinner beroende på totala värdet av deras hand
        if self.totalHandValue(self.playerHand) > 21 or (self.totalHandValue(self.playerHand) > 21 and self.totalHandValue(self.dealerHand) > 21):      # Om spelaren får över 21, eller båda får över 21, vinner dealern
            print(f"Your hand {self.playerHand} totals {self.totalHandValue(self.playerHand)} which means you bust! Dealer wins!")
        elif self.totalHandValue(self.dealerHand) > 21 and self.totalHandValue(self.playerHand) <= 21:      # Om endast dealern får över 21, vinner spelaren
            print(f"The dealer bust with their hand {self.dealerHand} for a total of {self.totalHandValue(self.dealerHand)}, you win!")
        elif self.totalHandValue(self.playerHand) == 21 and self.totalHandValue(self.dealerHand) == 21:     # Om båda får 21, är det push (oavgjort)
            print(f"Your hand {self.playerHand} totals 21 and dealers hand {self.dealerHand} also totals 21. Both got blackjack, it's a tie!")
        elif self.totalHandValue(self.playerHand) == self.totalHandValue(self.dealerHand):      # Om båda får samma värde t.ex. 16 16, vinner dealern
            print(f"Your hand {self.playerHand} totals {self.totalHandValue(self.playerHand)} and the dealers hand {self.dealerHand} also totals {self.totalHandValue(self.dealerHand)}. Dealer wins!")
        else:   
            if self.totalHandValue(self.playerHand) > self.totalHandValue(self.dealerHand):     # Annars om spelarens totala är över dealerns, vinner spelaren
                print(f"Your hand {self.playerHand} totals {self.totalHandValue(self.playerHand)} and the dealers hand {self.dealerHand} totals {self.totalHandValue(self.dealerHand)}. You win!")
            else:       # Annars vinner dealern
                print(f"Your hand {self.playerHand} totals {self.totalHandValue(self.playerHand)} and the dealers hand {self.dealerHand} totals {self.totalHandValue(self.dealerHand)}. Dealer wins!")


game = Game()       # Skapar instans för att starta upp spelet i main

def main():
    game.startingHand()
    game.anotherCard()

main()      # Startar upp programmet