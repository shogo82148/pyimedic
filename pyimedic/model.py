# -*- coding: utf-8 -*-

import re
import itertools
from collections import namedtuple


DictionaryEntry = namedtuple(
    'DictionaryEntry',
    'InputString OutputString PartOfSpeech '
    'CommentData1 CommentData2 CommentData3 '
    'URL Priority ReverseConversion CommonWord ')

_default_entry = DictionaryEntry(
    InputString = "",
    OutputString = "",
    PartOfSpeech = "",
    CommentData1 = "",
    CommentData2 = "",
    CommentData3 = "",
    URL = "",
    Priority = 100,
    ReverseConversion = False,
    CommonWord = False)


def makeDictionaryEntry(*args, **kargs):
    for name, val in itertools.izip(DictionaryEntry._fields, args):
        kargs[name] = val
    if 'InputString' not in kargs:
        raise TypeError('InputString is nessesary')
    if 'OutputString' not in kargs:
        raise TypeError('OutputString is nessesary')
    if ('URL' in kargs and kargs['URL'] and
        not kargs['URL'].startswith('http://') and
        not kargs['URL'].startswith('https://')):
        raise ValueError('Invalid URL format' + kargs['URL'])
    if ('Priority' in kargs and
        not 0 <= kargs['Priority'] <= 255):
        raise ValueError('Priority is out of range')

    return _default_entry._replace(**kargs)


class Dictionary(list):

    _re_guid = re.compile(r"\{[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\}", re.I)

    def __init__(self):
        super(Dictionary, self).__init__()
        self._GUID = None
        self._Language = "ja-jp"
        self._Version = 0
        self._SourceURL = ""
        self._CommentInsertion = False
        self._Info = DictionaryInfoSet()

    @property
    def GUID(self):
        return self._GUID

    @GUID.setter
    def GUID(self, val):
        if not Dictionary._re_guid.match(val):
            raise ValueError('Invalid GUID format')
        self._GUID = val


    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, val):
        if val not in ['ja-jp', 'zh-cn']:
            raise ValueError('Invalid Language')
        self._Language = val


    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, val):
        if not 0 <= val <= 9999:
            raise ValueError('Invalid Version Number')
        self._Version = val


    @property
    def SourceURL(self):
        return self._SourceURL

    @SourceURL.setter
    def SourceURL(self, val):
        self._SourceURL = val


    @property
    def CommentInsertion(self):
        return self._CommentInsertion

    @CommentInsertion.setter
    def CommentInsertion(self, val):
        self._CommentInsertion = True if val else False

    @property
    def Info(self):
        return self._Info

class DictionaryInfoSet(object):
    def __init__(self):
        self._Info = []

    def __len__(self):
        return len(self._Info)

    def __getitem__(self, key):
        for info in self._Info:
            if info.Language==key:
                return info
        raise IndexError

    def __setitem__(self, key, val):
        self.add(val)

    def add(self, val):
        if not isinstance(val, DictionaryInfo):
            raise TypeError
        key = val.Language
        index = -1
        for i, info in enumerate(self._Info):
            if info.Language==key:
                index = i

        if index<0:
            self._Info.append(val)
        else:
            self._Info[index] = val
        return val

    def __delitem__(self, key):
        index = -1
        for i, info in enumerate(self._Info):
            if info.Language==key:
                index = i
        if index<0:
            raise IndexError
        else:
            del self._Info[index]

    def __iter__(self):
        for info in self._Info:
            yield info.Language

    def __contains__(self, key):
        for info in self._Info:
            if info.Language==key:
                return True
        return False

    def has_key(self, key):
        return key in self

    def keys(self):
        return [info.Language for info in self._Info]

    def values(self):
        return [info for info in self._Info]

    def items(self):
        return [[info.Language, info] for info in self._Info]

    def iterkeys(self):
        return (info.Language for info in self._Info)

    def itervalues(self):
        return (info for info in self._Info)

    def iteritems(self):
        return ([info.Language, info] for info in self._Info)


class DictionaryInfo(object):
    def __init__(
        self,
        Language='ja-jp',
        ShortName = '',
        LongName = '',
        Description = '',
        Copyright = '',
        CommentHeader1 = '',
        CommentHeader2 = '',
        CommentHeader3 = ''):

        self.Language = Language
        self.ShortName = ShortName
        self.LongName = LongName
        self.Description = Description
        self.Copyright = Copyright
        self.CommentHeader1 = CommentHeader1
        self.CommentHeader2 = CommentHeader2
        self.CommentHeader3 = CommentHeader3

    @property
    def Language(self):
        return self._Language

    @Language.setter
    def Language(self, val):
        if val not in ['en-us', 'ja-jp', 'zh-cn']:
            raise ValueError('Invalid Language')
        self._Language = val

    @property
    def ShortName(self):
        return self._ShortName

    @ShortName.setter
    def ShortName(self, val):
        self._ShortName = val


    @property
    def LongName(self):
        return self._LongName

    @LongName.setter
    def LongName(self, val):
        self._LongName = val


    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, val):
        self._Description = val


    @property
    def Copyright(self):
        return self._Copyright

    @Copyright.setter
    def Copyright(self, val):
        self._Copyright = val


    @property
    def CommentHeader1(self):
        return self._CommentHeader1

    @CommentHeader1.setter
    def CommentHeader1(self, val):
        self._CommentHeader1 = val


    @property
    def CommentHeader2(self):
        return self._CommentHeader2

    @CommentHeader2.setter
    def CommentHeader2(self, val):
        self._CommentHeader2 = val


    @property
    def CommentHeader3(self):
        return self._CommentHeader3

    @CommentHeader3.setter
    def CommentHeader3(self, val):
        self._CommentHeader3 = val
