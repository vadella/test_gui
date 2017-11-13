from video_library import video_info  # import VideoStreamInfo, StreamInfo, AudioStreamInfo, SubtitleStreamInfo, MkvFile
import typing


class LibraryMkvFile(video_info.MkvFile):
    def __init__(self, filename):
        video_info.MkvFile.__init__(self, filename)

    @property
    def resolution(self):
        return self.video[0].resolution

    @property
    def audio_num(self):
        return len(self.audio)

    @property
    def audio_lang(self):
        return ', '.join(i.lang for i in self.audio)

    @property
    def sub_num(self):
        return len(self.subtitle)

    @property
    def sub_lang(self):
        return ', '.join(i.lang for i in self.subtitle)

    @property
    def summary(self):
        return self.filename.name, self.resolution, self.audio_num, self.audio_lang, self.sub_num, self.sub_lang

    @classmethod
    def summary_labels(cls):
        return 'name', 'resolution', 'audio_num', 'audio_lang', 'sub_num', 'sub_lang'


class VideoLibrary:
    def __init__(self, files):
        self._info = [LibraryMkvFile(file) for file in files] if files else []

    def __len__(self):
        return len(self._info)

    @property
    def filenames(self):
        return (info.filename.name for info in self._info)

    @property
    def stream_info(self):
        return [info.summary for info in self._info]

    @property
    def stream_strings(self):
        return [', '.join(str(i) for i in info) for info in self.stream_info]

    @property
    def header(self):
        return LibraryMkvFile.summary_labels()

    @property
    def data(self):
        return [i for i in self.stream_info]

    def __repr__(self):
        return str(self.stream_info)
