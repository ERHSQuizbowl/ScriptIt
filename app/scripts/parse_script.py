import requests
from requests import Session, Request
from scriptit.settings import MEDIA_ROOT
from docx import Document


class ScriptLine:
    def __init__(self, line):
        self.line = line

        # @property
        # def text_to_speech(self):
        #     token = requests.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers={'Content-Length': '0',
        #                                                                                               'Ocp-Apim-Subscription-Key': '063e5fc5034c455ba0937756d2894caf'}).content
        #     url = 'https://speech.platform.bing.com/synthesize'
        #     headers = {'Content-Length': str(len(self.line)), 'Content-Type': 'application/ssml+xml',
        #                'Authorization': 'Bearer ' + token,
        #                'X-Microsoft-OutputFormat': 'audio-16khz-32kbitrate-mono-mp3',
        #                'User-Agent': 'scripit'}
        #
        #     data = '<speak version=\"1.0\" xml:lang=\"en-US\"><voice xml:lang=\"en-US\" xml:gender=\"Female\" name=\"Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)\">' + self.line + '</voice></speak>'
        #     req = Request('POST', url=url, headers=headers, data=data)
        #     s = Session()
        #     res = s.send(req.prepare())
        #     return res.content
        # encoded mp3 file
        # file = open(MEDIA_ROOT + '/sound.mp3', 'w')
        # file.write(res.content)

    # fill in
    @property
    def speaker(self):
        return "Vinai"


class ParseScript:
    def __init__(self, file):
        self.file = file
        self.open_file = None
        self.lines = []
        self.othersLines = []
        self.counter = 0

    def open(self):
        of = open(self.file)
        self.open_file = of.read()
        for line in self.open_file:
            self.lines.append(ScriptLine(line))

    def text_to_speech(self, input):
        token = requests.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers={'Content-Length': '0',
                                                                                                  'Ocp-Apim-Subscription-Key': '063e5fc5034c455ba0937756d2894caf'}).content
        url = 'https://speech.platform.bing.com/synthesize'
        headers = {'Content-Length': str(len(input)), 'Content-Type': 'application/ssml+xml',
                   'Authorization': 'Bearer ' + token,
                   'X-Microsoft-OutputFormat': 'audio-16khz-32kbitrate-mono-mp3',
                   'User-Agent': 'scripit'}

        data = '<speak version=\"1.0\" xml:lang=\"en-US\"><voice xml:lang=\"en-US\" xml:gender=\"Female\" name=\"Microsoft Server Speech Text to Speech Voice (en-US, ZiraRUS)\">' + input + '</voice></speak>'
        req = Request('POST', url=url, headers=headers, data=data)
        s = Session()
        res = s.send(req.prepare())
        file = open(MEDIA_ROOT + '/sound.mp3', 'w')
        file.write(res.content)

    # parse the file and say every line except the name
    def parse(self, name):
        (a, b) = self.parse_text(self.file, name)
        self.lines = a
        self.othersLines = b

    """
    Function takes an input file and scraps the text
    """

    def parse_text(self, input_file, role):
        """
        Word doc File Inputs
        """
        if input_file.endswith('.docx'):
            print "this is a Word document"
            document = Document(input_file)
            document.save('test.docx')  # we can now access the doc file in python

            content = []
            my_part = []
            other_parts = []

            for para in document.paragraphs:  # parses paragraphs
                text = para.text.encode('ascii', 'ignore')
                content.append(text)

            val = 0  # counter

            while val < len(content):
                if content[val] == role:
                    my_part.append(content[val + 1])
                    val += 2
                else:
                    other_parts.append(content[val + 1])
                    val += 2
            return (my_part, other_parts)

        else:
            print "Error: Input a valid Word Docx"

        """
        Function detects errors and returns a list of indexes of words said incorrectly
        """

    def detect_errors(self, my_part, speech_input):
        # remove all punctuation in my_part of the scene and transcribed speech
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        my_part = my_part.translate(None, punctuation)
        my_part_list = my_part.split()

        #  speech_input_list = speech_input_list.translate(None, punctuation)
        speech_input_list = speech_input.split()

        # compare your part of speech with generated text from speech as you practise
        count = 0
        toggle_list = []
        for p in my_part_list:

            if p != speech_input_list[count]:
                toggle_list.append(count)

            count += 1
        return toggle_list  # returns list of indices of words gotten wrong

    def get_next_line(self):
        if self.counter == len(self.lines):
            return None

        to_ret = self.lines[self.counter]
        self.counter = self.counter + 1
        return to_ret

    def get_all_lines(self):
        return self.lines
