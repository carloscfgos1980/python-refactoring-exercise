__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner():
    characteristic = 'homeowner'

    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs

    def __str__(self):
        return f"Hi, I am {self.name}, a {self.characteristic} and I need {self.needs} to fix things around the house"


alfred = Homeowner("Alfred Alfredson", "Alfredslane 123",
                   ["painter", "plumber"])
bert = Homeowner("Bert Bertson", "Bertslane 231", ["plumber"])

candice = Homeowner("Candice Candicedottir",
                    "Candicelane 312", ["electrician", "painter"])
# Homeowner added
carlos = Homeowner("Carlos Infante", "Klooienberglaan 106",
                   ["electrician", "plumber"])


class Specialist():
    characteristic = 'specialist'
    # Instance method

    def __init__(self, name, pricing):
        self.name = name
        self.pricing = pricing
        # Instance method

    def __str__(self):
        return f"Hi, {self.name}. I am a {self.characteristic} "


class Electrician(Specialist):
    profession = 'electrician'

    def __str__(self):
        return f"Good morning, I am {self.name}, a {self.characteristic} {self.profession} and I charge vor my service {self.pricing} usd per hour"


class Painter(Specialist):
    profession = 'painter'

    def __str__(self):
        return f"Good morning, I am {self.name}, a {self.characteristic} {self.profession} and I charge vor my service {self.pricing} usd per hour"


class Plumber(Specialist):
    profession = 'plumber'

    def __str__(self):
        return f"Good morning, I am {self.name}, a {self.characteristic} {self.profession} and I charge vor my service {self.pricing} usd per hour"


alice = Electrician("Alice Aliceville", 50)
bob = Painter("Bob Bobsville", 40)
craig = Plumber("Craig Craigsville", 30)

# Specialists added:
roberto = Electrician("Roberto Rodriguez", 60)
amet = Painter("Amet Laza", 50)
alain = Plumber("Alan Perez", 25)

# dictionary to be able to loop thru the data of the specialists
profession_available = {
    "electrician": {
        alice.name: alice.pricing,
        roberto.name: roberto.pricing
    },
    "painter": {
        bob.name: bob.pricing,
        amet.name: amet.pricing
    },
    "plumber": {
        craig.name: craig.pricing,
        alain.name: alain.pricing
    }
}

# Function that allows me to find the best deal depending on the need of the Homeowner


def contracts(stuff, client):
    needed_tasks = []
    outcome = []
    for i in range(0, len(client.needs)):  # loop thru the list of homeowner needs
        if client.needs[i] in stuff:  # client.needs[i] represent each of the homeowner needs
            y = stuff[client.needs[i]]
            needed_tasks.append(y)
            # values of the dict, in this case pricing
            all_prices = list(needed_tasks[i].values())
            # key of the dict in this case the name of the person who provide the service
            all_specialists = list(needed_tasks[i].keys())
            cheaper_price = min(all_prices)  # find the minimum price
            # find the index position of the minimum price
            position = all_prices.index(cheaper_price)
            # find the name of the person with the best price
            better_deal = all_specialists[position]
            x = f"task: {client.needs[i]}; name: {better_deal}; price: {cheaper_price} USD per hour"
            outcome.append(x)
    return outcome


if __name__ == "__main__":
    print(f"{alfred.name}'s best contracts available: \n",
          contracts(profession_available, alfred))

    print(f"{bert.name}'s best contracts available: \n",
          contracts(profession_available, bert))

    print(f"{candice.name}'s best contracts available: \n",
          contracts(profession_available, candice))

    print(f"{carlos.name}'s best contracts available: \n",
          contracts(profession_available, carlos))
