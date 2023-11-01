import hydra


@hydra.main(config_path="config", config_name="config")
def main(cfg):
    print(cfg.pretty())

    # dataloader

    # model

    # optimizer

    # loss

    # train

    # save

    # test


if __name__ == "__main__":
    main()