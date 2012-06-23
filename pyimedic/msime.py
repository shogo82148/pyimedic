# -*- coding:utf-8 -*-

from model import *
import re

_dctx2msime = {
    u'Noun': u'名詞',
    u'Noun-Sa': u'さ変名詞',
    u'Noun-Za': u'ざ変名詞',
    u'Noun-Adjectival': u'形動名詞',
    u'Noun-Adverb': u'副詞的名詞',
    u'Noun-Sa-Adjectival': u'さ変形動名詞',
    u'Name-Personal': u'人名',
    u'Name-Family': u'姓',
    u'Name-Given': u'名',
    u'Place': u'地名その他',
    u'Place-Prefecture': u'地名その他',
    u'Place-Country': u'地名その他',
    u'Place-Ward': u'地名その他',
    u'Place-City': u'地名その他',
    u'Place-Town': u'地名その他',
    u'Place-Town-Machi': u'地名その他',
    u'Place-Town-Cho': u'地名その他',
    u'Place-Village': u'地名その他',
    u'Place-Village-Mura': u'地名その他',
    u'Place-Village-Son': u'地名その他',
    u'Place-Station': u'地名その他',
    u'Noun-Proper': u'固有名詞',
    u'Name-Company': u'固有名詞',
    u'Name-Organization': u'固有名詞',
    u'Name-Construction': u'固有名詞',
    u'Pronoun': u'名詞',
    u'Number': u'名詞',
    u'Verb-5-AW': u'あわ行五段',
    u'Verb-5-K': u'か行五段',
    u'Verb-5-G': u'が行五段',
    u'Verb-5-S': u'さ行五段',
    u'Verb-5-T': u'た行五段',
    u'Verb-5-N': u'な行五段',
    u'Verb-5-B': u'ば行五段',
    u'Verb-5-M': u'ま行五段',
    u'Verb-5-R': u'ら行五段',
    u'Verb-EuphonyU-AW': u'あわ行五段',
    u'Verb-Euphony-K': u'か行五段',
    u'Verb-Irregular-R': u'ら行五段',
    u'Verb-1': u'一段動詞',
    u'Adjective': u'形容詞',
    u'Adjective-Garu': u'形容詞',
    u'Adjective-Me': u'形容詞',
    u'Adjective-Syu': u'形容詞',
    u'AdjectivalNoun': u'形容動詞',
    u'AdjectivalNoun-No': u'形容動詞',
    u'AdjectivalNoun-Taru': u'形容動詞',
    u'Adverb': u'副詞',
    u'Adverb-Suru': u'副詞',
    u'Adverb-Ni': u'副詞',
    u'Adverb-Na': u'副詞',
    u'Adverb-Da': u'副詞',
    u'Adverb-To': u'副詞',
    u'Adverb-Tosuru': u'副詞',
    u'Adnominal': u'連帯詞',
    u'Conjuction': u'接続詞',
    u'Interjection': u'感動詞',
    u'Prefix': u'接頭語',
    u'Suffix': u'接尾語',
    u'Suffix-PersonalName': u'姓名接尾語',
    u'Suffix-Number': u'助数詞',
    u'Prefix-Number': u'助数詞',
    u'Suffix-Prefecture': u'地名接尾語',
    u'Suffix-Country': u'地名接尾語',
    u'Suffix-Ward': u'地名接尾語',
    u'Suffix-City': u'地名接尾語',
    u'Suffix-Town1': u'地名接尾語',
    u'Suffix-Town2': u'地名接尾語',
    u'Character': u'名詞',
    u'Symbol': u'名詞',
    u'Idiom': u'慣用句',
    u'ShortCut': u'短縮よみ',
    u'Emotion': u'顔文字',
}

_msime2dctx = {
    u'名詞': u'Noun',
    u'さ変名詞': u'Noun-Sa',
    u'ざ変名詞': u'Noun-Za',
    u'形動名詞': u'Noun-Adjectival',
    u'副詞的名詞': u'Noun-Adverb',
    u'さ変形動名詞': u'Noun-Sa-Adjectival',
    u'人名': u'Name-Personal',
    u'姓': u'Name-Family',
    u'名': u'Name-Given',
    u'地名その他': u'Place',
    u'固有名詞': u'Noun-Proper',
    u'あわ行五段': u'Verb-5-AW',
    u'か行五段': u'Verb-5-K',
    u'が行五段': u'Verb-5-G',
    u'さ行五段': u'Verb-5-S',
    u'た行五段': u'Verb-5-T',
    u'な行五段': u'Verb-5-N',
    u'ば行五段': u'Verb-5-B',
    u'ま行五段': u'Verb-5-M',
    u'ら行五段': u'Verb-5-R',
    u'一段動詞': u'Verb-1',
    u'形容詞': u'Adjective',
    u'形容動詞': u'AdjectivalNoun',
    u'副詞': u'Adverb',
    u'連帯詞': u'Adnominal',
    u'接続詞': u'Conjuction',
    u'感動詞': u'Interjection',
    u'接頭語': u'Prefix',
    u'姓名接頭語': u'Prefix',
    u'地名接頭語': u'Prefix',
    u'接尾語': u'Suffix',
    u'姓名接尾語': u'Suffix-PersonalName',
    u'助数詞': u'Suffix-Number',
    u'地名接尾語': u'Suffix',
    u'慣用句': u'Idiom',
    u'短縮よみ': u'ShortCut',
    u'顔文字': u'Emotion',
}

_re_version = re.compile(r'!version:\s*(\d+)', re.I)
_re_guid = re.compile(r'!guid:\s*(\{[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\})', re.I)
_re_sourceurl = re.compile(r'!source\s*url:\s*(.*)', re.I)
_re_commentinsertion = re.compile(r'!comment\s*insertion:\s*(true|false)', re.I)
_re_language = re.compile(r'!language:\s*(.*)', re.I)
_re_shortname = re.compile(r'!short\s*name\s*\(([a-z-]+)\):\s*(.*)', re.I)
_re_longname = re.compile(r'!long\s*name\s*\(([a-z-]+)\):\s*(.*)', re.I)
_re_longname = re.compile(r'!long\s*name\s*\(([a-z-]+)\):\s*(.*)', re.I)
_re_description = re.compile(r'!description\s*\(([a-z-]+)\):\s*(.*)', re.I)
_re_copyright = re.compile(r'!copyright\s*\(([a-z-]+)\):\s*(.*)', re.I)
_re_commentheader = re.compile(r'!comment\s*header\s*([1-3])\s*\(([a-z-]+)\):\s*(.*)', re.I)

def read(f):
    def info(lang):
        if lang not in d.Info:
            d.Info.add(DictionaryInfo(lang))
        return d.Info[lang]

    d = Dictionary()
    for line in f:
        line = line.decode('cp932').strip()
        if line[0]=='!':
            m = _re_version.match(line)
            if m:
                d.Version = int(m.group(1))
                continue
            m = _re_guid.search(line)
            if m:
                d.GUID = m.group(1)
                continue
            m = _re_sourceurl.match(line)
            if m:
                d.SourceURL = m.group(1)
            m = _re_commentinsertion.match(line)
            if m:
                d.CommentInsertion = (m.group(1).lower()=='true')
            m = _re_language.match(line)
            if m:
                d.Language = m.group(1)
            m = _re_shortname.match(line)
            if m:
                info(m.group(1)).ShortName = m.group(2)
            m = _re_longname.match(line)
            if m:
                info(m.group(1)).LongName = m.group(2)
            m = _re_description.match(line)
            if m:
                info(m.group(1)).Description = m.group(2)
            m = _re_copyright.match(line)
            if m:
                info(m.group(1)).Copyright = m.group(2)
            m = _re_commentheader.match(line)
            if m:
                if m.group(1)=='1':
                    info(m.group(2)).CommentHeader1 = m.group(3)
                elif m.group(1)=='2':
                    info(m.group(2)).CommentHeader2 = m.group(3)
                elif m.group(1)=='3':
                    info(m.group(2)).CommentHeader3 = m.group(3)
        else:
            columns = line.split('\t')
            if len(columns)<3:
                continue
            entry = {}
            entry['InputString'] = columns[0]
            entry['OutputString'] = columns[1]
            entry['PartOfSpeech'] = _msime2dctx.get(columns[2], columns[2])
            if len(columns)>=4:
                comments = columns[3].split(',')
                index = 1
                for comment in comments:
                    if 'URL' not in entry and (
                        comment.startswith('http://') or comment.startswith('https://')):
                        entry['URL'] = comment
                    else:
                        entry['CommentData{0}'.format(index)] = comment
                        index += 1
                        if index>3:
                            break
            d.append(makeDictionaryEntry(**entry))
    return d

def write(f, d):
    def e(string):
        string = string.replace('\t', ' ')
        string = string.replace('\n', ' ')
        string = string.replace('\r', '')
        return string.encode('cp932', 'ignore')

    f.write('!Microsoft IME Dictionary Tool\n')
    f.write('!Version: {0}\n'.format(d.Version))
    f.write('!Format: WORDLIST\n')
    f.write('!Output File Name:\n')
    f.write('!DateTime:\n')
    if d.GUID:
        f.write('!GUID: {0}\n'.format(e(d.GUID)))
    if d.Language:
        f.write('!Language: {0}\n'.format(e(d.Language)))
    if d.SourceURL:
        f.write('!Source URL: {0}\n'.format(e(d.SourceURL)))
    for info in d.Info.itervalues():
        f.write('!Short Name ({0}): {1}\n'.format(info.Language, e(info.ShortName)))
        f.write('!Long Name ({0}): {1}\n'.format(info.Language, e(info.LongName)))
        f.write('!Description ({0}): {1}\n'.format(info.Language, e(info.Description)))
        f.write('!Copyright ({0}): {1}\n'.format(info.Language, e(info.Copyright)))
        f.write('!Comment Insertion: {0}\n'.format('true' if d.CommentInsertion else 'false'))
        f.write('!Comment Header 1 ({0}): {1}\n'.format(info.Language, e(info.CommentHeader1)))
        f.write('!Comment Header 2 ({0}): {1}\n'.format(info.Language, e(info.CommentHeader2)))
        f.write('!Comment Header 3 ({0}): {1}\n'.format(info.Language, e(info.CommentHeader3)))

    for entry in d:
        f.write(e(entry.InputString) + '\t')
        f.write(e(entry.OutputString) + '\t')
        f.write(e(_dctx2msime.get(entry.PartOfSpeech, entry.PartOfSpeech)))
        comments = []
        if entry.CommentData1:
            comments.append(entry.CommentData1)
        if entry.CommentData2:
            comments.append(entry.CommentData2)
        if entry.CommentData3:
            comments.append(entry.CommentData3)
        if entry.URL:
            comments.append(entry.URL)
        if len(comments)!=0:
            f.write('\t' + e(','.join(comments)))
        f.write('\n')
