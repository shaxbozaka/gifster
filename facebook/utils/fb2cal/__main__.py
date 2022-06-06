#!/usr/bin/env python3

import logging

from .facebook_browser import FacebookBrowser
from .transformer import Transformer


def get_Friends(username=str, pwd=str) -> dict:
    facebook_users = dict({"data": [], "error": False})
    try:
        facebook_browser = FacebookBrowser()

        facebook_browser.authenticate(username, pwd)
        transformer = Transformer()

        # Endpoint will return all birthdays for offset_month plus the following 2 consecutive months.
        # logger.info('Fetching all Birthdays via BirthdayCometRootQuery endpoint...')
        for offset_month in [0, 3, 6, 9]:
            birthday_comet_monthly_json = facebook_browser.query_graph_ql_birthday_comet_monthly(offset_month)
            facebook_users_for_quarter = transformer.transform_birthday_comet_monthly_to_birthdays(birthday_comet_monthly_json)
            # print(facebook_users_for_quarter)
            # facebook_users.update(user for user in facebook_users_for_quarter)
            for x in facebook_users_for_quarter:
                facebook_users['data'].append(x)

        facebook_users['count'] = len(facebook_users['data'])
        if len(facebook_users) == 0:
            # logger.warning(f'Facebook user set is empty. Failed to fetch any birthdays.')
            facebook_users['error'] = {"status": 404,
                                       "desc": "Facebook user set is empty. Failed to fetch any birthdays."}

        return facebook_users
    except SystemExit:
        # logger.critical(f'Critical error encountered. Terminating.')
        facebook_users['error'] = {"status": 500,
                                   "desc": "server error"}
    finally:
        logging.shutdown()
        return facebook_users

