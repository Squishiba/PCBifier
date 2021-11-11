from ._anvil_designer import ExposureStartTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep
from .. import Globals



class ExposureStart(ExposureStartTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.label_1.text = Globals.Expos + " seconds exposure time"
    


  def Exposurebutton1_click(self, **event_args):
    Expos = Globals.Expos
    self.Exposurebutton1.text = "Started Exposure, Please Wait"
    anvil.server.call_s('start_exposure', Expos)
    anvil.open_form('Completed')


      

