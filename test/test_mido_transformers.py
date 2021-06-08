from midi_parser_pipelines.utils import parseToMidos
from unittest import TestCase
from unittest.suite import TestSuite
from midi_parser_pipelines.mido_transformers import TrackChooser
from midi_parser_pipelines.utils import findMidis, parseToMidos
from midi_parser_pipelines.mido_transformers import *
import os


def getMidos():
    paths = os.environ["MIDI"]+"\\maestro_small"
    midis = findMidis(paths)
    midos = parseToMidos(midis)
    return midos

class TestTrackChooser(TestCase):

    def test_choose_one(self):
        midos = getMidos()
        trackChooser = TrackChooser([0])
        result = trackChooser.apply(midos)
        for midi in result:
            self.assertEqual(len(midi.tracks), 1)
        
    def test_choose_two(self):
        midos = getMidos()
        trackChooser = TrackChooser([0, 1])
        result = trackChooser.apply(midos)
        for midi in result:
            self.assertEqual(len(midi.tracks), 2)


class TestTimeNormalizer(TestCase):


    def test_normalize(self):

        midos = getMidos()
        timeNormalizer = TimeNormalizer(1/64)
        result = timeNormalizer.apply(midos)
        for mido in result:
            for track in mido.tracks:
                for msg in track:
                    pass






