#  The main .py file provides the main program entry point; it initilises the game environment and starts the controller.

import configparser

import pygame  # type: ignore

import constants as c
import controller
import customlogger
import init
from states.state import State


@customlogger.log_trace(customlogger.Levels.INFO)
def main() -> None:
    """main

    The main program entry.

    (Logging is initialised when the file is executed on inclusion.)
    Sets up/creates the config parser and reads settings.
    Sets the logging level of the custom logger.
    Sets up all the elements of the game engine by calling methods from the init.py file.
    Starts the game controller.

    """
    #  Read the configuration file (create it if it doesn't exist) and get logging level.

    _configParser: configparser.ConfigParser = init.getConfig(c.GAME_NAME)
    _loggingLevel = _configParser.get("logging", "logging_level")

    #  Set the logging level.

    customlogger.log_level(_loggingLevel)

    #  Get the pygame display surface.

    _display: pygame.Surface = init.getDisplay(c.GAME_TITLE)  #  type: ignore

    #  Get the pygame clock.

    _clock: pygame.time.Clock = init.getClock()  #  type: ignore

    #  Load the game states.

    _gameStates: dict[str, State] = init.getGameStates()

    #  Get the controller and start the game loop.

    _controller: controller.Controller = init.getController(
        _display, _clock, _gameStates, c.INITIAL_STATE
    )
    _controller.run_game()


if __name__ == "__main__":
    main()
