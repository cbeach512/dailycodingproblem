#!/usr/bin/env python3
"""Problem - Day 7
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""
class CodeNode():
    def __init__(self, val, prv=None):
        self.v = val
        self.p = prv
        self.n = None

class DecoderRing():
    _alpha = 'abcdefghijklmnopqrstuvwxyz'
    def __init__(self, alpha = _alpha):
        self.num_keys = {l[0] + 1: l[1] for l in enumerate(alpha)}
        self.alpha_keys = {l[1]: l[0] + 1 for l in enumerate(alpha)}

    def encode(self, msg):
        encoded_list = [str(self.alpha_keys[l]) for l in msg]
        encoded_msg = ''.join(encoded_list)
        return encoded_msg

    def decode(self, code):
        dl = []
        for l in enumerate(code):
            if 0 < l[0]:
                dl.append(CodeNode(l[1], dl[-1]))
                dl[-1].p.n = dl[-1]
            elif l[0] == 0:
                dl.append(CodeNode(l[1]))
        decoded_list = self._decode(dl)
        possibles = self._flaten(decoded_list)
        return possibles

    def _decode(self, decode_list, decoded_list = None):
        if decoded_list is None:
            decoded_list = []
        for c in enumerate(decode_list):
            if int(c[1].v) == 0:
                continue
            elif c[1].n is None:
                decoded_list.append(self.num_keys[int(c[1].v)])
            elif int(c[1].n.v) == 0:
                decoded_list.append(self.num_keys[int(c[1].v + c[1].n.v)])
            elif c[1].n.n is None or int(c[1].n.n.v) > 0:
                if int(c[1].v) == 1:
                    decoded_list_n = [n for n in decoded_list]
                    decoded_list.append(self.num_keys[int(c[1].v)])
                    decoded_list_n.append(self.num_keys[int(c[1].v + c[1].n.v)])
                    decoded_list_combi = [self._decode(decode_list[c[0] + 1:], decoded_list), self._decode(decode_list[c[0] + 2:], decoded_list_n)]
                    return decoded_list_combi
                if int(c[1].v) == 2 and int(c[1].n.v) < 7:
                    decoded_list_n = [n for n in decoded_list]
                    decoded_list.append(self.num_keys[int(c[1].v)])
                    decoded_list_n.append(self.num_keys[int(c[1].v + c[1].n.v)])
                    decoded_list_combi = [self._decode(decode_list[c[0] + 1:], decoded_list), self._decode(decode_list[c[0] + 2:], decoded_list_n)]
                    return decoded_list_combi
                decoded_list.append(self.num_keys[int(c[1].v)])
            else:
                decoded_list.append(self.num_keys[int(c[1].v)])
        return decoded_list

    def _flaten(self, decoded_list):
        result = []
        for i in decoded_list:
            if type(i) == str:
                result.append(''.join(decoded_list))
                return result
            elif type(i) == list:
                result.extend(self._flaten(i))
        return result

if __name__ == '__main__':
    ring = DecoderRing()
    print('111 => {}\n'.format(ring.decode('111')))
    print('mynameisjeff => {}\n'.format(ring.encode('mynameisjeff')))
    print('132514113591910566 => {}\n'.format(ring.decode('132514113591910566')))
    print('anotherstring => {}\n'.format(ring.encode('anotherstring')))
    print('114152085181920189147 => {}\n'.format(ring.decode('114152085181920189147')))

