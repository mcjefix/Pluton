import clr
clr.AddReferenceByPartialName("Pluton")
import Pluton
from System import String

class Kits:
  def On_Command(self, command):
  	if command.cmd == 'starter':
  		command.User.Inventory.Add(11983)
  		command.User.Inventory.Add(14086)
  		command.User.Inventory.Add(14086)
  		command.User.Inventory.Add(14086)
  		command.User.Inventory.Add(14086)
  		command.User.Inventory.Add(11950, 3)

  	if command.cmd == 'resources':
  		command.User.Inventory.Add(514, 500)
  		command.User.Inventory.Add(11964, 250)

  	if command.cmd == 'suicide':
  		command.User.Kill()


