import pandas as pd
import numpy as np
import sys
from pydub import AudioSegment
from pydub.playback import play


class answer_to_speech:
    def __init__(self,dir):
        sys.path.insert(1, dir+ 'mapping_folder')   ### đường dẫn gọi đến  file mapping key

        file_r1 = pd.read_csv(dir+'key_speech.csv').to_numpy()
        self.key_speech = {}
        self.name_speech = []
        for w in file_r1:
            self.name_speech.append(w[0])
            self.key_speech[w[0]]=w[1]
        self.dir = dir
 
    def return_speech(self,ans_room): ### trả về danh sách đường dẫn của câu trả lời
        list_speech=[]
        for ans in ans_room:
            if ans==[""]:
                list_speech.append([self.dir+'folder_record/'+self.key_speech["không hiểu"]])
                continue
            list_ = []
            for word in ans:
                print(word)
                list_.append(self.dir+'folder_record/'+self.key_speech[word])
            list_speech.append(list_)
        return list_speech

    def play_sound_from_ans_room(self,ans_room): ### phát file âm thanh từ danh sách câu trả lời
        list_speech = self.return_speech(ans_room)
        for sentences in list_speech:
            sound = None
            for file_sound in sentences:
                if (sound==None):
                    sound = AudioSegment.from_file(file_sound, format="m4a")
                    continue
                sound += AudioSegment.from_file(file_sound, format="m4a")
            play(sound)
        return list_speech

    def play_sound_with_path(self,path_): ### phát file âm thanh từ danh sách đường dẫn
        for sentences in path_:
            sound = None
            for file_sound in sentences:
                if (sound==None):
                    sound = AudioSegment.from_file(file_sound)
                    continue
                sound += AudioSegment.from_file(file_sound)
            play(sound)

    def return_ans(self, key_):
        ### trả về danh sách đường dẫn từ key
        ### đầu vào là key để nhận diện
        ### đầu ra là đường dẫn đến câu trả lời của key đó
        from mapping_key import mapping
        x = mapping()
        ans_room = x.return_key(key_)
        list_file_sound = self.return_speech(ans_room)
        return list_file_sound