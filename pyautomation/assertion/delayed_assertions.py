"""
Created on Apr 25, 2019
"""

import inspect
import os.path
import allure
from pyautomation.logger.logger import LOG


class Assertions(object):
    """
    Class can be used for delayed assertions
    ----------
    Usage:
        def test():
            assertions = Assertions()
            assertions.expect(a == b, 'a is not equal to b')
            assertions.expect(1 == 1)
            assertions.assert_all() 
    """

    def __init__(self):
        self._failed_expectations = []
        self._cnt = 0

    def expect(self, expr, msg=None):
        """
        delayed assertion 
        
        parameters:
        -----------
            expr: expression to assert
            msg: [None] error message to log
        
        """
        if not expr:
            self._log_failure(msg)

    def assert_all(self):
        """
            Asserts all the conditions and raises AssertionError if any assertion fails
        """
        if self._failed_expectations:
            assert False, self._report_failures()

    def _log_failure(self, msg=None):
        (filename, line, funcname, contextlist) = inspect.stack()[2][1:5]
        filename = os.path.basename(filename)
        context = contextlist[0]
        ALLURE_EXPECT_TMPL = '''{0} : Assertion error occured in file {1} at line no {2}, in test {3}
            {4}
            {5}
        '''
        tmp = ALLURE_EXPECT_TMPL.format(self._cnt + 1, filename, line, funcname, context, msg if msg else '')
        LOG.warning(tmp)
        self._failed_expectations.append(tmp)

    def _report_failures(self):
        if self._failed_expectations:
            _, line, funcname = inspect.stack()[2][1:4]
            HEAD = 'Asserting all expectations: In test {} at line no {}'.format(funcname, line)
            COUNT = 'Failed Expectations:%s' % len(self._failed_expectations)
            LOG.info(HEAD)
            LOG.info(COUNT)
            allure.attach('<p>{0}</p><br><p><b>{1}</b></p>'.format(HEAD, COUNT),
                          'Assertions',
                          allure.attachment_type.HTML)
            AL_F = ''
            for r in self._failed_expectations:
                AL_F += '<p>{0}</p>'.format(r)
            allure.attach(AL_F,
                          '',
                          allure.attachment_type.HTML)
            report = [HEAD,
                      COUNT]
            report.extend(self._failed_expectations)
            self._failed_expectations = []
            LOG.error('\n'.join(report))
