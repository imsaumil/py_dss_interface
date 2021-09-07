# -*- coding: utf-8 -*-
# @Time     : 09/07/2021 02:18 AM
# @Author   : Rodolfo Londero
# @Email    : rodolfopl@gmail.com
# @File     : test_regcontrols.py
# @Software : VSCode

import os
import pytest


class TestRegcontrols13Bus:

    @pytest.fixture(autouse=True)
    def _request(self, solve_snap_13bus):
        self.dss = solve_snap_13bus
        self.dss.regcontrols_write_name('reg1')
        self.dss.solution_solve()

    # ===================================================================
    # Integer methods
    # ===================================================================
    def test_regcontrols_first(self):
        expected = 1
        actual = self.dss.regcontrols_first()
        assert expected == actual

    def test_regcontrols_next(self):
        expected = 2
        actual = self.dss.regcontrols_next()
        assert expected == actual

    def test_regcontrols_read_tap_winding(self):
        expected = 2
        actual = self.dss.regcontrols_read_tap_winding()
        assert expected == actual

    def test_regcontrols_write_tap_winding(self):
        expected = 1
        self.dss.regcontrols_write_tap_winding(expected)
        actual = self.dss.regcontrols_read_tap_winding()
        assert expected == actual

    def test_regcontrols_read_winding(self):
        expected = 2
        actual = self.dss.regcontrols_read_winding()
        assert expected == actual

    def test_regcontrols_write_winding(self):
        expected = 1
        self.dss.regcontrols_write_winding(expected)
        actual = self.dss.regcontrols_read_winding()
        assert expected == actual

    def test_regcontrols_read_is_reversible(self):
        expected = 0
        actual = self.dss.regcontrols_read_is_reversible()
        assert expected == actual

    def test_regcontrols_write_is_reversible(self):
        expected = 1
        self.dss.regcontrols_write_is_reversible(expected)
        actual = self.dss.regcontrols_read_is_reversible()
        assert expected == actual

    def test_regcontrols_read_is_inverse_time(self):
        expected = 0
        actual = self.dss.regcontrols_read_is_inverse_time()
        assert expected == actual

    def test_regcontrols_write_is_inverse_time(self):
        expected = 1
        self.dss.regcontrols_write_is_inverse_time(expected)
        actual = self.dss.regcontrols_read_is_inverse_time()
        assert expected == actual

    def test_regcontrols_read_max_tap_change(self):
        expected = 16
        actual = self.dss.regcontrols_read_max_tap_change()
        assert expected == actual

    def test_regcontrols_write_max_tap_change(self):
        expected = 12
        self.dss.regcontrols_write_max_tap_change(expected)
        actual = self.dss.regcontrols_read_max_tap_change()
        assert expected == actual

    def test_regcontrols_count(self):
        expected = 3
        actual = self.dss.regcontrols_count()
        assert expected == actual

    def test_regcontrols_read_tap_number(self):
        expected = 9
        actual = self.dss.regcontrols_read_tap_number()
        assert expected == actual

    def test_regcontrols_write_tap_number(self):
        expected = 16
        self.dss.regcontrols_write_tap_number(expected)
        actual = self.dss.regcontrols_read_tap_number()
        assert expected == actual

    # ===================================================================
    # Float methods
    # ===================================================================
    def test_regcontrols_read_ct_primary(self):
        expected = 700
        actual = self.dss.regcontrols_read_ct_primary()
        assert expected == actual

    def test_regcontrols_write_ct_primary(self):
        expected = 600
        self.dss.regcontrols_write_ct_primary(expected)
        actual = self.dss.regcontrols_read_ct_primary()
        assert expected == actual

    def test_regcontrols_read_pt_ratio(self):
        expected = 20
        actual = self.dss.regcontrols_read_pt_ratio()
        assert expected == actual

    def test_regcontrols_write_pt_ratio(self):
        expected = 15
        self.dss.regcontrols_write_pt_ratio(expected)
        actual = self.dss.regcontrols_read_pt_ratio()
        assert expected == actual

    def test_regcontrols_read_forward_r(self):
        expected = 3
        actual = self.dss.regcontrols_read_forward_r()
        assert expected == actual

    def test_regcontrols_write_forward_r(self):
        expected = 4
        self.dss.regcontrols_write_forward_r(expected)
        actual = self.dss.regcontrols_read_forward_r()
        assert expected == actual

    def test_regcontrols_read_forward_x(self):
        expected = 9
        actual = self.dss.regcontrols_read_forward_x()
        assert expected == actual

    def test_regcontrols_write_forward_x(self):
        expected = 8
        self.dss.regcontrols_write_forward_x(expected)
        actual = self.dss.regcontrols_read_forward_x()
        assert expected == actual

    def test_regcontrols_read_reverse_r(self):
        expected = 0
        actual = self.dss.regcontrols_read_reverse_r()
        assert expected == actual

    def test_regcontrols_write_reverse_r(self):
        expected = 5
        self.dss.regcontrols_write_reverse_r(expected)
        actual = self.dss.regcontrols_read_reverse_r()
        assert expected == actual

    def test_regcontrols_read_reverser_x(self):
        expected = 0
        actual = self.dss.regcontrols_read_reverser_x()
        assert expected == actual

    def test_regcontrols_write_reverser_x(self):
        expected = 5
        self.dss.regcontrols_write_reverser_x(expected)
        actual = self.dss.regcontrols_read_reverser_x()
        assert expected == actual

    def test_regcontrols_read_delay(self):
        expected = 15
        actual = self.dss.regcontrols_read_delay()
        assert expected == actual

    def test_regcontrols_write_delay(self):
        expected = 10
        self.dss.regcontrols_write_delay(expected)
        actual = self.dss.regcontrols_read_delay()
        assert expected == actual

    def test_regcontrols_read_tap_delay(self):
        expected = 2
        actual = self.dss.regcontrols_read_tap_delay()
        assert expected == actual

    def test_regcontrols_write_tap_delay(self):
        expected = 1
        self.dss.regcontrols_write_tap_delay(expected)
        actual = self.dss.regcontrols_read_tap_delay()
        assert expected == actual

    def test_regcontrols_read_voltage_limit(self):
        expected = 0
        actual = self.dss.regcontrols_read_voltage_limit()
        assert expected == actual

    def test_regcontrols_write_voltage_limit(self):
        expected = 1
        self.dss.regcontrols_write_voltage_limit(expected)
        actual = self.dss.regcontrols_read_voltage_limit()
        assert expected == actual

    def test_regcontrols_read_forward_band(self):
        expected = 2
        actual = self.dss.regcontrols_read_forward_band()
        assert expected == actual

    def test_regcontrols_write_forward_band(self):
        expected = 1
        self.dss.regcontrols_write_forward_band(expected)
        actual = self.dss.regcontrols_read_forward_band()
        assert expected == actual

    def test_regcontrols_read_forward_vreg(self):
        expected = 122
        actual = self.dss.regcontrols_read_forward_vreg()
        assert expected == actual

    def test_regcontrols_write_forward_vreg(self):
        expected = 111
        self.dss.regcontrols_write_forward_vreg(expected)
        actual = self.dss.regcontrols_read_forward_vreg()
        assert expected == actual

    def test_regcontrols_read_reverse_band(self):
        expected = 3
        actual = self.dss.regcontrols_read_reverse_band()
        assert expected == actual

    def test_regcontrols_write_reverse_band(self):
        expected = 12
        self.dss.regcontrols_write_reverse_band(expected)
        actual = self.dss.regcontrols_read_reverse_band()
        assert expected == actual

    def test_regcontrols_read_reverse_vreg(self):
        expected = 120
        actual = self.dss.regcontrols_read_reverse_vreg()
        assert expected == actual

    def test_regcontrols_write_reverse_vreg(self):
        expected = 110
        self.dss.regcontrols_write_reverse_vreg(expected)
        actual = self.dss.regcontrols_read_reverse_vreg()
        assert expected == actual

    # ===================================================================
    # String methods
    # ===================================================================
    def test_regcontrols_read_name(self):
        expected = 'reg1'
        actual = self.dss.regcontrols_read_name()
        assert expected == actual

    def test_regcontrols_write_name(self):
        expected = 'reg2'
        self.dss.regcontrols_write_name(expected)
        actual = self.dss.regcontrols_read_name()
        assert expected == actual

    def test_regcontrols_read_monitored_bus(self):
        expected = ''
        actual = self.dss.regcontrols_read_monitored_bus()
        assert expected == actual

    def test_regcontrols_write_monitored_bus(self):
        # TODO: I don't know how to test this, returning '' for whatever argument
        expected = ''
        self.dss.regcontrols_write_monitored_bus(expected)
        actual = self.dss.regcontrols_read_monitored_bus()
        assert expected == actual

    def test_regcontrols_read_transformer(self):
        expected = 'reg1'
        actual = self.dss.regcontrols_read_transformer()
        assert expected == actual

    def test_regcontrols_write_transformer(self):
        expected = 'reg2'
        self.dss.regcontrols_write_transformer(expected)
        actual = self.dss.regcontrols_read_transformer()
        assert expected == actual

    # ===================================================================
    # Variant methods
    # ===================================================================
    def test_regcontrols_all_names(self):
        expected = ['reg1', 'reg2', 'reg3']
        actual = self.dss.regcontrols_all_names()
        assert expected == actual
