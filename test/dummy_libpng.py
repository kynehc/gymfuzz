import gym
import gymfuzz.coverage as coverage
import numpy as np


def main():
    env = gym.make('FuzzLibPNG-v0')
    print("dict_size={} eof={}".format(env.dict_size(), env.eof()))

    env.reset()
    c = coverage.Coverage()

    inputs = [
        [1, env.eof()] + [0] * 1022,
        [env.eof()] + [0] * 1023,
        [1, env.eof()] + [0] * 1022,
    ]

    for i in inputs:
        obs, reward, done, info = env.step(np.array(i))
        c.add(info['step_coverage'])

        print(("STEP: reward={} done={} " +
               "step={}/{}/{} total={}/{}/{} " +
               "sum={}/{}/{} action={}").format(
                  reward, done,
                  info['step_coverage'].skip_path_count(),
                  info['step_coverage'].transition_count(),
                  info['step_coverage'].crash_count(),
                  info['total_coverage'].skip_path_count(),
                  info['total_coverage'].transition_count(),
                  info['total_coverage'].crash_count(),
                  c.skip_path_count(),
                  c.transition_count(),
                  c.crash_count(),
                  i[:13],
              ))
        if done:
            env.reset()
            print("DONE!")


if __name__ == "__main__":
    main()
