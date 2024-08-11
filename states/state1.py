#  An example instance of a game state.

import pygame  # type: ignore
import pygame.event  # type: ignore

import customlogger
from states.state import State


class State1(State):
    """State1

    Args:
        State: this subclasses State.
    """

    #  PROPERTIES

    @property
    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def nextState(self) -> str:
        """nextState

        Gets the next game state.

        Returns:
            str: the next game state.
        """
        return self._nextState

    #  GAME LOOP METHODS

    @customlogger.log_trace(customlogger.Levels.INFO)
    def __init__(self) -> None:
        """__init__

        Initialises the game state.

        """
        self._nextState: str = ""
        self._done: bool = False

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def handleKeyEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """handleKeyEvent

        Handles keyboard events.
        Coordinates the handling of events by other classes.

        Args:
            event (pygame.event.Event): event to handle.
        """
        ...

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def handleMouseEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """handleMouseEvent

        Handles mouse events.
        Coordinates the handling of events by other classes.

        Args:
            event (pygame.event.Event): event to handle.
        """
        ...

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def handleJoystickEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """handleJoystickEvent

        Handles joystick events.
        Coordinates the handling of events by other classes.

        Args:
            event (pygame.event.Event): event to handle.
        """
        ...

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def update(self, dt: float) -> None:
        """udate

        Updates the class.
        Coordinates the updating of all other classes.

        Args:
            dt (float): delta time
        """
        ...

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def render(self, display: pygame.Surface, actualFPS: float) -> None:  # type: ignore
        """render

        Renders the class.
        Coordinates the rendering of all other classes.

        Args:
            display (pygame.event.Event): display on which to render.
            actualFPS (float): actual frames per second.
        """
        ...

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def checkDone(self) -> bool:
        """checkDone

        Checks if the current state is completed.

        Returns:
            bool: true if completed.
        """
        ...

        return self._done
