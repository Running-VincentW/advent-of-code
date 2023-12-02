## CubeGame Class Documentation

### Overview:
The `CubeGame` class manages and analyzes games involving cubes of different colors and quantities.

### Public Methods:

#### `parse`
- **Signature:** `def parse(self, doc: str) -> list[Game]`
- **Description:** Parses a document containing multiple lines of game data.
- **Parameters:** `doc` (`str`): A document containing multiple lines of game information.
- **Returns:** `list[Game]`: A list of `Game` objects parsed from the document.

#### `get_games_power`
- **Signature:** `def get_games_power(self, games: list[Game]) -> int`
- **Description:** Calculates the combined power of multiple games.
- **Parameters:** `games` (`list[Game]`): A list of Game objects.
- **Returns:** `int`: The total power of all provided games.

#### `get_valid_games_index`
- **Signature:** `def get_valid_games_index(self, bag: dict[str, int], games: list[Game]) -> list[int]`
- **Description:** Retrieves the indices of valid games based on a provided bag of cube quantities.
- **Parameters:**
  - `bag` (`dict[str, int]`): A dictionary containing available cube quantities.
  - `games` (`list[Game]`): A list of Game objects.
- **Returns:** `list[int]`: A list of indices corresponding to valid games.

### Usage Example:

```python
# Create an instance of CubeGame
cube_game = CubeGame()

# Example document containing game information
document = "GameID: 1; 2 Red, 3 Blue; 4 Green, 1 Yellow\nGameID: 2; 1 Red, 2 Blue; 3 Green, 2 Yellow\n"

# Parse the document to obtain a list of Game objects
parsed_games = cube_game.parse(document)

# Perform operations on the parsed games
total_power = cube_game.get_games_power(parsed_games)

# Check the validity of games with a given bag of cube quantities
cube_bag = {'Red': 5, 'Blue': 6, 'Green': 5, 'Yellow': 3}
validity_list = cube_game.check_games_validity(cube_bag, parsed_games)

# Retrieve indices of valid games based on the cube bag
valid_game_indices = cube_game.get_valid_games_index(cube_bag, parsed_games)
