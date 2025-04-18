"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/core/channel/v1/genesis.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto"\xef\x04\n\x0cGenesisState\x12S\n\x08channels\x18\x01 \x03(\x0b2&.ibc.core.channel.v1.IdentifiedChannelB\x19\xc8\xde\x1f\x00\xfa\xde\x1f\x11IdentifiedChannel\x12@\n\x10acknowledgements\x18\x02 \x03(\x0b2 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x12;\n\x0bcommitments\x18\x03 \x03(\x0b2 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x128\n\x08receipts\x18\x04 \x03(\x0b2 .ibc.core.channel.v1.PacketStateB\x04\xc8\xde\x1f\x00\x12Z\n\x0esend_sequences\x18\x05 \x03(\x0b2#.ibc.core.channel.v1.PacketSequenceB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"send_sequences"\x12Z\n\x0erecv_sequences\x18\x06 \x03(\x0b2#.ibc.core.channel.v1.PacketSequenceB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"recv_sequences"\x12X\n\rack_sequences\x18\x07 \x03(\x0b2#.ibc.core.channel.v1.PacketSequenceB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"ack_sequences"\x12?\n\x15next_channel_sequence\x18\x08 \x01(\x04B \xf2\xde\x1f\x1cyaml:"next_channel_sequence""r\n\x0ePacketSequence\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x10\n\x08sequence\x18\x03 \x01(\x04B;Z9github.com/cosmos/ibc-go/v4/modules/core/04-channel/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.channel.v1.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z9github.com/cosmos/ibc-go/v4/modules/core/04-channel/types'
    _GENESISSTATE.fields_by_name['channels']._options = None
    _GENESISSTATE.fields_by_name['channels']._serialized_options = b'\xc8\xde\x1f\x00\xfa\xde\x1f\x11IdentifiedChannel'
    _GENESISSTATE.fields_by_name['acknowledgements']._options = None
    _GENESISSTATE.fields_by_name['acknowledgements']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['commitments']._options = None
    _GENESISSTATE.fields_by_name['commitments']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['receipts']._options = None
    _GENESISSTATE.fields_by_name['receipts']._serialized_options = b'\xc8\xde\x1f\x00'
    _GENESISSTATE.fields_by_name['send_sequences']._options = None
    _GENESISSTATE.fields_by_name['send_sequences']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"send_sequences"'
    _GENESISSTATE.fields_by_name['recv_sequences']._options = None
    _GENESISSTATE.fields_by_name['recv_sequences']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"recv_sequences"'
    _GENESISSTATE.fields_by_name['ack_sequences']._options = None
    _GENESISSTATE.fields_by_name['ack_sequences']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"ack_sequences"'
    _GENESISSTATE.fields_by_name['next_channel_sequence']._options = None
    _GENESISSTATE.fields_by_name['next_channel_sequence']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"next_channel_sequence"'
    _PACKETSEQUENCE.fields_by_name['port_id']._options = None
    _PACKETSEQUENCE.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _PACKETSEQUENCE.fields_by_name['channel_id']._options = None
    _PACKETSEQUENCE.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _globals['_GENESISSTATE']._serialized_start = 116
    _globals['_GENESISSTATE']._serialized_end = 739
    _globals['_PACKETSEQUENCE']._serialized_start = 741
    _globals['_PACKETSEQUENCE']._serialized_end = 855