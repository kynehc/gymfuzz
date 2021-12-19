import gym

from gym import spaces

import gymfuzz.coverage as coverage
from gymfuzz.envs.fuzz_mutator import FuzzMutator
import numpy as np
import os, datetime

class FuzzBaseEnv(gym.Env):
    def __init__(self):
        # Classes that inherit FuzzBase must define before calling this
        # constructor:
        # - self._input_size
        # - self._dict
        # - self._target_path
        # - self._args
        self.engine = coverage.Afl(self._target_path, args=self._args)
        self.mutator = FuzzMutator(self._input_size)
        self.m_seed = [1,2,3,4,5,6,7,8,9,10]
        self.last_state = list(self.m_seed) + [self._dict.eof()] + [0] * (self._input_size - len(self.m_seed) - 1)
        
        self.reward_history = []
        self.input_len_history = []
        self.mutate_history = []

        self.observation_space = spaces.Box(
            0, self._dict.eof(), shape=(self._input_size,), dtype='int32',
        )
        
        self.action_space = spaces.Discrete(self.mutator.methodNum)

        self.reset()

    def reset(self):
        self.total_coverage = coverage.Coverage()
        self.reward_history = []
        self.input_len_history = []
        self.mutate_history = []
        self.unique_path_history = []
        self.transition_count = []
        return list(self.m_seed) + [self._dict.eof()] + [0] * (self._input_size - len(self.m_seed) - 1)

    def step_raw(self, action):
        if self.action_space.contains(action):
            mutate = action
        else:
            mutate = np.argmax(action)
        assert self.action_space.contains(mutate)

        input_data = b""
        last_state = self.last_state

        # list convert to bytes
        for i in range(self._input_size):
            if int(last_state[i]) == self._dict.eof():
                break
            input_data += self._dict.bytes(int(last_state[i]))

        # action to input_data
        input_data = self.mutator.mutate(mutate, input_data)

        self.input_len_history.append(len(input_data))
        self.mutate_history.append(mutate)

        c = self.engine.run(input_data)

        self.last_state = self.bytes_to_array(input_data)

        crash_flag = False
        if c.crash_count() > 0:
            print("CRASH {}".format(input_data))
            crash_flag = True

        return {
            "step_coverage": c,
            "crash_info": crash_flag,
            "input_data": input_data,
        }

    def step(self, action):
        info = self.step_raw(action)

        reward = 0.0
        done = False
        c = info['step_coverage']

        reward = c.transition_count()

        old_path_count = self.total_coverage.skip_path_count()
        self.total_coverage.add(c)
        new_path_count = self.total_coverage.skip_path_count()

        if info['crash_info']:
            done = True
            name = '{}-{}'.format(os.path.basename(self._target_path), datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f'))
            print(' [+] Find {}'.format(name))
            with open(os.path.join("./crashes", name), 'wb') as fp:
                fp.write(info['input_data'])
        else:
            done = False

        self.reward_history.append(reward)

        # if old_path_count == new_path_count:
        #     done = True

        info['total_coverage'] = self.total_coverage

        state = [i for i in info['input_data']]
        trail = [0] * (self._input_size - len(state))
        state += trail
        if len(info['input_data']) < self._input_size-1:
            state[len(info['input_data'])] = self._dict.eof()
        else:
            state[len(info['input_data'])-1] = self._dict.eof()

        return state, reward, done, {}

    def render(self, mode='human', close=False):
        pass

    def eof(self):
        return self._dict.eof()

    def dict_size(self):
        return self._dict.size()

    def input_size(self):
        return self._input_size

    def bytes_to_array(self, input_data):
        cur_obs = [0] * self._input_size
        for i in range(len(input_data)):
            cur_obs[i] = input_data[i]
        if len(input_data) <= self._input_size-1:
            cur_obs[len(input_data)] = self._dict.eof()
        else:
            cur_obs[-1] = self._dict.eof()
        
        return cur_obs
