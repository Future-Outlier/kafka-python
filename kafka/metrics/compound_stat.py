from __future__ import absolute_import

import abc

from kafka.metrics.stat import AbstractStat
from kafka.vendor.six import add_metaclass


@add_metaclass(abc.ABCMeta)
class AbstractCompoundStat(AbstractStat):
    """
    A compound stat is a stat where a single measurement and associated
    data structure feeds many metrics. This is the example for a
    histogram which has many associated percentiles.
    """
    def stats(self):
        """
        Return list of NamedMeasurable
        """
        raise NotImplementedError


class NamedMeasurable(object):
    __slots__ = ('_name', '_stat')

    def __init__(self, metric_name, measurable_stat):
        self._name = metric_name
        self._stat = measurable_stat

    @property
    def name(self):
        return self._name

    @property
    def stat(self):
        return self._stat
