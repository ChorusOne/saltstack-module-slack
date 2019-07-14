# -*- coding: utf-8 -*-
'''
Provide authentication using a Slack token

Slack auth can be defined like any other eauth module:

.. code-block:: yaml

    external_auth:
      slack:
        fred:
          - .*
          - '@runner'

'''

# Import python libs
from __future__ import absolute_import, print_function, unicode_literals
import logging

# Import salt libs
import salt.utils.http

log = logging.getLogger(__name__)

__virtualname__ = 'slack'


def __virtual__():
    return __virtualname__


def auth(username, password):
    '''
    Slack authentication
    '''

    url = https://slack.com/api/auth.test?token={}'.format(self.password)

    # Post to the API endpoint. If 200 is returned then the result will be the ACLs
    # for this user
    result = salt.utils.http.query(url, method='POST', status=True, decode=True)
    if result['status'] == 200:
        log.debug('eauth REST call returned 200: %s', result)
        if result['dict'] is not None:
            if result['dict']['ok'] == False:
		log.debug('eauth Slack call failed (reject by server): %s', result)
        	return False
            if result['dict']['user'] != username:
                log.debug('eauth Slack call failed (user mismatch): %s', result)
                return False
        return True
    else:
        log.debug('eauth Slack call failed (non-200 response): %s', result)
        return False
