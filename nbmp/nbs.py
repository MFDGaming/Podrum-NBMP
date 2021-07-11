# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

from binary_utils.binary_stream import binary_stream

instruments: dict = {
    0: "note.harp",
    1: "note.bass",
    2: "note.bd",
    3: "note.snare",
    4: "note.hat",
    5: "note.guitar",
    6: "note.flute",
    7: "note.bell",
    8: "note.chime",
    9: "note.xylophone"
}

class nbs:
    def __init__(self, path: str) -> None:
        with open(path, "rb") as file:
            self.stream: object = binary_stream(file.read())
        self.load_header()
        self.load_noteblocks()
              
    def load_header(self) -> None:
        self.song_length: int = self.stream.read_short_le()
        self.song_height: int = self.stream.read_short_le()
        self.song_name: str = self.stream.read(self.stream.read_int_le()).decode()
        self.song_author: str = self.stream.read(self.stream.read_int_le()).decode()
        self.original_song_author: str = self.stream.read(self.stream.read_int_le()).decode()
        self.song_description: str = self.stream.read(self.stream.read_int_le()).decode()
        self.tempo: int = self.stream.read_short_le()
        self.auto_saving: int = self.stream.read_bool()
        self.auto_saving_duration: int = self.stream.read_byte()
        self.time_signiture: int = self.stream.read_byte()
        self.minutes_spent: int = self.stream.read_int_le()
        self.left_clicks: int = self.stream.read_int_le()
        self.right_clicks: int = self.stream.read_int_le()
        self.blocks_added: int = self.stream.read_int_le()
        self.blocks_removed: int = self.stream.read_int_le()
        self.midi_or_schematic_file_name: str = self.stream.read(self.stream.read_int_le()).decode()
            
    def load_noteblocks(self) -> None:
        self.noteblocks: dict = {}
        tick: int = -1
        jumps: int = 0
        while True:
            jumps: int = self.stream.read_short_le()
            if jumps == 0:
                break;
            tick += jumps
            layer: int = -1
            while True:
                jumps: int = self.stream.read_short_le()
                if jumps == 0:
                    break;
                layer += jumps
                instrument: str = instruments[self.stream.read_byte()]
                pitch: int = self.stream.read_byte()
                if tick not in self.noteblocks:
                    self.noteblocks[tick] = {layer: (instrument, pitch)}
                else:
                    self.noteblocks[tick][layer] = (instrument, pitch)
