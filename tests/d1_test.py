from advent_of_code.d1 import ElfDocumentParser


class TestDay1:
    def test__elf_document_parser__read_rows(self):
        parser_uut = ElfDocumentParser()

        test_doc = """1foo2h
        6ba5r
        wee0e!8===1\
        """

        parser_uut.parse(test_doc)

        actual_numbers = parser_uut.rows
        expected_numbers = [12, 65, 1]

        assert actual_numbers == expected_numbers, "should extract the right digits!"

    def test__elf_document_parser__get_total(self):
        parser_uut = ElfDocumentParser()

        test_doc = """1foo2h
        6ba5r
        h2\
        """
        parser_uut.parse(test_doc)

        actual_total = parser_uut.total
        expected_total = 12 + 65 + 22

        assert actual_total == expected_total, "should have right total amount"

    def test__elf_document_parser__get_total_with_str_literal(self):
        parser_uut = ElfDocumentParser()

        test_doc = """two1nine
        eightwothree
        abcone2threexyz
        xtwone3four
        4nineeightseven2
        zoneight234
        7pqrstsixteen\
        """
        parser_uut.parse(test_doc)

        actual_total = parser_uut.total
        expected_total = 29 + 83 + 13 + 24 + 42 + 14 + 76

        assert parser_uut.rows == [29, 83, 13, 24, 42, 14, 76]

        assert actual_total == expected_total, "should have right total amount"
