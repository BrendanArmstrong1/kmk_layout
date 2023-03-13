import board
from kb import KMKKeyboard
from storage import getmount

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.rapidfire import RapidFire
from kmk.modules.modtap import ModTap
from kmk.modules.oneshot import OneShot
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.split import Split

keyboard = KMKKeyboard()


split = Split(
    data_pin=board.GP1,
    split_side=None,
    use_pio=True,
    uart_flip=True,
)

rapid_fire = RapidFire()
layers_ext = Layers()
mod_tap = ModTap()
one_shot = OneShot()
mouse_key = MouseKeys()

mod_tap.tap_time = 150
one_shot.tap_time = 1500

keyboard.modules = [
    layers_ext,
    split,
    mod_tap,
    mouse_key,
    rapid_fire,
    one_shot,
]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

# OneShot
ONSHT1 = KC.OS(KC.MO(1))
LAYER_4 = KC.MO(3)

# Mod-taps
COMM_L2 = KC.MT(KC.COMM, KC.MO(2))
SCLN_GUI = KC.MT(KC.SCLN, KC.LGUI)
A_QUO = KC.MT(KC.QUOT, KC.LALT)

# MouseKeys
MSEWHU = KC.MW_UP
MSEWHD = KC.MW_DN
MSEBUL = KC.MB_LMB
MSEBUR = KC.MB_RMB
MSEBUM = KC.MB_MMB
MSELFT = KC.MS_LT
MSEDWN = KC.MS_DN
MSE_UP = KC.MS_UP
MSERHT = KC.MS_RT

# Rapid Fire
PRNSPM = KC.RF(
    KC.PSCR,
    timeout=0,
    interval=10000,
    enable_interval_randomization=True,
    randomization_magnitude=3000,
    toggle=True,
)

# fmt: off
# flake8: noqa
keyboard.keymap = [
    [  # DVORAK
   SCLN_GUI,   A_QUO,  KC.DOT,    KC.P,    KC.Y,    KC.F,    KC.G,    KC.C,    KC.R,    KC.L,
       KC.A,    KC.O,    KC.E,    KC.U,    KC.I,    KC.D,    KC.H,    KC.T,    KC.N,    KC.S,
    COMM_L2,    KC.Q,    KC.J,    KC.K,    KC.X,    KC.B,    KC.M,    KC.W,    KC.V,    KC.Z,
                               KC.LSFT,  ONSHT1,  KC.SPC, KC.LCTL,
    ],
    [  # SYMBOLS
     KC.GRV, KC.CIRC, KC.BSLS, KC.PERC, KC.PLUS, KC.MINS, KC.LBRC, KC.RBRC,  KC.DLR, KC.BSPC,
     KC.ESC, KC.UNDS, KC.TILD, KC.ASTR,  KC.TAB,  KC.ENT, KC.LCBR, KC.RCBR, KC.QUES, KC.PSLS,
    KC.PIPE, KC.HASH, KC.LABK, KC.RABK, KC.AMPR,  KC.EQL, KC.LPRN, KC.RPRN,   KC.AT, KC.EXLM,
                               KC.LSFT,KC.TO(0),  KC.SPC, KC.LCTL,
    ],
    [  # NUMBERS
    LAYER_4, KC.COMM,  KC.DOT,  KC.INS, KC.PLUS, KC.MINS,   KC.N1,   KC.N2,   KC.N3, KC.BSPC,
     KC.ESC, KC.HOME,  KC.END,  KC.DEL,  KC.TAB,  KC.ENT,   KC.N4,   KC.N5,   KC.N6,   KC.N0,
    COMM_L2, KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT,  KC.EQL,   KC.N7,   KC.N8,   KC.N9, KC.LGUI,
                               KC.LSFT, KC.LALT,  KC.SPC, KC.LCTL,
    ],
    [  # MOUSE
    _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  MSEWHU,  MSEBUL,  MSEBUM,  MSEBUR, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  MSELFT,  MSEDWN,  MSE_UP,  MSERHT, XXXXXXX,
    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  MSEWHD, XXXXXXX, XXXXXXX, XXXXXXX,  PRNSPM,
                               KC.LSFT, KC.LALT,  KC.SPC, KC.LCTL,
    ],
]

if __name__ == "__main__":
    keyboard.go()
