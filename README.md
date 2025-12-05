# ADAPT Data Browser

**ARPES Data Analysis & Processing Tool - Data Browser**

A desktop application for browsing and visualizing scientific ARPES (Angle-Resolved Photoemission Spectroscopy) data files.

## Features

- 📂 **Multi-format support**: HDF5, IBW (Igor Binary Wave), and ZIP archives
- 🔬 **Beamline loaders**: ADRESS, SIS, Bloch and more

## Supported File Formats

| Format | Extensions | Description |
|--------|------------|-------------|
| HDF5 | `.h5`, `.hdf5` | ADRESS and SIS beamline data |
| IBW | `.ibw` | Igor Binary Wave files |
| ZIP | `.zip` | SES analyzer archives |

## Requirements

- Python ≥ 3.9
- PySide6
- NumPy
- xarray
- h5py
- pyqtgraph
- matplotlib
- igor2

## Installation

```bash
cd ADAPT-Data-Browser-main
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 -m data_browser.app
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgements

Special thanks to:
- **Procopios Constantinou** for the [ARPEScape](https://github.com/c0deta1ker/ARPEScape) project.
- **Craig Polley** for the [pesto](https://gitlab.com/flashingLEDs/pesto) project.
