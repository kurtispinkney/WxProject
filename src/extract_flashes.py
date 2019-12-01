"""
Want to identify flashes that are within 250 km of any radar within the U.S.

1. Extract variables from GLM file
2. Associate flashes with lat/lon
3. Eliminate flashes that aren't within 250 km of any radar.
4.

"""

import os
import xarray as xr


def read_glm_file(glm_file: str):
    if not glm_file.endswith(".nc"):
        raise ValueError
    if os.path.exists(glm_file):
        return xr.open_dataset(glm_file)
    raise FileNotFoundError


def test():
    pass
