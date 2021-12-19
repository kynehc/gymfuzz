import gymfuzz
import gymfuzz.coverage as coverage

from gymfuzz.envs.fuzz_base_env import FuzzBaseEnv


class FuzzLibPNGEnv(FuzzBaseEnv):
    def __init__(self):
        self._input_size = 1024
        self._args = []
        self._dict = coverage.Dictionary({
            'tokens': [
                b"\x89PNG\x0d\x0a\x1a\x0a",
                b"IDAT",
                b"IEND",
                b"IHDR",
                b"PLTE",
                b"bKGD",
                b"cHRM",
                b"fRAc",
                b"gAMA",
                b"gIFg",
                b"gIFt",
                b"gIFx",
                b"hIST",
                b"iCCP",
                b"iTXt",
                b"oFFs",
                b"pCAL",
                b"pHYs",
                b"sBIT",
                b"sCAL",
                b"sPLT",
                b"sRGB",
                b"sTER",
                b"tEXt",
                b"tIME",
                b"tRNS",
                b"zTXt"
            ],
            'bytes': True,
        })
        super(FuzzLibPNGEnv, self).__init__()


class FuzzLibPNG12Env(FuzzLibPNGEnv):
    def __init__(self):
        self._target_path = gymfuzz.libpng12_target_path()
        super(FuzzLibPNG12Env, self).__init__()

class FuzzLibPNG16Env(FuzzLibPNGEnv):
    def __init__(self):
        self._target_path = gymfuzz.libpng16_target_path()
        super(FuzzLibPNG16Env, self).__init__()