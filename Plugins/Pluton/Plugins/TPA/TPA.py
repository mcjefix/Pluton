import clr
import sys
clr.AddReferenceByPartialName("UnityEngine")
clr.AddReferenceByPartialName("Pluton")
import UnityEngine
from UnityEngine import *
import Pluton


class TPA:
    def On_Command(self, command):
        if command.cmd == "tpa":
            if len(command.args) == 0:
                command.User.Message('usage: /tpa [playername]')
                return
            else:
                name = command.quotedArgs[0]
                StringName = Server.FindPlayer(name).ToString()
                if StringName is not None or StringName is not False:
                    NonString = Server.FindPlayer(name)
                    PYID = NonString.SteamID
                    DataStore.Add("TeleportRequest", PYID, command.User.Name)
                    NonString.Message(command.User.Name + " would like to teleport to you")
                    NonString.Message("use /tpaccept to accept")
                    command.User.Message("Request sent")
                else:
                    command.User.Message("Player Not Found!")
        elif command.cmd == "tpaccept":
            if DataStore.Get("TeleportRequest", command.User.SteamID):
                name = DataStore.Get("TeleportRequest", command.User.SteamID)
                StringName = name.ToString()
                NonString = Server.FindPlayer(name)
                if StringName is not None or StringName is not False:
                    command.User.Message("Teleport Accepted")
                    NonString.Message("Teleporting to: " + command.User.Name)
                    NonString.Teleport(command.User.Location)
                else:
                    command.User.Message("user went offline or no pending requests")
                    DataStore.Remove("TeleportRequest", command.User.SteamID)
            else:
                command.User.Message("no pending requests")

        elif command.cmd == "tp sat":
        	command.User.Teleport(2567,300,37)