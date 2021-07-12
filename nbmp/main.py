# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

from nbmp.nbs import nbs
from nbmp.play_command import play_command
from podrum.protocol.mcbe.packet.level_sound_event_packet import level_sound_event_packet
from time import sleep

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
        self.server.managers.command_manager.register(play_command(self))
        
    def play_file(self, path: str, player: object) -> None:
        song: object = nbs(path)
        for tick in range(0, song.song_length):
            if tick in song.noteblocks:
                for i, layer in song.noteblocks[tick].items():
                    packet: object = level_sound_event_packet()
                    packet.sound_id = 81
                    packet.position = player.position
                    packet.extra_data = instruments[layer[0]] << 8 | layer[1]
                    packet.entity_type = "minecraft:noteblock"
                    packet.is_baby_mob = False
                    packet.is_global = True
                    packet.encode()
                    player.send_packet(packet.data)
            sleep(1 / (0.05 * song.tempo * 100))
