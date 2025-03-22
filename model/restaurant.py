class Restaurant:
    def __init__(self, id: int, name: str, description: str, capacity: int, opening_hours: str, location: str, is_active: bool):
        self.id = id
        self.name = name
        self.description = description
        self.capacity = capacity
        self.opening_hours = opening_hours
        self.location = location
        self.is_active = is_active

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.id}) - {self.description}, \n\
Capacité: {self.capacity}\n\
Horraires: {self.opening_hours}\n\
Emplacement: {self.location}\n\
Ouvert: {self.is_active}"

