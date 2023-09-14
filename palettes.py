from typing import Literal, Optional

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

NatParksPalettes = {
    "Acadia": {
        "colors": [
            "#212E52",
            "#444E7E",
            "#8087AA",
            "#B7ABBC",
            "#F9ECE8",
            "#FCC893",
            "#FEB424",
            "#FD8700",
            "#D8511D",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "colorblind": True,
    },
    "Arches": {
        "colors": [
            "#1A3D82",
            "#0C62AF",
            "#4499F5",
            "#8FCAFD",
            "#F2F2F2",
            "#F0AC7D",
            "#CD622E",
            "#B14311",
            "#832B0F",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "colorblind": True,
    },
    "Arches2": {
        "colors": ["#3A1F46", "#7F4B89", "#B46DB3", "#E3A5D6", "#F3DAE4"],
        "indices": [0, 1, 2, 3, 4],
        "colorblind": True,
    },
    "Banff": {
        "colors": [
            "#006475",
            "#00A1B7",
            "#55CFD8",
            "#586028",
            "#898928",
            "#616571",
            "#9DA7BF",
        ],
        "indices": [1, 4, 0, 5, 2, 6, 3],
        "colorblind": False,
    },
    "BryceCanyon": {
        "colors": [
            "#882314",
            "#C0532B",
            "#CF932C",
            "#674D53",
            "#8C86A0",
            "#724438",
            "#D5AB85",
        ],
        "indices": [0, 4, 1, 6, 3, 2, 5],
        "colorblind": False,
    },
    "CapitolReef": {
        "colors": ["#291919", "#532A34", "#7C5467", "#878195", "#AEB2B7", "#D4D9DD"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": True,
    },
    "Charmonix": {
        "colors": ["#008FF8", "#B6AA0D", "#E2C2A2", "#E23B0E", "#F2C621", "#196689"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "CraterLake": {
        "colors": [
            "#1D4A79",
            "#794C23",
            "#6B7444",
            "#6089B5",
            "#BF9785",
            "#275E4D",
            "#807B7F",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6],
        "colorblind": False,
    },
    "Cuyahoga": {
        "colors": ["#E07529", "#FAAE32", "#7F7991", "#A84A00", "#5D4F36", "#B39085"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": True,
    },
    "DeathValley": {
        "colors": [
            "#8C2B0E",
            "#C5692D",
            "#FEB359",
            "#132F5B",
            "#435F90",
            "#68434E",
            "#B47E83",
        ],
        "indices": [0, 4, 6, 1, 5, 2, 3],
        "colorblind": True,
    },
    "Denali": {
        "colors": ["#20223E", "#3F3F7B", "#278192", "#00B089", "#2EEA8C", "#8FF7BD"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "Everglades": {
        "colors": ["#345023", "#596C0B", "#83A102", "#003B68", "#426F86", "#7A712F"],
        "indices": [2, 3, 0, 5, 4, 1],
        "colorblind": False,
    },
    "Glacier": {
        "colors": ["#01353D", "#088096", "#58B3C7", "#7AD4E4", "#B8FCFC"],
        "indices": [0, 1, 2, 3, 4],
        "colorblind": True,
    },
    "GrandCanyon": {
        "colors": [
            "#521E0F",
            "#9C593E",
            "#DDA569",
            "#3F4330",
            "#8E7E3C",
            "#2A4866",
            "#6592B0",
        ],
        "indices": [1, 5, 2, 3, 6, 0, 4],
        "colorblind": False,
    },
    "Halekala": {
        "colors": ["#722710", "#A3844D", "#675243", "#A85017", "#838BAA"],
        "indices": [0, 1, 2, 3, 4],
        "colorblind": True,
    },
    "IguazuFalls": {
        "colors": ["#415521", "#97AD3D", "#4C3425", "#7F6552", "#5A8093", "#9FBAD3"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "KingsCanyon": {
        "colors": ["#613921", "#A77652", "#F2C27B", "#AAC9ED", "#44637D", "#8E949F"],
        "indices": [0, 4, 5, 2, 1, 3],
        "colorblind": True,
    },
    "LakeNakuru": {
        "colors": ["#D76E9A", "#A1ACC8", "#AD3C36", "#332627", "#EACACF", "#AA6B77"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "Olympic": {
        "colors": [
            "#3A4330",
            "#426737",
            "#75871B",
            "#BAB97D",
            "#FAF3CE",
            "#FDE16A",
            "#F9B40E",
            "#E88C23",
            "#A25933",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "colorblind": False,
    },
    "Redwood": {
        "colors": ["#5E3B49", "#9B5F6B", "#BA817D", "#325731", "#6A9741", "#5F4E2F"],
        "indices": [1, 4, 5, 2, 3, 0],
        "colorblind": False,
    },
    "RockyMountain": {
        "colors": [
            "#274C31",
            "#A3AEB5",
            "#2F4B6A",
            "#8F8081",
            "#3F7156",
            "#6F89A7",
            "#5B5443",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6],
        "colorblind": False,
    },
    "Saguaro": {
        "colors": ["#127088", "#C85729", "#92874B", "#CD8A39", "#AC3414", "#57643C"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "SmokyMountains": {
        "colors": [
            "#42511A",
            "#889D35",
            "#D3D175",
            "#B50200",
            "#DA6C41",
            "#7C6E66",
            "#BCAFA6",
        ],
        "indices": [0, 3, 1, 5, 2, 4, 6],
        "colorblind": False,
    },
    "SouthDowns": {
        "colors": ["#948D2A", "#D5B44D", "#89A4BF", "#F1D6B6", "#9B8358", "#577291"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "Torres": {
        "colors": [
            "#2F397A",
            "#7391BD",
            "#894846",
            "#E9988C",
            "#535260",
            "#B7A7A6",
            "#785838",
            "#C68D61",
            "#4F6008",
            "#93995C",
        ],
        "indices": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "colorblind": False,
    },
    "Triglav": {
        "colors": ["#386EC2", "#B5B5B2", "#990006", "#625D0A", "#B9741F", "#213958"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": True,
    },
    "WindCave": {
        "colors": ["#2F100E", "#6C3322", "#B07159", "#C9A197", "#E0CDCD"],
        "indices": [0, 1, 2, 3, 4],
        "colorblind": True,
    },
    "Volcanoes": {
        "colors": ["#082544", "#1E547D", "#79668C", "#DE3C37", "#F2DC7E"],
        "indices": [0, 1, 2, 3, 4],
        "colorblind": True,
    },
    "Yellowstone": {
        "colors": ["#0067A2", "#DFCB91", "#CB7223", "#289A84", "#7FA4C2", "#AF7E56"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
    "Yosemite": {
        "colors": ["#293633", "#3D5051", "#6B7F7F", "#87A1C7", "#516B95", "#304F7D"],
        "indices": [0, 1, 2, 3, 4, 5],
        "colorblind": False,
    },
}

# Colorblind-friendly palettes:
colorblind_palettes = [
    "Acadia",
    "Arches",
    "Arches2",
    "CapitolReef",
    "Cuyahoga",
    "DeathValley",
    "Glacier",
    "Halekala",
    "KingsCanyon",
    "Triglav",
    "WindCave",
    "Volcanoes",
]


# ---------------------------------------------------------------------------------------------------
# Palette selection
# ---------------------------------------------------------------------------------------------------
def national_park_palettes(
    name: str,
    n: Optional[int] = None,
    type: Optional[Literal["continuous", "discrete"]] = None,
    direction: int = 1,
    override_order: bool = False,
):
    """
    National Parks Palette Generator

    Generates color palettes inspired by National Parks.

    Args:
        name: Name of chosen palette
        n: Optional, number of colors of the selected palette to use. If None, will use all colors.
        type: Either "continuous" or "discrete"
        direction: Sets order of colors. Default is 1. If -1, palette color order is reversed.
        override_order: If True, colors are selected in sequential order. If False, colors are selected by listed
            palette order.

    Returns:
        List of colors in hex format.
    """
    palette = NatParksPalettes.get(name)

    if not palette:
        raise ValueError("Palette does not exist.")

    if not n:
        n = len(palette["colors"])

    if direction not in [1, -1]:
        raise ValueError(
            "Direction not valid. Please use 1 for standard palette or -1 for reversed palette."
        )

    if not type:
        type = "continuous" if n > len(palette["colors"]) else "discrete"

    if type == "discrete" and n > len(palette["colors"]):
        raise ValueError(
            "Number of requested colors greater than what discrete palette can offer. Use continuous instead."
        )

    if type == "continuous":
        colors = plt.cm.colors.makeMappingArray(
            n, plt.cm.colors.ListedColormap(palette["colors"]), N=n
        ).tolist()
        if direction == -1:
            colors = colors[::-1]
        return [plt.colors.to_hex(color) for color in colors]
    else:
        indices = (
            palette["indices"]
            if not override_order
            else list(range(len(palette["colors"])))
        )
        selected_colors = [palette["colors"][i] for i in indices[:n]]
        if direction == -1:
            selected_colors = selected_colors[::-1]
        return selected_colors


def colorblind_friendly_check(palette_name: str):
    """Checks whether a palette is colorblind-friendly.

    Args:
        palette_name: Name of Palette. Valid choices are based on the keys of the NatParksPalettes dictionary.

    Returns:
        is_colorblind_friendly: True if the palette is colorblind-friendly, otherwise False.
    """
    if palette_name not in NatParksPalettes:
        raise ValueError("Palette does not exist.")

    is_colorblind_friendly = NatParksPalettes[palette_name]["colorblind"]
    return is_colorblind_friendly


def display_all():
    fig, axes = plt.subplots(6, 5, figsize=(15, 12))

    for ax, (name, palette) in zip(axes.ravel(), NatParksPalettes.items()):
        colors = palette["colors"]
        for i, color in enumerate(colors):
            ax.fill_between([i, i + 1], 0, 1, color=color)
        ax.set_xlim(0, len(colors))
        ax.set_ylim(0, 1)
        ax.set_title(name, fontsize=10)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------------------------------------------------
# Colormap scaling
# ---------------------------------------------------------------------------------------------------
def scale_color_natparks_d(
    name: str,
    direction: int = 1,
    override_order: bool = False,
):
    """Returns a colormap for the given palette name for discrete scales.

    Args:
        name: Name of the palette.
        direction: 1 for standard palette order, -1 for reversed order.
        override_order: If True, colors are selected in sequential order from the full palette.

    Returns:
        cmap: A matplotlib colormap object.
    """
    palette = NatParksPalettes.get(name, None)

    if not palette:
        raise ValueError("Palette does not exist.")

    if direction not in [1, -1]:
        raise ValueError(
            "Direction not valid. Please use 1 for standard palette or -1 for reversed palette."
        )

    if override_order:
        colors = palette["colors"][: len(palette["indices"])]
    else:
        colors = [palette["colors"][idx] for idx in palette["indices"]]

    if direction == -1:
        colors = list(reversed(colors))

    cmap = mcolors.LinearSegmentedColormap.from_list(name, colors)
    return cmap


def scale_color_natparks_c(name: str, direction: int = 1):
    """Returns a colormap for the given palette name for continuous scales.

    Args:
        name: Name of the palette
        direction: 1 for standard palette order, -1 for reversed order.

    Returns:
        cmap: A matplotlib colormap object.
    """
    palette = NatParksPalettes.get(name, None)

    if not palette:
        raise ValueError("Palette does not exist.")

    if direction not in [1, -1]:
        raise ValueError(
            "Direction not valid. Please use 1 for standard palette or -1 for reversed palette."
        )

    colors = palette["colors"]

    if direction == -1:
        colors = list(reversed(colors))

    cmap = mcolors.LinearSegmentedColormap.from_list(name, colors)
    return cmap
