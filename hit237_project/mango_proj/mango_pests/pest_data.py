class MangoPestDisease:
    """Sample class for pest data (minimal version for testing)"""
    def __init__(self, id, name, brief_desc, image):
        self.id = id
        self.name = name
        self.brief_desc = brief_desc
        self.image = image

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brief_desc': self.brief_desc,
            'image': self.image
        }