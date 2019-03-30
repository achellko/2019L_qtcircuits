from circuitsmodel import *
import unittest


class CircuitsModelTest(unittest.TestCase):
    def test_circuit_to_json(self):
        expected = """{
    "connections": [],
    "elements": [],
    "name": "jakas ladna \\\"nazwa\"
}"""

        c = Circuit()
        c.name = "jakas ladna \"nazwa"

        #print(c.toJSON())
        self.assertEqual(c.toJSON(), expected)


    def test_circuit_from_json(self):
        s = """{
    "data": {
        "connections": [],
        "elements": [],
        "name": "Podwajacz napięcia"
    }
}"""
        c = Circuit()
        c.fromJSON(s)
        self.assertEqual("Podwajacz napięcia", c.data["name"])
        self.assertEqual([], c.data["elements"])
        self.assertEqual([], c.data["connections"])

    def test_model_to_file(self):
        s = """{
\"connections\": [],
\"elements\": [],
\"name\": "Podwajacz napięcia"
}"""
        expected = """{
    "circuits": [
        {
            "connections": [],
            "elements": [],
            "name": "Podwajacz napi\\u0119cia"
        }
    ]
}"""
        c = Circuit()
        c.fromJSON(s)
        cm = CircuitsContainer()
        cm.circuits.append(c)

        import tempfile
        with tempfile.TemporaryDirectory() as tdir:
            fname = f"{tdir}/cm_file_test.json"
            # print(f"Tworzę plik testowy {fname}")
            cm.to_file(fname)

            with open(fname) as f:
                s = f.read(100000)
                #print(s)

                self.assertEqual(s, expected)

    def test_przyklad(self):
        wartosc_do_sprawdzenia = str(sum([1, 2, 3]))
        oczekiwana = "6"
        komunikat = "powinna być szóstka"
        self.assertEqual(wartosc_do_sprawdzenia, oczekiwana, komunikat)


if __name__ == "__main__":
    unittest.main()

