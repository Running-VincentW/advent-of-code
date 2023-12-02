# ElfDocumentParser Class

The `ElfDocumentParser` class is used for parsing a document containing spelled-out digits and extracting their numeric representations.

## Constructor

### `__init__(self)`

- Initializes an instance of `ElfDocumentParser`.
- **Parameters:** None

### `parse(self, raw_doc)`

- Parses the provided raw document.
- **Parameters:**
  - `raw_doc` (str): The raw document to be parsed.
- **Returns:** None

### `rows`

- Property: Returns a list of parsed numbers from each row of the document.
- **Returns:** List[int]

### `total`

- Property: Returns the total sum of parsed numbers in the document.
- **Returns:** int

---

Usage Example:

```python
# Instantiate the ElfDocumentParser
parser = ElfDocumentParser()

# Parse a raw document
raw_document = "three seven\nfive one two\nnine eight"
parser.parse(raw_document)

# Get parsed rows and total sum
parsed_rows = parser.rows
total_sum = parser.total
