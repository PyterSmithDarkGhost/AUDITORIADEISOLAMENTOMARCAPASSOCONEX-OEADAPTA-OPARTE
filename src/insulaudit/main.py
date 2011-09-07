#!/usr/bin/python

from cli.log import LoggingApp
from insulaudit import core
from pprint import pprint

"""
Very rough.
"""



from console import Subcommand

class QuxApp(Subcommand):
  """Qux Does several special things"""
  name = "qux"
class FuxApp(Subcommand):
  """Fux is accidently different."""
  name = "fux"
class BuxApp(Subcommand):
  """Bux seems special, but it's a trick."""
  name = "bux"

# core

from console import Command


def get_devices():
  devices = [ ]
  a = Command('AAA', [ FuxApp, QuxApp, BuxApp ] )
  b = Command('BBB', [ FuxApp, QuxApp, BuxApp ] )
  return [ a, b ]

from console.utils import setup_device_options, setup_global_options, GlobalOptions

from console import Application as ConsoleApp

class Application(ConsoleApp):
  name = "insulaudit"

  def setup_commands(self):
    for dev in get_devices():
      self.add_device( dev )
    #self.foo = self.commands.add_parser('device', help="foo help")
    #self.foo.add_argument('comm', help='free form')
  def add_device(self, device):
    self.devices[device.name] = device
    parser = self.commands.add_parser(device.name, help=device.help())
    device.setup(parser)

    

if __name__ == '__main__':
  app = Application()
  app.run( )

#####
# EOF
