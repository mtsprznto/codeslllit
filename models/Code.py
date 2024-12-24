class Code:
    def __init__(self, code):
        self.code = code

    def to_dict(self):
        return {
            'code': self.code
        }