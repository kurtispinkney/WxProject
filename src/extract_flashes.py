"""
Want to identify flashes that are within 250 km of any radar within the U.S.

1. Extract variables from GLM file
2. Associate flashes with lat/lon
3. Eliminate flashes that aren't within 250 km of any radar.
4.

"""

import os
import xarray as xr

from typing import Dict


def read_glm_file(glm_file: str) -> xr.Dataset:
    if not glm_file.endswith(".nc"):
        raise ValueError
    if os.path.exists(glm_file):
        return xr.open_dataset(glm_file)
    raise FileNotFoundError


def get_flash_info(glm_data: xr.Dataset) -> Dict:
    return {glm_data["Id"][idx]:
            {"lat": glm_data["Lat"][idx], "lon": glm_data["Lon"][idx]}
            for idx
            in range(len(glm_data["Id"]))}



# x = read_glm_file("/Users/kurtispinkney/Desktop/WxProject/OR_GLM-L2-LCFA_G16_s20193002359400_e20193010000000_c20193010000028.nc")
# print(x["flash_lat"].data)