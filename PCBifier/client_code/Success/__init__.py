from ._anvil_designer import SuccessTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep


class Success(SuccessTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    sleep(1)
    self.textie.content = "Received Successfully!"
    self.raise_event(self.received())
    
  def received(self, **event_args):
    sleep(1)
    anvil.open_form('ExposureStart')

  