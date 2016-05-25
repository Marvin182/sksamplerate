from ._samplerate import resample, available_convertors, src_version_str, convertor_description
from .version import __version__

from numpy.testing import Tester

test = Tester().test
bench = Tester().bench

