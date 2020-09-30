# boxcli

[![Documentation Status](https://readthedocs.org/projects/boxcli/badge/?version=latest)](https://boxcli.readthedocs.io/en/latest/?badge=latest)

Create simple and beautiful boxes in the terminal.

## Installation

The preferred method of installation is through pip.

Just execute,
`pip install -U boxcli`

That will install boxcli, or if you already have boxcli it will update it to the latest version,
pretty neat right?

## Changelog

### 2.0.0

1. Remove redudant exception from codebase, `DifferentLengthError`.

2. Use `rich` for cross-platform colour support.

3. Allow custom border colours with the `RGB` class.

## Usage

You can use boxcli in your application very easily.
Here is an example:

```python
import boxcli

# Create a box factory.
factory = boxcli.BoxFactory(
    20,
    5,
    boxcli.BoxStyles.ROUND,
    colour=boxcli.RGB((255, 255, 0)),
)

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

3. Colour (with option for custom RGB colours) support for box border.

4. Support for non-latin alphabet characters.

5. Specify title positions and content aligment according to your need.

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
