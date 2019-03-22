#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: "Chris Ward" <cward@redhat.com>




def test_load():
    from did.plugins import load
    assert load


def test_detect():
    from did.plugins import detect
    assert detect
