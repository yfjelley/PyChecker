# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

'''
Tests related to pychecker.CodeChecks
'''

import unittest
import common

from pychecker import CodeChecks

class DispatchTestCase(common.TestCase):
    '''
    Test that we have all opcodes in the DISPATCH array.
    '''
    def testDispatch(self):
        if not common.canImport('dis'):
            # FIXME: no skip support
            return

        res = []
        import dis
        for key, value in dis.opmap.items():
            if not CodeChecks.DISPATCH[value]:
                res.append("opcode %d: %s not in CodeChecks.DISPATCH" % (
                    value, key))
        self.failIf(res, "\n".join(res))
