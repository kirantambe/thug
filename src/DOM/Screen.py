#!/usr/bin/env python
#
# Screen.py
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA  02111-1307  USA

import PyV8

import logging
log = logging.getLogger("Thug")

class Screen(PyV8.JSClass):
    def __init__(self, width = 800, height = 600, depth = 32):
        self._width  = width
        self._height = height
        self._depth  = depth
        self._left   = 0
        self._top    = 0

        if not log.ThugOpts.Personality.isIE():
            self.pixelDepth = self._pixelDepth

        self.__init_personality()

    def __init_personality(self):
        if log.ThugOpts.Personality.isIE():
            self.__init_personality_IE()
            return

        if log.ThugOpts.Personality.isFirefox():
            self.__init_personality_Firefox()
            return

        if log.ThugOpts.Personality.isChrome():
            self.__init_personality_Chrome()
            return

        if log.ThugOpts.Personality.isSafari():
            self.__init_personality_Safari()
            return

        if log.ThugOpts.Personality.isOpera():
            self.__init_personality_Opera()

    def __init_personality_IE(self):
        pass

    def __init_personality_Firefox(self):
        pass

    def __init_personality_Chrome(self):
        pass

    def __init_personality_Safari(self):
        pass

    def __init_personality_Opera(self):
        pass

    @property
    def availHeight(self):
        """
            The height of the screen (excluding the Windows Taskbar)
        """
        return self._height

    @property
    def availWidth(self):
        """
            The width of the screen (excluding the Windows Taskbar)
        """
        return self._width

    @property
    def colorDepth(self):
        """
            The bit depth of the color palette for displaying images
        """
        return self._depth

    @property
    def height(self):
        """
            The total height of the screen
        """
        return self._heigth

    @property
    def _pixelDepth(self):
        """
            The color resolution (in bits per pixel) of the screen
        """
        return self._depth               

    @property
    def width(self):
        """
            The total width of the screen
        """
        return self._width

    @property
    def availLeft(self):
        """
            The first available pixel available from the left side 
            of the screen
        """
        return self._left + 1

    @property
    def availTop(self):
        """
            The first available pixel from the top of the screen 
            available to the browser
        """
        return self._top + 1

