"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ..... import proofs_pb2 as proofs__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'ibc/core/commitment/v1/commitment.proto\x12\x16ibc.core.commitment.v1\x1a\x14gogoproto/gogo.proto\x1a\x0cproofs.proto" \n\nMerkleRoot\x12\x0c\n\x04hash\x18\x01 \x01(\x0c:\x04\x88\xa0\x1f\x00"9\n\x0cMerklePrefix\x12)\n\nkey_prefix\x18\x01 \x01(\x0cB\x15\xf2\xde\x1f\x11yaml:"key_prefix""9\n\nMerklePath\x12%\n\x08key_path\x18\x01 \x03(\tB\x13\xf2\xde\x1f\x0fyaml:"key_path":\x04\x98\xa0\x1f\x00"5\n\x0bMerkleProof\x12&\n\x06proofs\x18\x01 \x03(\x0b2\x16.ics23.CommitmentProofB>Z<github.com/cosmos/ibc-go/v4/modules/core/23-commitment/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.core.commitment.v1.commitment_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z<github.com/cosmos/ibc-go/v4/modules/core/23-commitment/types'
    _MERKLEROOT._options = None
    _MERKLEROOT._serialized_options = b'\x88\xa0\x1f\x00'
    _MERKLEPREFIX.fields_by_name['key_prefix']._options = None
    _MERKLEPREFIX.fields_by_name['key_prefix']._serialized_options = b'\xf2\xde\x1f\x11yaml:"key_prefix"'
    _MERKLEPATH.fields_by_name['key_path']._options = None
    _MERKLEPATH.fields_by_name['key_path']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"key_path"'
    _MERKLEPATH._options = None
    _MERKLEPATH._serialized_options = b'\x98\xa0\x1f\x00'
    _globals['_MERKLEROOT']._serialized_start = 103
    _globals['_MERKLEROOT']._serialized_end = 135
    _globals['_MERKLEPREFIX']._serialized_start = 137
    _globals['_MERKLEPREFIX']._serialized_end = 194
    _globals['_MERKLEPATH']._serialized_start = 196
    _globals['_MERKLEPATH']._serialized_end = 253
    _globals['_MERKLEPROOF']._serialized_start = 255
    _globals['_MERKLEPROOF']._serialized_end = 308