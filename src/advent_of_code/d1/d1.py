class ElfDocumentParser:
    def __init__(self):
        self._rows = []
        self._total = 0

    @staticmethod
    def _map_spelled_out_digits(row):
        translate_mapping = {
            "one": "o1e",
            "two": "t2o",
            "three": "t3e",
            "four": "f4r",
            "five": "f5e",
            "six": "s6x",
            "seven": "s7n",
            "eight": "e8t",
            "nine": "n9e",
        }
        for word, replacement in translate_mapping.items():
            row = row.replace(word, replacement)
        return row

    @staticmethod
    def _number_in_row(row):
        row_digits = [c for c in row if c.isdigit()]
        if not row_digits:
            return 0
        digit_10th = int(row_digits[0])
        digit_1 = int(row_digits[-1])
        return digit_10th * 10 + digit_1

    def parse(self, raw_doc):
        """Read in the document"""
        rows = raw_doc.splitlines()
        modified_rows = (self._map_spelled_out_digits(row) for row in rows)
        self._rows = [self._number_in_row(row) for row in modified_rows]
        self._total = sum(self._rows)

    @property
    def rows(self):
        """Return rows of numbers from each row of the document"""
        return self._rows

    @property
    def total(self):
        return self._total


if __name__ == "__main__":
    from os import path
    from pathlib import Path

    path.dirname(__file__)
    target_file = Path(path.dirname(__file__), "input.txt")

    with open(target_file, "r") as file_read:
        input_doc = file_read.read()

    doc_parser = ElfDocumentParser()
    doc_parser.parse(input_doc)

    print(doc_parser.total)
