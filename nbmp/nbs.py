# Copyright Alexander Argentakis (MFDGaming).
# This file is licensed under the GPLv2 license.

from binary_utils.binary_stream import binary_stream

class nbs:
    def __init__(self, path: str) -> None:
        with open(path, "rb") as file:
            self.stream: object = binary_stream(file.read())
        self.load_header()
              
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
