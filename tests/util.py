from unittest import mock as utm

from tornado import ioloop as ti, gen as tg


class AsyncMock(utm.Mock):

    def __init__(self, return_value=None, delay=None):
        super(AsyncMock, self).__init__(return_value=self)

        self._return_value = return_value
        self._awaited = False
        self._delay = 0.25 if delay is None else delay

    def __await__(self):
        yield tg.sleep(self._delay)
        self._awaited = True
        return self._return_value

    def assert_awaited(self):
        assert self._awaited
