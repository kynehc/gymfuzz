import gymfuzz
import gymfuzz.coverage as coverage

from gymfuzz.envs.fuzz_base_env import FuzzBaseEnv


class FuzzSimpleBitsEnv(FuzzBaseEnv):
    def __init__(self):
        self._input_size = 64
        self._target_path = gymfuzz.simple_bits_target_path()
        self._args = []
        self._dict = coverage.Dictionary({
            'tokens': [],
            'bytes': True,
        })
        super(FuzzSimpleBitsEnv, self).__init__()
