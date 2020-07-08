# boxcli

[![Documentation Status](https://readthedocs.org/projects/boxcli/badge/?version=latest)](https://boxcli.readthedocs.io/en/latest/?badge=latest)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d3240b45af6d44c4821aa5b73f4b478b)](https://www.codacy.com/manual/anishjewalikar/boxcli?utm_source=github.com&utm_medium=referral&utm_content=NightShade256/boxcli&utm_campaign=Badge_Grade)

Create simple and beautiful boxes in the terminal.

## Installation

The preferred method of installation is through pip.

Just execute,
`pip install -U boxcli`

That will install boxcli, or if you already have boxcli it will update it to the latest version,
pretty neat right?

## Changelog

### 1.5.2

1. Fix docs.

## Usage

You can use boxcli in your application very easily.
Here is an example:

```python
import boxcli

# Create a box factory.
factory = boxcli.BoxFactory(20, 5, boxcli.BoxStyles.ROUND)

# Create a box.
box = factory.get_box("This is the title of the box", "This is the content of the box")

# Print it! as easy as that.
print(box)
```

With the 1.4.0 update of boxcli, you can now specify the colour of the box border too.

In-depth documentation can be found [here](http://boxcli.rtfd.io/).

## Features

1. There are 8 different inbuilt box styles.

2. Custom box styles support.

3. Colour support for box border.

4. Support for non-latin alphabet characters.

5. Specify title positions and content aligment according to your need.

## Note

### Colour Support on Windows

This package cannot be directly used to colour box borders on Windows.
You have to use this code snippet to turn on that functionality:

```python
import colorama

colorama.init()
```

## Contributing

Pull requests are welcome!

## Acknowledgements

This package is a port of the package [box-cli-maker](https://github.com/Delta456/box-cli-maker) written by
[Delta456](https://github.com/Delta456) in Go.

## License

boxcli is licensed under the MIT license.

## Support

Please feel free to contact me on Discord, if you have any query regarding boxcli.
Username: `__NightShade256__#5169`
