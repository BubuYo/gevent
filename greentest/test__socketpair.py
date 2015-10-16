from gevent import monkey; monkey.patch_all()
import socket
import unittest


class TestSocketpair(unittest.TestCase):

    def test_makefile(self):
        msg = b'hello world'
        x, y = socket.socketpair()
        x.sendall(msg)
        x.close()
        read = y.makefile('rb').read()
        self.assertEqual(msg, read)

    def test_fromfd(self):
        msg = b'hello world'
        x, y = socket.socketpair()
        xx = socket.fromfd(x.fileno(), x.family, socket.SOCK_STREAM)
        x.close()
        yy = socket.fromfd(y.fileno(), y.family, socket.SOCK_STREAM)
        y.close()

        xx.sendall(msg)
        xx.close()
        read = yy.makefile('rb').read()
        self.assertEqual(msg, read)


if __name__ == '__main__':
    unittest.main()
