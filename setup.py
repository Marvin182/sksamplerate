#!/usr/bin/env python
descr   = """\
Samplerate is a small python package to do high quality audio resampling for
data in numpy arrays; IOW, it is a matlab resample replacement.

Samplerate is a wrapper around the Secret Rabbit Code from Erik de Castro Lopo
(http://www.mega-nerd.com/SRC/), which has high quality converters based on the
work of J.O Smith from CCRMA (see
http://ccrma.stanford.edu/~jos/resample/optfir.pdf)
"""

DISTNAME            = 'sksamplerate'
DESCRIPTION         = 'A python module for high quality audio resampling'
LONG_DESCRIPTION    = descr
MAINTAINER          = 'David Cournapeau'
MAINTAINER_EMAIL    = 'david@ar.media.kyoto-u.ac.jp'
URL                 = 'http://www.ar.media.kyoto-u.ac.jp/members/david/softwares/samplerate'
LICENSE             = 'GPL'
DOWNLOAD_URL        = 'http://pypi.python.org/pypi/scikits.samplerate'
PACKAGE_NAME        = 'sksamplerate'
EXTRA_INFO          = dict(
    install_requires=['numpy'],
    classifiers     = ['Development Status :: 4 - Beta',
                       'Environment :: Console',
                       'Intended Audience :: Developers',
                       'Intended Audience :: Science/Research',
                       'License :: OSI Approved :: GNU General Public License (GPL)',
                       'Topic :: Multimedia :: Sound/Audio',
                       'Topic :: Scientific/Engineering']
)

import os
import sys
import subprocess

import setuptools
from numpy.distutils.core import setup

def configuration(parent_package='', top_path=None, package_name=DISTNAME):
    if os.path.exists('MANIFEST'): os.remove('MANIFEST')

    from numpy.distutils.misc_util import Configuration
    config = Configuration(None, parent_package, top_path)

    # Avoid non-useful msg: "Ignoring attempt to set 'name' (from ... "
    config.set_options(ignore_setup_xxx_py=True,
                       assume_default_configuration=True,
                       delegate_options_to_subpackages=True,
                       quiet=True)

    config.add_subpackage(PACKAGE_NAME)
    return config

def get_version():
    """Obtain the version number"""
    import imp
    mod = imp.load_source('version', os.path.join(PACKAGE_NAME, 'version.py'))
    return mod.__version__

# Documentation building command
try:
    from sphinx.setup_command import BuildDoc as SphinxBuildDoc
    class BuildDoc(SphinxBuildDoc):
        """Run in-place build before Sphinx doc build"""
        def run(self):
            ret = subprocess.call([sys.executable, sys.argv[0], 'build_ext', '-i'])
            if ret != 0:
                raise RuntimeError("Building Scipy failed!")
            SphinxBuildDoc.run(self)
    cmdclass = {'build_sphinx': BuildDoc}
except ImportError:
    cmdclass = {}

# Call the setup function
if __name__ == "__main__":
    setup(configuration=configuration,
          name=DISTNAME,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          license=LICENSE,
          url=URL,
          download_url=DOWNLOAD_URL,
          long_description=LONG_DESCRIPTION,
          include_package_data=True,
          test_suite="nose.collector",
          cmdclass=cmdclass,
          version=get_version(),
          **EXTRA_INFO)
