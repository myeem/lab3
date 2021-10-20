from environs import Env

env = Env()
env.read_env()

SERVER = env.str('SERVER')
PORT = env.int('PORT')