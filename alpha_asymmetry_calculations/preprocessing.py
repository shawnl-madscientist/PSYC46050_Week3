"""Re-referencing and epoching."""
import mne


def rereference(raw, targets=("AF7", "AF8"), reference=("TP9", "TP10")):
    """Subtract the mean of the ``reference`` channels from each ``targets`` channel.

    Returns a re-referenced copy; the input is not modified.
    """
    raw = raw.copy()
    ref_data = raw.get_data(picks=list(reference)).mean(axis=0)
    for ch in targets:
        raw._data[raw.ch_names.index(ch), :] -= ref_data
    return raw


def make_blocks(raw, block_duration=4.0):
    """Split ``raw`` into consecutive fixed-length blocks, returned as :class:`mne.Epochs`."""
    events = mne.make_fixed_length_events(raw, duration=block_duration)
    return mne.Epochs(raw, events, tmin=0,
                      tmax=block_duration - 1 / raw.info["sfreq"],
                      baseline=None, preload=True, verbose=False)
