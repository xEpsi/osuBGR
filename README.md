# osuBGR

This program replaces all osu! backgrounds with a custom image.
It can also restore the backgrounds to their original state.


## Table of Contents

- [Installation](#installation)
- [Contributing](#contributing)


## Installation

First install the required modules:

```bash
pip install -r requirements.txt
```

Then set up your settings in osuBGR.py:

```python
mode = "replace" / "restore"
custom_image = r"image path" / None
```

Then run the script:

```bash
python osuBGR.py
```


## Contributing

Contributions are welcome! Please create an issue or pull request.
