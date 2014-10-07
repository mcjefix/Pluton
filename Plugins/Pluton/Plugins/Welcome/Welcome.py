import clr
clr.AddReferenceByPartialName("Pluton")
import Pluton
from System import String

class Welcome:
  def On_PlayerConnected(self, player):
    Server.Broadcast(player.Name + " has joined the server!")
    player.Message(String.Format("This server is working with Pluton[{0}]", Pluton.Bootstrap.Version))
    player.Message("Type /help for a list of commands")
    player.Inventory.Add(6604,40)
    player.Inventory.Add(11963, 1)


