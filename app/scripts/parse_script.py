import requests
from requests import Session, Request
from scriptit.settings import MEDIA_ROOT


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
        input_file = open(self.file)
        self.text_to_speech(input_file.read())

    def get_next_line(self):
        if self.counter == len(self.lines):
            return None

        to_ret = self.lines[self.counter]
        self.counter = self.counter + 1
        return to_ret

    def get_all_lines(self):
        return self.lines