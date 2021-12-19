import numpy as np
import gym
import sys
from tqdm import tqdm
import time

import gymfuzz as rf

from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Activation, Flatten, Input, Concatenate
from tensorflow.keras.optimizers import Adam
from rl.agents import DDPGAgent
from rl.memory import SequentialMemory
from rl.random import OrnsteinUhlenbeckProcess

import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore',category=FutureWarning)

ENV_NAME = 'FuzzLibXML-v0'

def train(ENV_NAME):
    env = gym.make(ENV_NAME)

    print("Action space: {}".format(env.action_space.n))
    print("Env space shape: {}".format(env.observation_space.shape))
    nb_actions = env.action_space.n
    nb_observation = env.observation_space.shape[0]

    actor_input = Input(shape=(1,) + env.observation_space.shape, name='actor_observation_input')
    f_actor_input = Flatten()(actor_input)
    x = Dense(1024, activation='relu')(f_actor_input)
    x = Dense(128, activation='relu')(x)
    y = Dense(nb_actions, activation='softmax')(x)
    actor = Model(inputs=actor_input, outputs=y, name='Actor')
    actor.summary()

    critic_action_input = Input(shape=(env.action_space.n), name='critic_action_input')
    critic_observation_input = Input(shape=(1,) + env.observation_space.shape, name='critic_observation_input')
    f_critic_observation_input = Flatten()(critic_observation_input)
    x = Concatenate()([critic_action_input, f_critic_observation_input])
    x = Dense(1024, activation='relu')(x)
    x = Dense(128, activation='relu')(x)
    y = Dense(1, activation='sigmoid')(x)
    critic = Model(inputs=[critic_action_input, critic_observation_input], outputs=y, name='Critic')
    critic.summary()

    agent = DDPGAgent(nb_actions=nb_actions, 
                  actor=actor, 
                  critic=critic, 
                  critic_action_input=critic_action_input, 
                  memory=SequentialMemory(limit=100000, window_length=1), 
                  nb_steps_warmup_critic=180,
                  nb_steps_warmup_actor=180,
                  random_process=OrnsteinUhlenbeckProcess(size=nb_actions, theta=.15, mu=0., sigma=.3), 
                  gamma=.99, 
                  target_model_update=1e-3
                 )
    agent.compile(Adam(lr=.001, clipnorm=1.), metrics=['mae'])

    # set done=True after run nb_steps，nb_max_episode_steps
    history = agent.fit(env, nb_steps=20000, visualize=False, verbose=1)

    agent.save_weights('abcd_{}_weights.h5f'.format(ENV_NAME), overwrite=True)


    sns.set("notebook", "darkgrid")
    plt.figure(dpi=300)

    data = env.reward_history
    plt.plot(data, linewidth=1)
    plt.xlabel('step')
    plt.ylabel('reward_history')
    plt.axhline(y=max(data), color='r', linewidth=1, linestyle='--')
    plt.text(0, max(data), str(max(data)), fontdict={'size': 8, 'color': 'r'})
    plt.axhline(y=min(data), color='r', linewidth=1, linestyle='--')
    plt.text(0, min(data), str(min(data)), fontdict={'size': 8, 'color': 'r'})

    plt.savefig('rl_ddpg_{}.png'.format(ENV_NAME))


if __name__ == '__main__':
    
    train(ENV_NAME)
