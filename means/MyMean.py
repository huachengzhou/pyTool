class MyMean():

    def __str__(self) -> str:
        return super().__str__() + self.title + "-" + self.value

    def __init__(self, title, value, children=[], desc=""):
        self.title = title
        self.value = value
        self.desc = desc
        self.children = children
