# -*- coding:utf-8 -*-
"""
For Open Extended Dictionary format
See http://www.microsoft.com/downloads/ja-jp/details.aspx?FamilyID=f138dcd4-edb3-4319-bb69-82784e3ea52f for details
"""

import xml.sax
import xml.sax.handler

from model import *

_ns_dctx = 'http://www.microsoft.com/ime/dctx'

class Handler(xml.sax.handler.ContentHandler):
    _entry_tags = (
        'InputString', 'OutputString', 'PartOfSpeech',
        'CommentData1', 'CommentData2', 'CommentData3',
        'URL', 'Priority', 'ReverseConversion', 'CommonWord')
    _header_tags = (
        'DictionaryGUID', 'DictionaryLanguage', 'DictionaryVersion',
        'SourceURL', 'CommentInsertion')
    _info_tags = (
        'ShortName', 'LongName', 'Description', 'Copyright',
        'CommentHeader1', 'CommentHeader2', 'CommentHeader3')

    def startDocument(self):
        self._dic = Dictionary()
        self._dicentry = {}
        self._nest = []
        self._text = ''

    @property
    def dic(self):
        return self._dic

    def startElementNS(self, name, qname, attrs):
        nest = self._nest

        if name[0]==_ns_dctx and name[1] in Handler._entry_tags:
            if nest[-1]!=(_ns_dctx, 'DictionaryEntry'):
                raise ValueError
        elif name==(_ns_dctx, 'DictionaryEntry'):
            if nest[-1]!=(_ns_dctx, 'Dictionary'):
                raise ValueError
            self._dicentry = {}
        elif name==(_ns_dctx, 'DictionaryInfo'):
            if nest[-1]!=(_ns_dctx, 'DictionaryHeader'):
                raise ValueError
            self._info = DictionaryInfo(attrs[(None, 'Language')])
        elif name[0]==_ns_dctx and name[1] in Handler._info_tags:
            if nest[-1]!=(_ns_dctx, 'DictionaryInfo'):
                raise ValueError
        elif name[0]==_ns_dctx and name[1] in Handler._header_tags:
            if nest[-1]!=(_ns_dctx, 'DictionaryHeader'):
                raise ValueError
        elif name==(_ns_dctx, 'DictionaryHeader'):
            if nest[-1]!=(_ns_dctx, 'Dictionary'):
                raise ValueError
        elif name==(_ns_dctx, 'Dictionary'):
            if len(nest)!=0:
                raise ValueError

        self._text = ''
        nest.append(name)

    def endElementNS(self, name, qname):
        nest = self._nest
        nest.pop()
        text = self._text

        if name==(_ns_dctx, 'DictionaryEntry'):
            entry = self._dicentry
            if 'Priority' in entry:
                entry['Priority'] = int(entry['Priority'])
            if 'ReverseConversion' in entry:
                if entry['ReverseConversion'].strip() == 'true':
                    entry['ReverseConversion'] = True
                elif entry['ReverseConversion'].strip() == 'false':
                    entry['ReverseConversion'] = False
                else:
                    raise ValueError
            if 'CommonWord' in entry:
                if entry['CommonWord'].strip() == 'true':
                    entry['CommonWord'] = True
                elif entry['CommonWord'].strip() == 'false':
                    entry['CommonWord'] = False
                else:
                    raise ValueError
            self._dic.append(makeDictionaryEntry(**self._dicentry))
        elif name[0]==_ns_dctx and name[1] in Handler._entry_tags:
            self._dicentry[name[1]] = self._text
        elif name[0]==_ns_dctx and name[1] in Handler._info_tags:
            setattr(self._info, name[1], self._text)
        elif name==(_ns_dctx, 'DictionaryGUID'):
            self._dic.GUID = text.strip()
        elif name==(_ns_dctx, 'DictionaryLanguage'):
            self._dic.Language = text.strip()
        elif name==(_ns_dctx, 'DictionaryVersion'):
            self._dic.Version = int(text.strip())
        elif name==(_ns_dctx, 'SourceURL'):
            self._dic.SourceURL = text.strip()
        elif name==(_ns_dctx, 'CommentInsertion'):
            if text.strip() == 'true':
                self._dic.CommentInsertion = True
            elif text.strip() == 'false':
                self._dic.CommentInsertion = False
            else:
                raise ValueError
        elif name==(_ns_dctx, 'DictionaryInfo'):
            self._dic.Info.add(self._info)

    def characters(self, content):
        self._text += content


def parse(f):
    parser = xml.sax.make_parser()
    handler = Handler()
    parser.setContentHandler(handler)
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setFeature(xml.sax.handler.feature_namespaces, True)

    parser.parse(f)
    return handler.dic
