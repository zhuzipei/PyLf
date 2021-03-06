# coding: utf-8
""" Doing the tests with your naked eyes """
import pathlib

import PIL.Image

from pylf import *
from tests.util import *

SEED = "PyLf"


def test_handwrite2():
    images = (
        PIL.Image.open(abs_path("backgrounds/even-odd-letter/村庄信笺纸.jpg")),
        PIL.Image.open(abs_path("backgrounds/even-odd-letter/树信笺纸.jpg")),
    )

    template2 = {
        "backgrounds": [
            im.resize(size=(im.size[0] * 2, im.size[1] * 2)) for im in images
        ],
        "margins": (
            {"left": 40, "top": 200, "right": 30, "bottom": 560},
            {"left": 40, "top": 200, "right": 30, "bottom": 980},
        ),
        "line_spacings": (88, 88),
        "font_sizes": (74, 74),
        "font": get_default_font(),
    }
    for file in pathlib.Path(abs_path("texts")).iterdir():
        print(file)
        with file.open(encoding="utf-8") as f:
            text = f.read()
        images = handwrite2(text, template2, seed=SEED)
        for im in images:
            im.show()
        assert input("Like it? [Y/N] ").upper() == "Y"


if __name__ == "__main__":
    print("""Test by naked eyes:""")
    print(
        """======================================
    Test: pylf.handwrite2"""
    )
    test_handwrite2()
