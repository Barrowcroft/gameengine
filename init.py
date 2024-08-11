#  The init.py file provides a number of initialisation methods used by the main.py file.

import configparser
import os
from typing import Any

import pygame  # type: ignore

import constants as c
import controller
import customlogger
from states.state import State
from states.state1 import State1


@customlogger.log_trace(customlogger.Levels.INFO)
def getConfig(name: str) -> configparser.ConfigParser:
    """getConfig

    Args:
        name (str): filename to read from.

    Initialises the config parser and reads the config from the given file.
    If the config file does not exist it will be created and default logging level (INFO) set.

    Returns:
        ConfigParser: the config parser.
    """
    #  Set up logging file.

    _filename = os.path.join(os.getcwd(), f"{c.GAME_NAME}.ini")

    _configParser: configparser.ConfigParser = configparser.ConfigParser()

    if os.path.exists(_filename):
        _configParser.read(_filename)
    else:
        _configParser["logging"] = {"logging_level": "INFO"}
        with open(_filename, "w") as configfile:
            _configParser.write(configfile)

    return _configParser


@customlogger.log_trace(customlogger.Levels.INFO)
def getDisplay(gameTitle: str) -> pygame.Surface:  # type: ignore
    """getDisplay

    Initialises the pygame display.

    Args:
        gameTitle (str): title for screen.

    Returns:
        Surface: main game surface.
    """
    pygame.init()  # type: ignore
    pygame.mixer.init()  # type: ignore

    _flags = pygame.DOUBLEBUF | pygame.NOFRAME  # type: ignore

    _display: pygame.Surface = pygame.display.set_mode(c.SCREEN_SIZE, _flags)  # type: ignore
    pygame.display.set_caption(gameTitle)  # type: ignore

    return _display  # type: ignore


@customlogger.log_trace(customlogger.Levels.INFO)
def getClock() -> pygame.time.Clock:  # type: ignore
    """getClock

    Initialises the clock.

    Returns:
        Clock: the clock.
    """
    _clock: pygame.time.Clock = pygame.time.Clock()  # type: ignore

    return _clock  # type: ignore


@customlogger.log_trace(customlogger.Levels.INFO)
def getGameStates() -> dict[str, State]:
    """getGameStates

    Initialises the dictionary containing the game states.

    Returns:
        dict[str, State]: dictionary of game states.
    """
    _gamestates: dict[str, Any] = {
        c.GAME_STATE: State1,
    }
    return _gamestates


@customlogger.log_trace(customlogger.Levels.INFO)
def getController(
    display: pygame.Surface,  # type: ignore
    clock: pygame.time.Clock,  # type: ignore
    gamestates: dict[str, State],
    startingState: str,
) -> controller.Controller:
    """getController

    Gets the game controller.

    """
    _controller: controller.Controller = controller.Controller(
        display, clock, gamestates, startingState
    )

    return _controller
