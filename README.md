# PSYC46050_Week3
This repository contains a Jupyter notebook and data to run some initial preprocessing of some EEG data collected by a Muse 2 EEG headband.


## Package: `alpha_asymmetry_calculations`

Install (from the repo root): `pip install -e .`

```python
from alpha_asymmetry_calculations import calculate_faa
mean_faa, faa_blocks = calculate_faa("Data/Participant_043_EC.edf", block_duration=4, band=(8, 13))
```

FAA = 10·log10(AF8 alpha power) − 10·log10(AF7 alpha power), computed per block after re-referencing AF7/AF8 to the mean of TP9/TP10. Lower-level functions (`load_edf`, `rereference`, `make_blocks`, `band_power`, `compute_faa`, `faa_per_block`) are also exported. See `Notebooks/` for an example.
