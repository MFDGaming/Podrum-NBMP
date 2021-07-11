# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

from nbmp.nbs import nbs
from podrum.protocol.mcbe.packet.level_sound_event_packet import level_sound_event_packet
import time

instruments: dict = {
    "note.harp": 0,
    "note.bd": 1,
    "note.snare": 2,
    "note.hat": 3,
    "note.bass": 4,
    "note.bell": 5,
    "note.flute": 6,
    "note.chime": 7,
    "note.guitar": 8,
    "note.xylophone": 9,
    "note.iron_xylophone": 10,
    "note.cow_bell": 11,
    "note.didgeridoo": 12,
    "note.bit": 13,
    "note.banjo": 14,
    "note.pling": 15,
    "note.bassattack": 16
}

class main:
    def on_load(self) -> None:
        self.server.logger.info("Loaded NBMP :)")
        
    def play_file(path: str, player: object) -> None:
        song: object = nbs(path)
        for i in range(0, song.song_length):
            if i in song.noteblocks:
                packet: object = level_sound_event_packet()
                packet.sound_id
            sleep(1 / (0.05 * song.tempo * 100))
