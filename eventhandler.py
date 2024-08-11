#  The event handler coordinates the handlingof events by the current state.

import sys

import pygame  # type: ignore

import customlogger
from states.state import State


class EventHandler:
    """EventHandler

    The event handler manages the event handlers of the current state.

    """

    @customlogger.log_trace(customlogger.Levels.INFO)
    def __init__(self, currentState: State) -> None:
        """__init__

        Initialises the event handler.

        Args:
            currentState (State): Initial game state whose event handlers need to be managed.
        """
        #  Store current game state.

        self._currentState: State = currentState

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def handleEvents(self) -> None:
        """handlerEvents

        Calls each of the event handlers for the current state.
        """
        #  Call event handlers for each event.

        for _event in pygame.event.get():  # type: ignore
            self.checkQuitEvent(_event)
            self.checkKeyEvent(_event)
            self.checkMouseEvent(_event)
            self.checkJoystickEvent(_event)

    @staticmethod
    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def checkQuitEvent(event: pygame.event.Event) -> None:  # type: ignore
        """checkQuitEvent

        Checks if the event passed to it is a quit event and if so quits the game.

        Args:
            event (pygame.event.Event): event to check.
        """
        #  Check event and quit if neeed

        if event.type == pygame.QUIT:  # type: ignore
            quit()
            sys.exit()

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def updateState(self, newState: State) -> None:
        """updateState

        Sets the new game state.

        Args:
            newState (State): new game state.
        """
        #  Set new game state.

        self._currentState = newState

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def checkKeyEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """checkKeyEvent

        Calls the key event handler for the current game state.

        Args:
            event (pygame.event.Event): event to handle.
        """
        self._currentState.handleKeyEvent(event)

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def checkMouseEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """checkMouseEvent

        Calls the mouse event handler for the current game state.

        Args:
            event (pygame.event.Event): event to handle.
        """
        self._currentState.handleMouseEvent(event)

    @customlogger.log_trace(customlogger.Levels.DEBUG)
    def checkJoystickEvent(self, event: pygame.event.Event) -> None:  # type: ignore
        """checkJoystickEvent

        Calls the joystick event handler for the current game state.

        Args:
            event (pygame.event.Event): event to handle.
        """
        self._currentState.handleJoystickEvent(event)
