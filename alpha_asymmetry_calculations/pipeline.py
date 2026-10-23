"""End-to-end FAA calculation from an EDF file."""
import numpy as np

from .edf_io import load_edf
from .preprocessing import rereference, make_blocks
from .faa import faa_per_block, ALPHA_BAND


def calculate_faa(edf_path, block_duration=4.0, band=ALPHA_BAND,
                  left="AF7", right="AF8", reference=("TP9", "TP10")):
    """Compute FAA (dB) from an EDF file.

    Loads the file, re-references ``left``/``right`` to the mean of ``reference``,
    splits into ``block_duration``-second blocks and computes FAA per block.

    Returns ``(mean_faa, faa_blocks)``.
    """
    raw = rereference(load_edf(edf_path), (left, right), reference)
    epochs = make_blocks(raw, block_duration)
    blocks = faa_per_block(epochs, band, left, right)
    return float(np.mean(blocks)), blocks
