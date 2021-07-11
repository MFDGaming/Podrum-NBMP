#########################################################
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################

from podrum.task.immediate_task import immediate_task

class play_command:
    def __init__(self, plugin: object) -> None:
        self.plugin: object = plugin
        self.name: str = "play"
        self.description: str = "Plays a .nbs file."
    
    def execute(self, args: list, sender: object) -> None:
        if sender != self.plugin.server:
            if len(args) >= 1:
                sender.send_message(f"Playing file")
                immediate_task(self.plugin.play_file, [args[0], sender]).start()
            else:
                sender.send_message("/play {file}")
