"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bibc/core/client/v1/tx.proto\x12\x12ibc.core.client.v1\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"\xbb\x01\n\x0fMsgCreateClient\x12C\n\x0cclient_state\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12I\n\x0fconsensus_state\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:"consensus_state"\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x19\n\x17MsgCreateClientResponse"z\n\x0fMsgUpdateClient\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12$\n\x06header\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x19\n\x17MsgUpdateClientResponse"\xf5\x02\n\x10MsgUpgradeClient\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12C\n\x0cclient_state\x18\x02 \x01(\x0b2\x14.google.protobuf.AnyB\x17\xf2\xde\x1f\x13yaml:"client_state"\x12I\n\x0fconsensus_state\x18\x03 \x01(\x0b2\x14.google.protobuf.AnyB\x1a\xf2\xde\x1f\x16yaml:"consensus_state"\x12=\n\x14proof_upgrade_client\x18\x04 \x01(\x0cB\x1f\xf2\xde\x1f\x1byaml:"proof_upgrade_client"\x12O\n\x1dproof_upgrade_consensus_state\x18\x05 \x01(\x0cB(\xf2\xde\x1f$yaml:"proof_upgrade_consensus_state"\x12\x0e\n\x06signer\x18\x06 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1a\n\x18MsgUpgradeClientResponse"\x86\x01\n\x15MsgSubmitMisbehaviour\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12*\n\x0cmisbehaviour\x18\x02 \x01(\x0b2\x14.google.protobuf.Any\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x00"\x1f\n\x1dMsgSubmitMisbehaviourResponse2\xa2\x03\n\x03Msg\x12`\n\x0cCreateClient\x12#.ibc.core.client.v1.MsgCreateClient\x1a+.ibc.core.client.v1.MsgCreateClientResponse\x12`\n\x0cUpdateClient\x12#.ibc.core.client.v1.MsgUpdateClient\x1a+.ibc.core.client.v1.MsgUpdateClientResponse\x12c\n\rUpgradeClient\x12$.ibc.core.client.v1.MsgUpgradeClient\x1a,.ibc.core.client.v1.MsgUpgradeClientResponse\x12r\n\x12SubmitMisbehaviour\x12).ibc.core.client.v1.MsgSubmitMisbehaviour\x1a1.ibc.core.client.v1.MsgSubmitMisbehaviourResponseB:Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.client.v1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/ibc-go/v4/modules/core/02-client/types'
    _MSGCREATECLIENT.fields_by_name['client_state']._options = None
    _MSGCREATECLIENT.fields_by_name['client_state']._serialized_options = b'\xf2\xde\x1f\x13yaml:"client_state"'
    _MSGCREATECLIENT.fields_by_name['consensus_state']._options = None
    _MSGCREATECLIENT.fields_by_name['consensus_state']._serialized_options = b'\xf2\xde\x1f\x16yaml:"consensus_state"'
    _MSGCREATECLIENT._options = None
    _MSGCREATECLIENT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGUPDATECLIENT.fields_by_name['client_id']._options = None
    _MSGUPDATECLIENT.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MSGUPDATECLIENT._options = None
    _MSGUPDATECLIENT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGUPGRADECLIENT.fields_by_name['client_id']._options = None
    _MSGUPGRADECLIENT.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MSGUPGRADECLIENT.fields_by_name['client_state']._options = None
    _MSGUPGRADECLIENT.fields_by_name['client_state']._serialized_options = b'\xf2\xde\x1f\x13yaml:"client_state"'
    _MSGUPGRADECLIENT.fields_by_name['consensus_state']._options = None
    _MSGUPGRADECLIENT.fields_by_name['consensus_state']._serialized_options = b'\xf2\xde\x1f\x16yaml:"consensus_state"'
    _MSGUPGRADECLIENT.fields_by_name['proof_upgrade_client']._options = None
    _MSGUPGRADECLIENT.fields_by_name['proof_upgrade_client']._serialized_options = b'\xf2\xde\x1f\x1byaml:"proof_upgrade_client"'
    _MSGUPGRADECLIENT.fields_by_name['proof_upgrade_consensus_state']._options = None
    _MSGUPGRADECLIENT.fields_by_name['proof_upgrade_consensus_state']._serialized_options = b'\xf2\xde\x1f$yaml:"proof_upgrade_consensus_state"'
    _MSGUPGRADECLIENT._options = None
    _MSGUPGRADECLIENT._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _MSGSUBMITMISBEHAVIOUR.fields_by_name['client_id']._options = None
    _MSGSUBMITMISBEHAVIOUR.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MSGSUBMITMISBEHAVIOUR._options = None
    _MSGSUBMITMISBEHAVIOUR._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00'
    _globals['_MSGCREATECLIENT']._serialized_start = 101
    _globals['_MSGCREATECLIENT']._serialized_end = 288
    _globals['_MSGCREATECLIENTRESPONSE']._serialized_start = 290
    _globals['_MSGCREATECLIENTRESPONSE']._serialized_end = 315
    _globals['_MSGUPDATECLIENT']._serialized_start = 317
    _globals['_MSGUPDATECLIENT']._serialized_end = 439
    _globals['_MSGUPDATECLIENTRESPONSE']._serialized_start = 441
    _globals['_MSGUPDATECLIENTRESPONSE']._serialized_end = 466
    _globals['_MSGUPGRADECLIENT']._serialized_start = 469
    _globals['_MSGUPGRADECLIENT']._serialized_end = 842
    _globals['_MSGUPGRADECLIENTRESPONSE']._serialized_start = 844
    _globals['_MSGUPGRADECLIENTRESPONSE']._serialized_end = 870
    _globals['_MSGSUBMITMISBEHAVIOUR']._serialized_start = 873
    _globals['_MSGSUBMITMISBEHAVIOUR']._serialized_end = 1007
    _globals['_MSGSUBMITMISBEHAVIOURRESPONSE']._serialized_start = 1009
    _globals['_MSGSUBMITMISBEHAVIOURRESPONSE']._serialized_end = 1040
    _globals['_MSG']._serialized_start = 1043
    _globals['_MSG']._serialized_end = 1461