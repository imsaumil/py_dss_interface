# -*- coding: utf-8 -*-
# @Time    : 8/26/2021 09:40 PM
# @Author  : Rodolfo Londero
# @Email   : rodolfpl@gmail.com
# @File    : test_dssinterface.py
# @Software: PyCharm


import pytest
import platform
import os


class TestDSSInterface13Bus:

    @pytest.fixture(autouse=True)
    def _request(self, solve_snap_13bus):
        self.dss = solve_snap_13bus

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_dss_num_circuits(self):
        expected = 1
        actual = self.dss.dss_num_circuits()
        assert expected == actual

    def test_dss_clear_all(self):
        expected = 0
        actual = self.dss.dss_clear_all()
        assert expected == actual

    def test_dss_show_panel(self):
        expected = 0
        actual = self.dss.dss_show_panel()
        assert expected == actual

    def test_dss_start(self):
        expected = 1
        actual = self.dss.dss_start()
        assert expected == actual

    def test_dss_num_classes(self):
        expected = 52
        actual = self.dss.dss_num_classes()
        assert expected == actual

    def test_dss_num_user_classes(self):
        expected = 0
        actual = self.dss.dss_num_user_classes()
        assert expected == actual

    def test_dss_reset(self):
        expected = 0
        actual = self.dss.dss_reset()
        assert expected == actual

    def test_dss_read_allow_forms(self):
        expected = 0
        actual = self.dss.dss_read_allow_forms()
        assert expected == actual

    # TODO: Not writing, always returning 0
    # def test_dss_write_allow_forms(self):
    #     expected = 1
    #     self.dss.dss_write_allow_forms(expected)
    #     actual = self.dss.dss_read_allow_forms()
    #     assert expected == actual

    # ===================================================================
    # String methods
    # ===================================================================
    def test_dss_new_circuit(self):
        expected = 'New Circuit'
        actual = self.dss.dss_new_circuit('new_rest_circuit')
        assert expected == actual

    def test_dss_version(self):
        expected = 'Version 9.3.0.1 (64-bit build); License Status: Open '
        actual = self.dss.dss_version()
        assert expected == actual

    def test_dss_read_datapath(self):
        expected = ''
        actual = self.dss.dss_read_datapath()
        assert expected == actual

    # TODO Paulo: Not writing datapath, the read method returns '' afeter write
    # def test_dss_write_datapath(self):
    #     expected = 'C:'
    #     self.dss.dss_write_datapath(expected)
    #     actual = self.dss.dss_read_datapath()
    #     assert expected == actual

    def test_dss_default_editor(self):
        expected = 'Notepad.exe'
        actual = self.dss.dss_default_editor()
        assert expected == actual
