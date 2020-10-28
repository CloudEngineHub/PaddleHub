# coding:utf-8
# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import shutil


def _get_user_home():
    return os.path.expanduser('~')


def _get_hub_home():
    if 'HUB_HOME' in os.environ:
        home_path = os.environ['HUB_HOME']
        if os.path.exists(home_path):
            if os.path.isdir(home_path):
                return home_path
            else:
                raise RuntimeError('The environment variable HUB_HOME {} is not a directory.'.format(home_path))
        else:
            return home_path
    return os.path.join(_get_user_home(), '.paddlehub')


def _get_sub_home(directory):
    home = os.path.join(_get_hub_home(), directory)
    if not os.path.exists(home):
        os.makedirs(home)
    return home


USER_HOME = _get_user_home()
HUB_HOME = _get_hub_home()
MODULE_HOME = _get_sub_home('modules')
CACHE_HOME = _get_sub_home('cache')
DATA_HOME = _get_sub_home('dataset')
CONF_HOME = _get_sub_home('conf')
THIRD_PARTY_HOME = _get_sub_home('thirdparty')
TMP_HOME = _get_sub_home('tmp')
SOURCES_HOME = _get_sub_home('sources')
LOG_HOME = _get_sub_home('log')
