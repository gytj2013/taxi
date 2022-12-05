import numpy as np
import gym
from tqdm import tqdm
import random
import time

from IPython.display import clear_output

env = gym.make('Taxi-v3')
    
def evaluate_policy(q, n=50):
    acc_returns = 0
    for i in range(n):
        terminated = False
        s = env.reset()
        while not terminated:
            a = np.argmax(q[s,:])
            s, reward, terminated, info = env.step(a)
            acc_returns += reward

    return acc_returns / n

def sarsa(alpha=0.1, gamma=0.6, epsilon=1., q=None, env=env):
    if q is None:
        state_size = env.observation_space.n
        action_size = env.action_space.n
        q = np.zeros((state_size, action_size))

    nb_episodes = 20000
    steps = 100
    progress = []
    for i in tqdm(range(nb_episodes)):
        terminated = False
        s = env.reset()
        while not terminated :
            if random.uniform(0,1) < epsilon:
                a = env.action_space.sample()
            else:
                a = np.argmax(q[s,:])
                
            new_s, reward, terminated, info = env.step(a)
            
            q[s,a] = q[s,a] + alpha * (reward + gamma * np.max(q[new_s,:]) - q[s,a])
            s = new_s
            
        epsilon = 0.01 + (0.09) * np.exp(- 0.0005 * i)

        if i%steps == 0:
            progress.append(evaluate_policy(q, n=50))

    return q, progress

def show(q) :
    for i in range(10):
        total_reward = 0
        s = env.reset()
        terminated = False
        while not terminated :
            clear_output(wait = True)
            print(f'Episode {i+1}')

            env.render()
            a = np.argmax(q[s])
            s, reward, terminated, info  = env.step(a)
            total_reward += reward
            if total_reward<-20 : break
            print(f'Step reward: {reward}')
            print(f'Total reward: {total_reward}')

            time.sleep(0.3)
            
        print('Episode done')
        time.sleep(2)

if __name__ == '__main__':
    q, progress = sarsa()
    print(progress)
    print(max(progress))
    print(evaluate_policy(q, n=10))
    show(q)
