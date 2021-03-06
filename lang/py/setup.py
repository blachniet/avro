#!/usr/bin/env python

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
# 
# https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import setuptools


def _get_version():
  curdir = os.getcwd()
  version_file = ("VERSION.txt" if os.path.isfile("VERSION.txt")
    else os.path.join(curdir[:curdir.index("lang/py")], "share/VERSION.txt"))
  with open(version_file) as verfile:
    # To follow the naming convention defined by PEP 440
    # in the case that the version is like "x.y.z-SNAPSHOT"
    return verfile.read().rstrip().replace("-", "+")


setuptools.setup(
  name = 'avro',
  version = _get_version(),
  packages = ['avro'],
  package_dir = {'': 'src'},
  scripts = ["./scripts/avro"],

  #include_package_data=True,
  package_data={'avro': ['LICENSE', 'NOTICE']},

  # metadata for upload to PyPI
  author = 'Apache Avro',
  author_email = 'dev@avro.apache.org',
  description = 'Avro is a serialization and RPC framework.',
  license = 'Apache License 2.0',
  keywords = 'avro serialization rpc',
  url = 'https://avro.apache.org/',
  extras_require = {
    'snappy': ['python-snappy'],
  },
)
