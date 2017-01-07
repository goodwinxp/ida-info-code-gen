from pida_abc_type import IdaTypes
from pida_types import IDA_TYPES
from pida_type_decoder import decode_hybrid_type


class IdaTTypedef(IdaTypes):
    def __init__(self, ida_type=IDA_TYPES['typedef']):
        self.ida_type = {'idt': ida_type, 'value': None}

    def decode(self, data):
        len_str, value = decode_hybrid_type(data)
        self.ida_type['value'] = value

        return len_str

    def get_type(self):
        return self.ida_type
