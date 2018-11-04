class Course:
    def __init__(self, name, abbrev, id):
        self.name = name
        self.abbrev = abbrev
        self.id = id

    def __repr__(self):
        return f"course('{self.name}', '{self.abbrev}', '{self.id}')"

    def __hash__(self):
        return hash(self.id)