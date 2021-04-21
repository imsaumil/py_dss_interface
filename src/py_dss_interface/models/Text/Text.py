# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
import ctypes
from py_dss_interface.models.Base import Base


class Text(Base):

    # Text Interface
    def text(self, argument):
        """Can be used to send commands to the text interface of OpenDSS (DSS.Text)."""
        # ctypes.c_char_p(self.dss_obj.DSSPut_Command(argument.encode('ascii')))
        result = ctypes.c_char_p(self.dss_obj.DSSPut_Command(argument.encode('ascii')))
        return result.value.decode("ascii")
