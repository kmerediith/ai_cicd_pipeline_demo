from .cli import main as cli_main
import os


def main() -> None:
    # Call the CLI callback directly with the default config path.
    default_cfg = os.path.join(os.getcwd(), "configs", "pipeline.example.yaml")
    # cli_main is a Typer callback function; call it directly with the config path
    cli_main(config=default_cfg)


if __name__ == "__main__":
    main()
