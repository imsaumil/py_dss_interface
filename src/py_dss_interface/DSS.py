# -*- coding: iso-8859-15 -*-
import ctypes
import json
import os
import pathlib

from . import ActiveClass, Bus, CapControls, Capacitors, Circuit, CktElement, CMathLib, CtrlQueue, DSSElement
from . import DSSExecutive, DSSInterface, DSSProgress, DSSProperties, ErrorOpenDSS, Fuses, Generators, ISources
from . import LineCodes, Lines, Loads, LoadShapes, Meters, Monitors, Parallel, Parser, PDElements, PVSystems, Reclosers
from . import Relays, RegControls, Sensors, Settings, Solution, SwtControls, Text, Topology, Transformers, VSources
from . import XYCurves
from .utils.System import System

DLL_NAME_WIN = "OpenDSSDirect.dll"
DLL_NAME_LINUX = "libopendssdirect.so"


class DSS(Bus, CapControls, Capacitors, Circuit, CktElement, CMathLib, CtrlQueue, DSSElement,
          DSSExecutive, DSSInterface, DSSProgress, DSSProperties, ErrorOpenDSS, Fuses, Generators, Lines, Loads,
          ISources, LineCodes, LoadShapes, Meters, Monitors, Parallel, Parser, PDElements, PVSystems, Reclosers,
          Relays, RegControls, Sensors, Settings, Solution, SwtControls, Text, Topology, Transformers, VSources,
          XYCurves):
    dll_folder: str
    dll_path: str
    my_dss_version: ctypes.c_char_p
    dss_obj: ctypes.cdll
    started = False
    memory_commands = []
    class_commands = []



    # TODO need to be able to get different dll names:
    #  https://www.youtube.com/watch?v=74hCbYfdZdU&list=PLhdRxvt3nJ8x74v7XWcp6iLJL_nCOjxjK&index=9&t=2827s
    def __init__(self, dll_folder_param=None, dll_by_user=None):
        # TODO: dss_write_allowforms
        """
        Class to create an OpenDSS object
        :param dll_folder_param: None will use the OpenDSS available within the package. The dll path allows to use a
        different OpenDSS
        """
        self.started = False
        if dll_folder_param is not None and dll_by_user is not None:
            os.chdir(dll_folder_param)
            self.dss_obj = ctypes.cdll.LoadLibrary(os.path.join(dll_folder_param, dll_by_user))
            self.started = True
        elif dll_by_user is None:
            if dll_folder_param is None:
                dll_folder_param = os.path.join(pathlib.Path(os.path.dirname(os.path.abspath(__file__))), "dll")
            if System.detect_platform() == 'Linux':
                dll_folder_param = pathlib.Path(dll_folder_param)
                dll_by_user = DLL_NAME_LINUX
            elif System.detect_platform() == 'Windows':
                dll_folder_param = pathlib.Path(dll_folder_param)
                dll_by_user = DLL_NAME_WIN

            self.dll_path = System.get_architecture_path(dll_folder_param)
            self.dll_file_path = os.path.join(self.dll_path, dll_by_user)
            self.dss_obj = ctypes.cdll.LoadLibrary(self.dll_file_path)
            self.started = True
        if self.started:
            self.load_json()
            self._allocate_memory()

            if self.check_started():
                self.active_class = ActiveClass()

                self.instantiate_all_dss_objects()
                print(f"OpenDSS Started successfully! \nOpenDSS {self.my_dss_version.value.decode('ascii')}\n\n")

            else:
                print("OpenDSS Failed to Start")
                exit()
        else:
            print("An error occur!")
            exit()

    def instantiate_all_dss_objects(self):
        self.active_class.dss_obj = self.dss_obj

    def check_started(self):
        if int(self.dss_obj.DSSI(ctypes.c_int32(3), ctypes.c_int32(0))) != 1:
            return False
        # TODO: Need refactor this call to use a method that already exists
        self.my_dss_version = ctypes.c_char_p(self.dss_obj.DSSS(ctypes.c_int32(1), "".encode('ascii')))
        return True

    def load_json(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f'{dir_path}/configurations.json') as json_f:
            data = json.load(json_f)
            for n in data['structured_data']:
                for t in n['types']:
                    if t == 'F':
                        ctype = 'c_double'
                    elif t == 'S':
                        ctype = 'c_char_p'
                    command_ = 'self.dss_obj.' + n['name'] + t + '.restype' + ' = ' + 'ctypes.' + ctype
                    self.memory_commands.append(command_)

    def _allocate_memory(self):
        self.dss_obj.DSSPut_Command.restype = ctypes.c_char_p
        self.dss_obj.DSSProperties.restype = ctypes.c_char_p

        for i in self.memory_commands:
            exec(i)
