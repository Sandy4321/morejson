"""Testing the dumps and loads functionality."""

import unittest

import sys
import datetime
import json

import morejson


__author__ = "Shay Palachy"
__copyright__ = "Shay Palachy"
__license__ = "MIT"


class TestDumps(unittest.TestCase):
    """Testing the dumps and loads functionality."""

    def test_regular_dumps(self):
        """Testing dumps and loads of regular types."""
        dicti = {
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, json.loads(morejson.dumps(dicti)))

    def test_dumps_date(self):
        """Testing dumps and loads of date types."""
        dicti = {
            'date': datetime.date.today(),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_time(self):
        """Testing dumps and loads of time types."""
        dicti = {
            'mintime': datetime.time.min,
            'maxtime': datetime.time.max,
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_datetime(self):
        """Testing dumps and loads of datetime types."""
        dicti = {
            'datetime': datetime.datetime.now(),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_timedelta(self):
        """Testing dumps and loads of timedelta types."""
        dicti = {
            'timedelta1': datetime.timedelta(days=392),
            'timedelta2': datetime.timedelta(weeks=2, hours=23),
            'timedelta3': datetime.timedelta(microseconds=27836),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    @unittest.skipIf(sys.version_info < (3, 0), "not supported in Python2")
    def test_dumps_timezone(self):
        """Testing dumps and loads of timezone types."""
        dicti = {
            'utc_timezone': datetime.timezone.utc,
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_datetime_with_zone(self):
        """Testing dumps and loads of timezone-aware datetime types, as well as standalone 
        timezone objects """

        try:
            import pytz
            import tzlocal
        except ImportError:
            # These packages aren't available - can't test
            raise unittest.SkipTest(
                "pytz or tzlocal not available in this test run; skipping zone-aware DT tests.")

        local_tz = tzlocal.get_localzone()
        pytz_est = pytz.timezone("US/Eastern")
        pytz_pst = pytz.timezone("US/Pacific")
        pytz_utc = pytz.timezone("UTC")
        pytz_fixed = pytz.FixedOffset(-120)

        original_allow_pickle = morejson.CONFIG.get("allow_pickle", False)
        morejson.CONFIG["allow_pickle"] = True

        dicti = {
            'datetime-no-tz': datetime.datetime.now(),
            'datetime-with-utc': datetime.datetime.now(tz=pytz_utc),
            'datetime-with-est': datetime.datetime.now(tz=pytz_est),
            'datetime-with-tzlocal': datetime.datetime.now(tz=local_tz),
            'datetime-with-pst': datetime.datetime.now(tz=pytz_pst),
            'datetime-with-fixedoffset': datetime.datetime.now(tz=pytz_fixed),
            'eastern-tzone': pytz_est,
            'pacific-tzone': pytz_pst,
            'array': [1, 2, 3, pytz_utc, pytz_est, local_tz, pytz_pst, pytz_fixed],
            'string': 'trololo',
            'null': None
        }
        out_str = morejson.dumps(dicti)
        actual_obj = morejson.loads(out_str)
        self.assertEqual(dicti, actual_obj)
        morejson.CONFIG["allow_pickle"] = original_allow_pickle

    @unittest.skipIf(sys.version_info < (3, 0), "not supported in Python2")
    def test_dumps_datetime_with_custom_zones(self):
        """
        Testing dumps and loads of timezone-aware datetime types, with custom defined (fixed offset from UTC) zones.
        This uses the `datetime.timezone` class which is not available on Python 2.7, so we skip it there.
        """

        custom_tz = datetime.timezone(datetime.timedelta(hours=-8, minutes=-30))
        UTC = datetime.timezone.utc

        original_allow_pickle = morejson.CONFIG.get("allow_pickle", False)
        morejson.CONFIG["allow_pickle"] = True

        dicti = {
            'datetime-no-tz': datetime.datetime.now(),
            'datetime-with-utc': datetime.datetime.now(tz=UTC),
            'datetime-with-tz-plain': datetime.datetime.now(tz=custom_tz),
            'custom-tzone': custom_tz,
            'array': [1, 2, 3, UTC, custom_tz],
            'string': 'trololo',
            'null': None
        }
        out_str = morejson.dumps(dicti)
        actual_obj = morejson.loads(out_str)
        self.assertEqual(dicti, actual_obj)
        morejson.CONFIG["allow_pickle"] = original_allow_pickle

    def test_dumps_set(self):
        """Testing dumps and loads of set types."""
        dicti = {
            'set': set([1, 2, 4, 4, 2]),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_frozenset(self):
        """Testing dumps and loads of frozenset types."""
        dicti = {
            'frozenset': frozenset([1, 2, 4, 4, 2]),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))

    def test_dumps_complex(self):
        """Testing dumps and loads of complex types."""
        dicti = {
            'complex1': complex(1, 34.2),
            'complex2': complex(-98.213, 91823),
            'array': [1, 2, 3],
            'string': 'trololo',
            'int': 1,
            'float': 4.32,
            'true': True,
            'false': False,
            'null': None
        }
        self.assertEqual(dicti, morejson.loads(morejson.dumps(dicti)))


    # testing problmem handling and corner cases

    def test_dumps_unsupported(self):
        """Testing dumps of unsupported types."""
        dicti = {
            'lambda': lambda a: a+1
        }
        with self.assertRaises(TypeError):
            morejson.dumps(dicti)

    def test_loads_bad_datetime_arg(self):
        """Testing dumps of unsupported types."""
        dicti = {
            "release_day": 2,
            "closing_date": {
                "month": 10,
                "year": 2013,
                "day": 18,
                "__type__": "datetime.date"
            }
        }
        morejson.loads(morejson.dumps(dicti))

    class _Monkey(object):
        def __init__(self, name, bananas):
            self.name = name
            self.bananas = bananas
        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return (self.name == other.name) and (
                    self.bananas == other.bananas)
            else:
                return False

    @staticmethod
    def _monkey_default_encoder(obj): # pylint: disable=E0202
        if isinstance(obj, TestDumps._Monkey):
            return {
                "_custom_type_": "monkey",
                "name": obj.name,
                "bananas": obj.bananas
            }
        else:
            raise TypeError("Type {} is not JSON encodable.".format(type(obj)))

    @staticmethod
    def _monkey_object_hook(dict_obj):
        if "_custom_type_" not in dict_obj:
            return dict_obj
        if dict_obj["_custom_type_"] == "monkey":
            return TestDumps._Monkey(
                dict_obj['name'], dict_obj['bananas'])
        else:
            return dict_obj

    def test_dump_monkey(self):
        """Testing dumps of monkey types."""
        johnny = TestDumps._Monkey("Johnny", 54)
        dicti = {"my_pet": johnny}
        self.assertEqual(dicti, morejson.loads(
            morejson.dumps(dicti, default=TestDumps._monkey_default_encoder),
            object_hook=TestDumps._monkey_object_hook))

    def test_custom_default_backoff(self):
        """Testing custom default backoff."""
        dicti = {"now": datetime.datetime.now()}
        self.assertEqual(dicti, morejson.loads(
            morejson.dumps(dicti, default=TestDumps._monkey_default_encoder),
            object_hook=TestDumps._monkey_object_hook))
