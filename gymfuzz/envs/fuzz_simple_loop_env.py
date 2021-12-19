import gymfuzz
import gymfuzz.coverage as coverage

from gymfuzz.envs.fuzz_base_env import FuzzBaseEnv


class FuzzSimpleLoopEnv(FuzzBaseEnv):
    def __init__(self):
        self._input_size = 8
        self._target_path = gymfuzz.simple_loop_target_path()
        self._args = []
        self._dict = coverage.Dictionary({
            'tokens': [],
            'bytes': True,
        })
        super(FuzzSimpleLoopEnv, self).__init__()
