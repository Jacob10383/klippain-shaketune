# Shake&Tune: 3D printer analysis tools
#
# Copyright (C) 2024 Félix Boisselier
# Licensed under the GNU General Public License v3.0 (GPL-3.0)
#
# File: constants.py
# Description: Lightweight constants shared across commands without importing heavy libs.


# Constant used to define the standard axis direction and names
AXIS_CONFIG = [
    {"axis": "x", "direction": (1, 0, 0), "label": "axis_X"},
    {"axis": "y", "direction": (0, 1, 0), "label": "axis_Y"},
    {"axis": "a", "direction": (1, -1, 0), "label": "belt_A"},
    {"axis": "b", "direction": (1, 1, 0), "label": "belt_B"},
    {"axis": "corexz_x", "direction": (1, 0, 1), "label": "belt_X"},
    {"axis": "corexz_z", "direction": (-1, 0, 1), "label": "belt_Z"},
]


