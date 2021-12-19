import gym
import gymfuzz  # noqa F401
import numpy as np


def main():
    env = gym.make('FuzzSimpleLoop-v0')
    print("dict_size={} eof={}".format(env.dict_size(), env.eof()))

    env.reset()

    inputs = [
        [0, 256] + [0] * 6,
        [0, 4, 256] + [0] * 5,
        [42, 1, 256] + [0] * 5,
        [42, 2, 256] + [0] * 5,
        [42, 4, 256] + [0] * 5,
        [42, 8, 256] + [0] * 5,
        [42, 64, 256] + [0] * 5,
        [42, 255, 256] + [0] * 5,
        [42, 13, 256] + [0] * 5,
    ]

    for i in inputs:
        obs, reward, done, info = env.step(np.array(i))

        print(("STEP:" +
               "step={}/{}/{} " +
               "action={} transitions={}").format(
                   info['step_coverage'].skip_path_count(),
                   info['step_coverage'].transition_count(),
                   info['step_coverage'].crash_count(),
                   i[:8],
                   info['step_coverage'].transitions,
               ))


if __name__ == "__main__":
    main()
