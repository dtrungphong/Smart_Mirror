import sys
from pydub import AudioSegment
from pydub.playback import play
sys.path.insert(1, './mapping_ans_to_speech')
from ans_to_speech import answer_to_speech
# import importlib
k = answer_to_speech('./mapping_ans_to_speech/')
# k = play_sound('./mapping_ans_to_speech/')

list_speech=k.return_ans(['du lịch','y tế'])
# print(list_speech)
# sound = AudioSegment.from_file('./mapping_ans_to_speech/folder_record/key_220.m4a')
# play(sound)
k.play_sound_with_path(list_speech)