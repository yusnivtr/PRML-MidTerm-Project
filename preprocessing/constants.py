FS = 128
COLUMN_NAMES: list[str] = [
    "ED_COUNTER",
    "ED_INTERPOLATED",
    "ED_RAW_CQ",
    "ED_AF3",
    "ED_F7",
    "ED_F3",
    "ED_FC5",
    "ED_T7",
    "ED_P7",
    "ED_O1",
    "ED_O2",
    "ED_P8",
    "ED_T8",
    "ED_FC6",
    "ED_F4",
    "ED_F8",
    "ED_AF4",
    "ED_GYROX",
    "ED_GYROY",
    "ED_TIMESTAMP",
    "ED_ES_TIMESTAMP",
    "ED_FUNC_ID",
    "ED_FUNC_VALUE",
    "ED_MARKER",
    "ED_SYNC_SIGNAL",
]

ALL_CHANNELS: list[str] = [
    "ED_AF3",
    "ED_F7",
    "ED_F3",
    "ED_FC5",
    "ED_T7",
    "ED_P7",
    "ED_O1",
    "ED_O2",
    "ED_P8",
    "ED_T8",
    "ED_FC6",
    "ED_F4",
    "ED_F8",
    "ED_AF4",
]

USEFUL_CHANNELS: list[str] = [
    "ED_F7",
    "ED_F3",
    "ED_P7",
    "ED_O1",
    "ED_O2",
    "ED_P8",
    "ED_AF4",
]

WINDOW_LENGTH = 256
STEP_RATE = 0.25
LOWCUT = 0.5  # Low cut-off frequency for band-pass filter
HIGHCUT = 50  # High cut-off frequency for band-pass filter