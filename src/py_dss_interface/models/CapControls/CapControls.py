# -*- encoding: utf-8 -*-
"""
 Created by eniocc at 11/10/2020
"""
from py_dss_interface.models.CapControls.CapControlsF import CapControlsF
from py_dss_interface.models.CapControls.CapControlsI import CapControlsI
from py_dss_interface.models.CapControls.CapControlsS import CapControlsS
from py_dss_interface.models.CapControls.CapControlsV import CapControlsV


class CapControls(CapControlsF, CapControlsI, CapControlsS, CapControlsV):
    pass
