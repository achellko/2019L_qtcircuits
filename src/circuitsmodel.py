import json
import os
import copy


def jsonserializable(skipped_fields=None):
    def _jsonserializable(cls):

        def toJSON(self):
            d = self.__dict__
            if skipped_fields is not None:
                d = {k: v for k, v in d.items() if k not in skipped_fields}
            return json.dumps(d, sort_keys=True, indent=4)

        def __repr__(self):
            return self.toJSON()

        def fromJSON(self, s):
            self.__dict__.update(json.loads(s))

        cls.toJSON = toJSON
        cls.fromJSON = fromJSON
        cls.__repr__ = __repr__

        return cls

    return _jsonserializable


@jsonserializable()
class Circuit(object):
    def __init__(self):
        self.name = None
        self.elements = []
        self.connections = []


@jsonserializable(skipped_fields=['filename'])
class CircuitsStore(object):
    def __init__(self, filename=None):
        self.circuits = []
        self.filename = filename
        if filename is not None:
            if not os.path.exists(filename):
                # po to aby domyślnie tworzyć pusty plik
                self.to_file()
            self.from_file()

    def to_file(self, filename=None):
        if filename is not None and self.filename is None:
            self.filename = filename
        else:
            filename = self.filename

        f = open(filename, "w")
        try:
            f.write(self.toJSON())
        finally:
            f.close()

    def from_file(self, filename=None):
        if filename is not None and self.filename is None:
            self.filename = filename
        else:
            filename = self.filename

        f = open(filename)
        try:
            s = "".join(f.readlines())
            self.fromJSON(s)
        finally:
            f.close()
