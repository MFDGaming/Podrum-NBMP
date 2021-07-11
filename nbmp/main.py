# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

from nbmp.nbs import nbs
from podrum.protocol.mcbe.packet.level_sound_event_packet import level_sound_event_packet
import time

class main:
    def on_load(self) -> None:
        self.server.logger.info("Loaded NBMP :)")
        
    def play_file(path: str, player: object) -> None:
        song: object = nbs(path)
        for i in range(0, song.song_length):
            if i in song.noteblocks:
                pass # Sned the packet
            sleep(1 / (0.05 * song.tempo * 100))
