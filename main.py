import argparse

from hrac.train import run_hrac, run_star, run_hiro

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--algo", default="hrac", type=str)
    parser.add_argument("--seed", default=2, type=int)
    parser.add_argument("--eval_freq", default=5e3, type=float)
    parser.add_argument("--max_timesteps", default=5e6, type=float)
    parser.add_argument("--max_steps_eps", default=500, type=int)
    parser.add_argument("--save_models", action="store_true")
    parser.add_argument("--env_name", default="AntMaze", type=str)
    parser.add_argument("--load", default=False, type=bool)
    parser.add_argument("--log_dir", default="./logs", type=str)
    parser.add_argument("--no_correction", action="store_true")
    parser.add_argument("--inner_dones", action="store_true")
    parser.add_argument("--absolute_goal", action="store_true")
    parser.add_argument("--binary_int_reward", action="store_true")
    parser.add_argument("--load_adj_net", default=False, action="store_true")
    parser.add_argument("--load_fwd_model", default=False, action="store_true")

    parser.add_argument("--gid", default=0, type=int)
    parser.add_argument("--traj_buffer_size", default=50000, type=int)
    parser.add_argument("--lr_r", default=2e-4, type=float)
    parser.add_argument("--r_margin_pos", default=1.0, type=float)
    parser.add_argument("--r_margin_neg", default=1.2, type=float)
    parser.add_argument("--r_training_epochs", default=25, type=int)
    parser.add_argument("--r_batch_size", default=64, type=int)
    parser.add_argument("--r_hidden_dim", default=128, type=int)
    parser.add_argument("--r_embedding_dim", default=32, type=int)
    parser.add_argument("--goal_loss_coeff", default=20, type=float)
    parser.add_argument("--goal_reward_coeff", default=1, type=float)

    parser.add_argument("--lr_fwd", default=1e-3, type=float)
    parser.add_argument("--fwd_training_epochs", default=3, type=int)
    parser.add_argument("--fwd_batch_size", default=64, type=int)
    parser.add_argument("--fwd_hidden_dim", default=32, type=int)
    parser.add_argument("--fwd_embedding_dim", default=32, type=int)
    
    parser.add_argument("--boss_propose_freq", default=30, type=int) # k 
    parser.add_argument("--train_boss_freq", default=1000, type=int)
    parser.add_argument("--manager_propose_freq", default=10, type=int) # l
    parser.add_argument("--train_manager_freq", default=10, type=int)
    parser.add_argument("--man_discount", default=0.99, type=float)
    parser.add_argument("--ctrl_discount", default=0.95, type=float)

    # Boss Parameters
    parser.add_argument("--boss_batch_size", default=64, type=int)
    parser.add_argument("--boss_buffer_size", default=100000, type=int)
    parser.add_argument("--boss_buffer_min_size", default=5000, type=int)
    parser.add_argument("--boss_policy", default="Q-learning", type=str) # Do not change
    parser.add_argument("--boss_discount_factor", default=0.99, type=float) 
    parser.add_argument("--boss_alpha", default=0.01, type=float) 
    parser.add_argument("--reach_algo", default="Ai2", type=str) # Do not change
    parser.add_argument("--boss_eps", default=0.99, type=int)
    parser.add_argument("--boss_eps_min", default=0.01, type=int)
    parser.add_argument("--boss_eps_decay", default=0.9995, type=float)
    
    # Partition Parametres for STAR
    parser.add_argument("--t_re", default=0.7, type=float)
    parser.add_argument("--t_unre", default=0.01, type=float)


    # Manager Parameters
    parser.add_argument("--man_soft_sync_rate", default=0.005, type=float)
    parser.add_argument("--man_batch_size", default=128, type=int)
    parser.add_argument("--man_buffer_size", default=2e5, type=int)
    parser.add_argument("--man_rew_scale", default=0.1, type=float)
    parser.add_argument("--man_act_lr", default=1e-4, type=float)
    parser.add_argument("--man_crit_lr", default=1e-3, type=float)
    parser.add_argument("--candidate_goals", default=10, type=int)

    # Controller Parameters
    parser.add_argument("--ctrl_soft_sync_rate", default=0.005, type=float)
    parser.add_argument("--ctrl_batch_size", default=128, type=int)
    parser.add_argument("--ctrl_buffer_size", default=2e5, type=int)
    parser.add_argument("--ctrl_rew_scale", default=1.0, type=float)
    parser.add_argument("--ctrl_act_lr", default=1e-4, type=float)
    parser.add_argument("--ctrl_crit_lr", default=1e-3, type=float)

    # Noise Parameters
    parser.add_argument("--noise_type", default="normal", type=str)
    parser.add_argument("--ctrl_noise_sigma", default=1., type=float)
    parser.add_argument("--man_noise_sigma", default=1., type=float)

    # Experiment Number
    parser.add_argument("--exp", default="0", type=str)

    # Run the algorithm
    args = parser.parse_args()

    if args.env_name in ["AntGather", "AntMazeSparse"]:
        args.man_rew_scale = 1.0
        if args.env_name == "AntGather":
            args.inner_dones = True
    
    if args.env_name == "AntFall":
        args.boss_alpha = 0.005

    print('=' * 30)
    for key, val in vars(args).items():
        print('{}: {}'.format(key, val))

    if args.algo == "hrac":
        for exp in range(1):
            args.exp = str(exp) 
            run_hrac(args)
    elif args.algo == "star":
        for exp in range(1):
            args.exp = str(exp) 
            run_star(args)  
    elif args.algo == "hiro":
        for exp in range(1):
            args.exp = str(exp) 
            run_hiro(args) 
    else:
        raise NotImplementedError
