class Character:
    def __init__(self, character_id, name, image, killer_id, season):
        self.character_id = character_id
        self.name = name
        self.image = image
        self.killer_id = killer_id
        self.season = season

    def toString(self):
        return '[character_id] {0}, [name] {1} [image] {2}  [killer_id] {3} [season] {4}'.format(
            self.character_id, self.name, self.image, self.killer_id, self.season)

