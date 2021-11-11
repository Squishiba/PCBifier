from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from time import sleep
from .. import Globals



class Upload(UploadTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.upload.enabled = False
    self.cancelbutton.enabled = False


  def ImageLoad_change(self, file, **event_args):
    self.ImageLoad.show_state = True
    self.upload.enabled = True
    self.image_1.source = file  
    self.cancelbutton.enabled = True
    
  
  def Upload_click(self, **event_args):
    file = self.ImageLoad.file
    global Expos
    Globals.Expos = self.exposuredrop.selected_value
    anvil.server.call('get_Images', file)
    sleep(1)
    anvil.open_form('ExposureStart')
    
        
  def cancel_click(self, **event_args):
    self.ImageLoad.clear()
    file_contents = "Hello, world".encode()
    self.image_1.source = BlobMedia("Image", content=file_contents )
    pass 

    
    
    
    
        
    
    
    
    
    

    
    


  






