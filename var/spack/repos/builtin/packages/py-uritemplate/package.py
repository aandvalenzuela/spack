# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyUritemplate(PythonPackage):
    """Simple python library to deal with URI Templates."""

    homepage = "https://uritemplate.readthedocs.org/"
    pypi = "uritemplate/uritemplate-3.0.0.tar.gz"

    version('3.0.0', sha256='c02643cebe23fc8adb5e6becffe201185bf06c40bda5c0b4028a93f1527d011d')

    depends_on('py-setuptools', type='build')
