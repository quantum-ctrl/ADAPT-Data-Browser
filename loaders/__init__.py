"""
ADAPT Data Browser - Loaders Package

Provides data loaders for various ARPES file formats:
- ADRESS beamline (SLS) HDF5 files
- SIS beamline HDF5 files
- Igor Binary Wave (.ibw) files
- SES analyzer ZIP archives
"""

from .load_adress_data import load as load_adress
from .load_sis_data import load_sis_data as load_sis
from .load_ibw_data import load as load_ibw
from .load_ses_zip import load as load_ses

__all__ = [
    'load_adress',
    'load_sis',
    'load_ibw',
    'load_ses',
]
