# Super Bowl Squares
Did you run out of time to pick names out of hats this year to fill our your Super Bowl squares?  Worry not, this light python package has the solution!

# Examples
```python
from super_bowl_squares import generate_squares

players = {
    'TB12': 50,
    'Trubisky': 10,
    'Jay': 35
}

blank_squares = 'Charity'
export_path = '/path/to/export.csv'

df_squares = generate_squares(
    players=players,
    export_path=export_path)
df_squares
```

# Installation
```bash
pip install .
```
