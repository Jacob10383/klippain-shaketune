# Shake&Tune: 3D printer analysis tools
#
# Copyright (C) 2024 Félix Boisselier <felix@fboisselier.fr> (Frix_x on Discord)
# Licensed under the GNU General Public License v3.0 (GPL-3.0)
#
# File: stub_dependencies.py
# Description: Stub implementations for problematic dependencies to allow running
#              without numpy, matplotlib, scipy, pywavelets, and zstandard.
#              This is used when only data collection is needed, not graph generation.

import sys
from typing import Any, List, Tuple

# Stub for numpy
class np:
    # Add ndarray class
    class ndarray:
        def __init__(self, data=None):
            self.data = data or []
        
        def __getitem__(self, key):
            return self.data[key]
        
        def __setitem__(self, key, value):
            self.data[key] = value
    
    @staticmethod
    def array(data, dtype=None):
        return data
    
    @staticmethod
    def zeros(shape, dtype=None):
        if isinstance(shape, int):
            return [0.0] * shape
        elif len(shape) == 2:
            return [[0.0] * shape[1] for _ in range(shape[0])]
        return [0.0] * shape[0]
    
    @staticmethod
    def ones(shape, dtype=None):
        if isinstance(shape, int):
            return [1.0] * shape
        elif len(shape) == 2:
            return [[1.0] * shape[1] for _ in range(shape[0])]
        return [1.0] * shape[0]
    
    @staticmethod
    def linspace(start, stop, num):
        step = (stop - start) / (num - 1) if num > 1 else 0
        return [start + i * step for i in range(num)]
    
    @staticmethod
    def arange(start, stop=None, step=1):
        if stop is None:
            start, stop = 0, start
        return [start + i * step for i in range(int((stop - start) / step))]
    
    @staticmethod
    def searchsorted(arr, value, side='left'):
        for i, v in enumerate(arr):
            if side == 'left' and v >= value:
                return i
            elif side == 'right' and v > value:
                return i
        return len(arr)
    
    @staticmethod
    def argmax(arr):
        if not arr:
            return 0
        return max(range(len(arr)), key=lambda i: arr[i])
    
    @staticmethod
    def max(arr):
        return max(arr) if arr else 0
    
    @staticmethod
    def min(arr):
        return min(arr) if arr else 0
    
    @staticmethod
    def mean(arr):
        return sum(arr) / len(arr) if arr else 0
    
    @staticmethod
    def std(arr):
        if not arr:
            return 0
        mean_val = sum(arr) / len(arr)
        variance = sum((x - mean_val) ** 2 for x in arr) / len(arr)
        return variance ** 0.5
    
    @staticmethod
    def sum(arr):
        return sum(arr)
    
    @staticmethod
    def sqrt(arr):
        if isinstance(arr, (list, tuple)):
            return [x ** 0.5 for x in arr]
        return arr ** 0.5
    
    @staticmethod
    def exp(arr):
        if isinstance(arr, (list, tuple)):
            return [2.718281828459045 ** x for x in arr]
        return 2.718281828459045 ** arr
    
    @staticmethod
    def log(arr):
        if isinstance(arr, (list, tuple)):
            return [__import__('math').log(x) for x in arr]
        return __import__('math').log(arr)
    
    @staticmethod
    def sin(arr):
        if isinstance(arr, (list, tuple)):
            return [__import__('math').sin(x) for x in arr]
        return __import__('math').sin(arr)
    
    @staticmethod
    def cos(arr):
        if isinstance(arr, (list, tuple)):
            return [__import__('math').cos(x) for x in arr]
        return __import__('math').cos(arr)
    
    @staticmethod
    def pi():
        return 3.141592653589793
    
    @staticmethod
    def kaiser(M, beta):
        # Simplified Kaiser window
        return [1.0] * M
    
    @staticmethod
    def concatenate(arrays, axis=0):
        if axis == 0:
            result = []
            for arr in arrays:
                result.extend(arr)
            return result
        else:
            # For 2D arrays, this is simplified
            return arrays[0] if arrays else []

# Stub for matplotlib
class matplotlib:
    @staticmethod
    def use(backend):
        pass
    
    class font_manager:
        class FontProperties:
            def set_size(self, size):
                pass
    
    class ticker:
        class AutoMinorLocator:
            pass
    
    class figure:
        class Figure:
            def savefig(self, path, dpi=None, bbox_inches=None):
                pass

class plt:
    @staticmethod
    def imread(path):
        return None
    
    @staticmethod
    def figure(figsize=None):
        return None
    
    @staticmethod
    def subplots(nrows=1, ncols=1, figsize=None):
        return None, None
    
    @staticmethod
    def savefig(path, dpi=None, bbox_inches=None):
        pass
    
    @staticmethod
    def close(fig=None):
        pass

# Stub for scipy.signal
class scipy:
    class signal:
        @staticmethod
        def spectrogram(x, fs=None, window=None, nperseg=None, noverlap=None, detrend=None, scaling=None, mode=None):
            # Return dummy spectrogram data
            f = [0.0, 1.0, 2.0]
            t = [0.0, 0.1, 0.2]
            Sxx = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
            return f, t, Sxx

# Stub for zstandard
class zstandard:
    class ZstdCompressor:
        def __init__(self, level=None):
            pass
        
        def stream_writer(self, file):
            return self
        
        def write(self, data):
            pass
        
        def flush(self, flag=None):
            pass
    
    class ZstdDecompressor:
        def __init__(self):
            pass
        
        def stream_reader(self, file):
            return self
        
        def read(self, size=None):
            return b''
    
    FLUSH_FRAME = 'FLUSH_FRAME'

# Stub for pywavelets (if used)
class pywt:
    @staticmethod
    def wavedec(data, wavelet, level=None):
        return [data, [None] * level] if level else [data, []]
    
    @staticmethod
    def waverec(coeffs, wavelet):
        return coeffs[0] if coeffs else []

# Function to replace problematic imports
def replace_imports():
    """Replace problematic imports with stub implementations"""
    # Create a numpy module with __version__ attribute and ndarray
    numpy_module = type('numpy', (), {
        'np': np,
        'ndarray': np.ndarray,
        '__version__': '1.21.0'  # Add a version string
    })()
    sys.modules['numpy'] = numpy_module
    
    # Create scipy module with stats
    scipy_module = type('scipy', (), {
        'signal': scipy.signal,
        'stats': type('stats', (), {
            'pearsonr': lambda x, y: (0.0, 1.0)  # Dummy correlation function
        })()
    })()
    sys.modules['scipy'] = scipy_module
    sys.modules['scipy.signal'] = scipy.signal
    sys.modules['scipy.stats'] = scipy_module.stats
    
    sys.modules['matplotlib'] = matplotlib
    sys.modules['matplotlib.pyplot'] = plt
    sys.modules['matplotlib.figure'] = matplotlib.figure
    sys.modules['matplotlib.font_manager'] = matplotlib.font_manager
    sys.modules['matplotlib.ticker'] = matplotlib.ticker
    sys.modules['zstandard'] = zstandard
    sys.modules['pywt'] = pywt 