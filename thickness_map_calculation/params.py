params = {}
params["img_shape"] = (512, 512, 3)
params["batch_size"] = 2
params["epochs"] = 1
params["learning_rate"] = 0.001
params["continuing_training"] = False
params["data_dir"] = "./data"
params["save_path"] = "./output"
params["loss_function"] = "dice_loss"
params["n_filters"] = 32
params["batchnorm"] = True
params["dropout"] = 0.2