"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...tendermint.crypto import keys_pb2 as tendermint_dot_crypto_dot_keys__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n tendermint/types/validator.proto\x12\x10tendermint.types\x1a\x14gogoproto/gogo.proto\x1a\x1ctendermint/crypto/keys.proto"\x8a\x01\n\x0cValidatorSet\x12/\n\nvalidators\x18\x01 \x03(\x0b2\x1b.tendermint.types.Validator\x12-\n\x08proposer\x18\x02 \x01(\x0b2\x1b.tendermint.types.Validator\x12\x1a\n\x12total_voting_power\x18\x03 \x01(\x03"\x82\x01\n\tValidator\x12\x0f\n\x07address\x18\x01 \x01(\x0c\x123\n\x07pub_key\x18\x02 \x01(\x0b2\x1c.tendermint.crypto.PublicKeyB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cvoting_power\x18\x03 \x01(\x03\x12\x19\n\x11proposer_priority\x18\x04 \x01(\x03"V\n\x0fSimpleValidator\x12-\n\x07pub_key\x18\x01 \x01(\x0b2\x1c.tendermint.crypto.PublicKey\x12\x14\n\x0cvoting_power\x18\x02 \x01(\x03B9Z7github.com/tendermint/tendermint/proto/tendermint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.types.validator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z7github.com/tendermint/tendermint/proto/tendermint/types'
    _VALIDATOR.fields_by_name['pub_key']._options = None
    _VALIDATOR.fields_by_name['pub_key']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_VALIDATORSET']._serialized_start = 107
    _globals['_VALIDATORSET']._serialized_end = 245
    _globals['_VALIDATOR']._serialized_start = 248
    _globals['_VALIDATOR']._serialized_end = 378
    _globals['_SIMPLEVALIDATOR']._serialized_start = 380
    _globals['_SIMPLEVALIDATOR']._serialized_end = 466