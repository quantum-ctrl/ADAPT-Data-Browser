"""
ADAPT loaders package.
Provides functions to load ARPES data from various file formats.

All loaders return xarray.DataArray with standardized dimension names:
- energy: Binding/Kinetic energy axis
- angle: Detector angle
- scan: Third dimension (tilt, photon energy, etc.) for 3D data
"""

from loaders.load_adress_data import load as load_adress
from loaders.load_ibw_data import load as load_ibw
from loaders.load_ses_zip import load as load_ses
from loaders.load_sis_data import load_sis_data as load_sis

__all__ = [
    'load_adress',
    'load_ibw',
    'load_ses',
    'load_sis',
]
