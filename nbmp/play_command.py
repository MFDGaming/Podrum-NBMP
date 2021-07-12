# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

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
                immediate_task(self.plugin.play_file, [" ".join(args), sender]).start()
            else:
                sender.send_message("/play {file}")
