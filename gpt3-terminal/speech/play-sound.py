from pydub import AudioSegment, playback


class Sound:
    def play(self, sound):
        playback.play(sound)

    def play_file(self, file_name: str):
        if type(file_name) != str:
            raise TypeError(
                f"Invalid file name type, need str, got {type(file_name)}")
        file_extension = file_name.split('.')[-1]
        if not file_extension:
            raise ValueError(
                f"Invalid file name, need file extension, got {file_name}")
        sound_file = AudioSegment.from_file(file_name)
        self.play(sound_file)
