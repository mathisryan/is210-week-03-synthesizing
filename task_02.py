#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

ORIG = 'Spanish'
SUB = 'Flemish'
SIZE = len(ORIG)
TEXT = inquisition.SPANISH
WHERE = TEXT.find(ORIG)

FLEMISH = TEXT[:WHERE] + 'Flemish' + TEXT[WHERE + SIZE:]
