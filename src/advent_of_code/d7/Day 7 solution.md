### CamelCardParser Class32T3K 765

The `CamelCardParser` class allows parsing camel cards and determining their ranks based on given rules.

#### Methods

##### `parse(self, raw_input: str) -> None`
- **Description:** Parses the raw input containing cards and their bets.
- **Parameters:**
  - `raw_input` (str): A string containing card details and bets.
- **Usage:**
  ```python
  parser = CamelCardParser()
  raw_input = "32T3K 765\nT55J5 684\n..."
  parser.parse(raw_input)
  ```
- **Example:**
  ```python
  parser = CamelCardParser()
  raw_input = "32T3K 765\nT55J5 684\n..."
  parser.parse(raw_input)
  ```

##### `total_bets(self) -> int`
- **Description:** Calculates the total bets based on the sorted cards.
- **Returns:** Total sum of bets.
- **Usage:**
  ```python
  parser = CamelCardParser()
  parser.parse(raw_input)
  total = parser.total_bets()
  ```
- **Example:**
  ```python
  parser = CamelCardParser()
  parser.parse(raw_input)
  total = parser.total_bets()
  ```

##### `get_hand(cards: str) -> CamelCardsHand`
- **Description:** Determines the rank of a given set of cards.
- **Parameters:**
  - `cards` (str): A string containing card details.
- **Returns:** Enum representing the hand rank.
- **Usage:**
  ```python
  hand_rank = CamelCardParser.get_hand("32T3K")
  ```
- **Example:**
  ```python
  hand_rank = CamelCardParser.get_hand("T55J5")
  ```

#### Purpose
The `CamelCardParser` class is designed to interpret camel card combinations and calculate their ranks based on specific rules. It provides methods to parse input, determine hand ranks, and compute total bets based on the parsed cards.

#### Notes
- Ensure the input follows the specified format for card representation.
- The `CamelCardParser` aims to accurately rank and sort camel cards according to predefined criteria.
- Usage of the class involves parsing the input, analyzing hand ranks, and calculating total bets.
