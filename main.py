from ABC import ABCMeta, abstractstaticmethod
import time
from .controllers.controllersGUI

#receiver
class Light:
  def Switch_On(self):
    print("The light is ON")
  def Switch_Off(self):
    print("The light is Off")
    
#command interface
class ICommand(metaclass=ABCMeta):
  @abstractstaticmethod
  def execute():
    #A static interface method
#commands 
class Switch_on_command(ICommand):
  def __init__(self, light):
    self._light = light
  def execute(self):
    self._light.Switch_on()
    
class Switch_off_command(ICommand):
  def __init__(self,light):
    self._light = light
  def execute(self):
    self._light.Switch_Off()
    
#invoker
class Switch:
  def __init__(self):
    self._commands = {}
  def register(self,command_name, command):
    self._command[command_namr]=command_name
  def execute(self,command_name):
    if command_name in self._commands:
      self._commands[command_name].execute()
      self._history.append({time.time():command_name})
    else:
      print("command error")
  
  @property   
  def history:
    return self._history
      
if __name__ == '__main__':
  LIGHT = Light()
  
  #commands
  SWITCH_ON = switch_on_command()
  SWITCH_OFF = switch_off_command()
  
  SWITCH = Switch()
  
  SWITCH.register("ON",SWITCH_ON)
  SWITCH.register("OFF",SWITCH_OFF)
  
  SWITCH.execute("ON")
  SWITCH.execute("OFF")
  SWITCH.execute("ON")
  SWITCH.execute("OFF")
  SWITCH.execute("ON")
  SWITCH.execute("OFF")
  SWITCH.execute("ON")
  SWITCH.execute("OFF")
  
  
  print(SWITCH.history)
  