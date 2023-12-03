# EngineParser

## Properties
- `map_width` (int): Width of the map.
- `map_height` (int): Height of the map.
- `point_dict` (dict[Point, PointData]): Dictionary mapping `Point` objects to `PointData`.
- `char_pts` (dict[Point, str]): Dictionary mapping `Point` objects to strings.

## Methods

### `parse_map(self, input_str: str) -> None`
Parses the input string to initialize the `char_pts` and `point_dict` properties.

- **Parameters:**
  - `input_str` (str): Input string containing map information.
- **Returns:** None
- **Usage Example:**
  ```python
  parser = EngineParser()
  parser.parse_map("...12\n.34.*\n567..")
  ```

###  `_get_surround_points(self, point: Point) -> list[Point]`
Returns a list of surrounding points for a given `Point`.

- **Parameters:**
  - `point` (Point): Point object for which surrounding points are retrieved.
- **Returns:** List of surrounding Point objects.
- **Usage Example:**
  ```python
  parser = EngineParser()
  points = parser._get_surround_points(Point(2, 2))
  ```

### `get_engine_schematics(self) -> Tuple[list[int], list[int]]`
Computes engine schematics from char_pts and point_dict.

- **Returns:** Tuple containing two lists: schematic numbers and gear values.
- **Usage Example:**

  ```python
  parser = EngineParser()
  schematics, gears = parser.get_engine_schematics()
  ```

### `get_engine_schematics_sum(self) -> int`
Computes the sum of all schematic numbers.

- **Returns:** Total sum of schematic numbers.
- **Usage Example:**
  ```python
  parser = EngineParser()
  total_sum = parser.get_engine_schematics_sum()
  ```

### `get_gear_sum(self) -> int`
Computes the sum of gear values.

- **Returns:** Total sum of gear values.
- **Usage Example:**
  ```python
  parser = EngineParser()
  gear_sum = parser.get_gear_sum()
  ```


## Notes for Users

The EngineParser class is designed to parse map data, identify engine schematics, and calculate their sums and gear values from the provided input string.

Ensure to call parse_map method before using methods relying on map data.
Utilize get_engine_schematics, get_engine_schematics_sum, and get_gear_sum for retrieving engine information after parsing the map.