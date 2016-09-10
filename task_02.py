#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

STR = 'Spanish'

STR_LEN = len(STR)

START_PT = inquisition.SPANISH.index('Spanish')

FIRST_PART = inquisition.SPANISH[:START_PT]

SECOND_PART = inquisition.SPANISH[START_PT+STR_LEN:]

FLEMISH = FIRST_PART + 'Flemish' + SECOND_PART
