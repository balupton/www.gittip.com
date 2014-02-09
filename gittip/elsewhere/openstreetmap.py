from __future__ import absolute_import, division, print_function, unicode_literals

from gittip.elsewhere import PlatformOAuth1, not_available, xpath


class OpenStreetMap(PlatformOAuth1):

    # Platform attributes
    name = 'openstreetmap'
    display_name = 'OpenStreetMap'
    account_url = 'http://www.openstreetmap.org/user/{user_name}'
    icon = '/assets/icons/openstreetmap.12.png'

    # API attributes
    api_format = 'xml'
    api_user_info_path = '/user/{user_name}'
    api_user_self_info_path = '/user/details'
    x_user_id = xpath('./user', attr='id')
    x_user_name = xpath('./user', attr='display_name')
    x_display_name = x_user_name
    x_email = not_available
    x_avatar_url = xpath('./user/img', attr='href')
