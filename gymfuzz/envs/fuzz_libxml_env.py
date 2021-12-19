import gymfuzz
import gymfuzz.coverage as coverage

from gymfuzz.envs.fuzz_base_env import FuzzBaseEnv


class FuzzLibXMLEnv(FuzzBaseEnv):
    def __init__(self):
        self._input_size = 1024
        self._target_path = gymfuzz.libxml_target_path()
        self._args = []
        self._dict = coverage.Dictionary({
            'tokens': [],
            'bytes': True,
        })
        super(FuzzLibXMLEnv, self).__init__()