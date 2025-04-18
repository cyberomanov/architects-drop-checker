"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....tendermint.types import params_pb2 as tendermint_dot_types_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/consensus/v1/query.proto\x12\x13cosmos.consensus.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1dtendermint/types/params.proto"\x14\n\x12QueryParamsRequest"H\n\x13QueryParamsResponse\x121\n\x06params\x18\x01 \x01(\x0b2!.tendermint.types.ConsensusParams2\x8a\x01\n\x05Query\x12\x80\x01\n\x06Params\x12\'.cosmos.consensus.v1.QueryParamsRequest\x1a(.cosmos.consensus.v1.QueryParamsResponse"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/consensus/v1/paramsB0Z.github.com/cosmos/cosmos-sdk/x/consensus/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.consensus.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z.github.com/cosmos/cosmos-sdk/x/consensus/types'
    _QUERY.methods_by_name['Params']._options = None
    _QUERY.methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1d\x12\x1b/cosmos/consensus/v1/params'
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 117
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 137
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 139
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 211
    _globals['_QUERY']._serialized_start = 214
    _globals['_QUERY']._serialized_end = 352