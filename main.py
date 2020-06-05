import sys
import click
from corpobot.logger import logger
from corpobot import CORPOBOT_VERION
from corpobot.app import Application


@click.command()
@click.option("--config", help="Your .env file location")
def main(config):
    """ CorpoBot is application which helps you automate boring tasks at work. """

    if not config:
        logger.warning("No .env file specified! Goodbye!")
        return

    logger.info(f"Welcome to CorpoBot ! v.{CORPOBOT_VERION}")
    Application().run()


if __name__ == "__main__":
    sys.exit(main())
