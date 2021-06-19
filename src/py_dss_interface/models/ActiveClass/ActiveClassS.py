# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""

from py_dss_interface.models.Base import Base


class ActiveClassS(Base):
    """
    This interface can be used to read/modify the properties of the ActiveClass Class where the values are strings.

    The structure of the interface is as follows:
        CStr ActiveClassI(int32_t Parameter, CStr argument)

    This interface returns a string, the first parameter is used to specify the property of the class to be used
    and the second parameter can be used to modify the value of the property when necessary. Reading and writing
    properties are separated and require a different parameter number to be executed.

    The properties (parameter) are integer numbers and are described as follows.
    """

    # TODO: if return is str:'0' we can't get the name
    def active_class_get_name(self) -> str:
        """Gets the name of the active Element of the Active class."""
        return (self.dss_obj.ActiveClassS(0, 0)).decode('ascii')

    # TODO: need more research about this method
    # def active_class_write_name(self, argument) -> str:
    #     """Sets the name of the active Element of the Active class.
    #     : TODO: After sets the name what is the return type? str or int? How can I treat this? >=0 is ok?
    #     """
    #     return (self.dss_obj.ActiveClassS(1, argument.encode('ascii'))).decode('ascii')
    #     # result = ctypes.c_char_p(self.dss_obj.DSSLoadsS(ctypes.c_int32(1), ))
    #     # return result.value.decode('ascii')

    def active_class_get_class_name(self) -> str:
        """Sets the name of the active Element of the Active class.
         TODO: After sets the name what is the return type? str or int? How can I treat this? >=0 is ok?
         """
        return (self.dss_obj.ActiveClassS(2, 0)).decode('ascii')

    def active_class_parent_class_name(self) -> str:
        """Gets the name of the Parent Element of the Active class."""
        return (self.dss_obj.ActiveClassS(3, 0)).decode('ascii')
