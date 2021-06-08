from midi_parser_pipelines.pipeline import Pipeline
from midi_parser_pipelines.mido_transformers import *
from midi_parser_pipelines.music_generation import *
from midi_parser_pipelines.tokenizers import *
from midi_parser_pipelines.parsers import *
from midi_parser_pipelines.utils import *
import os
import pickle

from unittest import TestCase
from itertools import chain


testdir = os.environ["MIDI"]+"\\JSB Chorales\\JSB Chorales\\train"

class TestPipeline(TestCase):


    def test_on_off_pipeline(self):


        pipeline = Pipeline([
            Parser(True),
            KeyShiftAdder(),
            TrackChooser([0]),
            NoteRangeConverter((46,84)),
            TimeNormalizer(1/64),
            OnOffTokenizer("test/test_data/on_off_tokenizer_results")
        ])

        pipeline.apply(testdir)



    def test_load(self):

        f = open("test/test_data/on_off_tokenizer_results.pickle", "rb")
        pieces = pickle.load(f)
        f.close()
        print(len(pieces))
        print(len(set(chain.from_iterable(pieces))))

    def test_to_mido(self):
        f = open("test/test_data/on_off_tokenizer_results.pickle", "rb")
        pieces = pickle.load(f)
        f.close()
        mido = tokenizedOnOffToMido(pieces[1])
        playMido(mido, 1/64)



