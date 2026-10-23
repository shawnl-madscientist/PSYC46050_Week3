"""Band power and frontal alpha asymmetry (FAA) calculations."""
import numpy as np
import mne

ALPHA_BAND = (8, 13)


def band_power(data, info, band=ALPHA_BAND, picks=("AF7", "AF8"),
               fmin=1, fmax=45, n_fft=1024):
    """Mean Welch PSD within ``band`` for each channel in ``picks``.

    ``data`` is a (n_channels, n_times) array described by ``info``.
    Returns an array of shape (len(picks),).
    """
    block = mne.io.RawArray(data, info, verbose=False)
    psd = block.compute_psd(fmin=fmin, fmax=fmax, method="welch", n_fft=n_fft,
                            picks=list(picks), verbose=False)
    psds, freqs = psd.get_data(return_freqs=True)
    mask = (freqs >= band[0]) & (freqs <= band[1])
    return psds[:, mask].mean(axis=1)


def compute_faa(left_power, right_power):
    """FAA in dB: 10*log10(right power) - 10*log10(left power)."""
    return 10 * np.log10(right_power) - 10 * np.log10(left_power)


def faa_per_block(epochs, band=ALPHA_BAND, left="AF7", right="AF8"):
    """FAA (dB) for each block of ``epochs``. Returns an array of shape (n_blocks,)."""
    out = []
    for block in epochs.get_data():
        left_p, right_p = band_power(block, epochs.info, band, picks=(left, right))
        out.append(compute_faa(left_p, right_p))
    return np.array(out)
