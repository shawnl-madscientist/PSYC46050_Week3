"""Frontal alpha asymmetry calculations from EDF EEG files."""
from .edf_io import load_edf
from .preprocessing import rereference, make_blocks
from .faa import ALPHA_BAND, band_power, compute_faa, faa_per_block
from .pipeline import calculate_faa

__all__ = ["load_edf", "rereference", "make_blocks", "ALPHA_BAND",
           "band_power", "compute_faa", "faa_per_block", "calculate_faa"]
