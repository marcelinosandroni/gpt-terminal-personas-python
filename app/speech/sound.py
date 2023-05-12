from pydub import AudioSegment, playback
import os


class Sound:
    def play(self, sound):
        playback.play(sound)

    def play_file(self, file_name: str):
        # if type(file_name) != str:
        #     raise TypeError(
        #         f"Invalid file name type, need str, got {type(file_name)}")
        # file_extension = file_name.split('.')[-1]
        # if not file_extension:
        #     raise ValueError(
        #         f"Invalid file name, need file extension, got {file_name}")
        if type(file_name) == list:
            for file in file_name:
                sound_file = AudioSegment.from_file(file_name)
                playback._play_with_ffplay(sound_file)
            return
        sound_file = AudioSegment.from_file(file_name)
        print(playback.get_player_name())
        playback._play_with_ffplay(sound_file)
        #playback._play_with_pyaudio(sound_file)
        #playback._play_with_simpleaudio(sound_file)

        #pcm_data = sound_file
        # Initialize audio player
        #audio_player = simpleaudio.play_buffer(pcm_data, num_channels=2, bytes_per_sample=2, sample_rate=44100)
        # Wait for playback to finish
        #audio_player.wait_done()

        #jprint(pyaudio.PyAudio().get_device_info_by_index(0))
        #print(pyaudio.PyAudio().get_default_output_device_info())
        # audio_player = pyaudio.PyAudio()
        # # Get the index of the default output device
        # default_output_device_index = audio_player.get_default_output_device_info()['index']
        # print("Default output device index:", default_output_device_index)


        # stream = audio_player.open(format=pyaudio.paInt16, channels=2,
        #                         rate=44100, output=True, output_device_index=default_output_device_index)

        # # Play the audio file
        # stream.write(sound_file._data)

        # # Close the audio player and stream
        # stream.stop_stream()
        # stream.close()
        # audio_player.terminate()

        # print(f'Playing {file_name}...')
        # self.play(sound_file)
