from ._anvil_designer import CompletedTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep


class Completed(CompletedTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def returnhome_click(self, **event_args):
    anvil.open_form('Upload')
    pass

