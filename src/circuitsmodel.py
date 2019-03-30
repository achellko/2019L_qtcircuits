import json


def jsonserializable(cls):
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __repr__(self):
        return self.toJSON()

    def fromJSON(self, s):
        self.__dict__.update(json.loads(s))

    cls.toJSON = toJSON
    cls.fromJSON = fromJSON
    cls.__repr__ = __repr__

    return cls


@jsonserializable
class Circuit(object):
    def __init__(self):
        self.name = None
        self.elements = []
        self.connections = []


@jsonserializable
class CircuitsContainer(object):
    def __init__(self):
        self.circuits = []

    def to_file(self, filename):
        f = open(filename, "w")
        try:
            f.write(self.toJSON())
        finally:
            f.close()

    def from_file(self, filename):
        f = open(filename)
        try:
            s = f.readlines()
            self.fromJSON(s)
        finally:
            f.close()
