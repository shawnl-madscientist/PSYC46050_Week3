"""Loading EEG data from EDF files."""
import mne


def load_edf(path, preload=True):
    """Load an EDF file as an :class:`mne.io.Raw` object."""
    return mne.io.read_raw_edf(path, preload=preload, verbose=False)
