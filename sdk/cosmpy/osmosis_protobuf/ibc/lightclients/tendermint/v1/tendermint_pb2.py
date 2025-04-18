"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....tendermint.types import validator_pb2 as tendermint_dot_types_dot_validator__pb2
from .....tendermint.types import types_pb2 as tendermint_dot_types_dot_types__pb2
from ..... import proofs_pb2 as proofs__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from .....ibc.core.commitment.v1 import commitment_pb2 as ibc_dot_core_dot_commitment_dot_v1_dot_commitment__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/ibc/lightclients/tendermint/v1/tendermint.proto\x12\x1eibc.lightclients.tendermint.v1\x1a tendermint/types/validator.proto\x1a\x1ctendermint/types/types.proto\x1a\x0cproofs.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fibc/core/client/v1/client.proto\x1a\'ibc/core/commitment/v1/commitment.proto\x1a\x14gogoproto/gogo.proto"\xbc\x06\n\x0bClientState\x12\x10\n\x08chain_id\x18\x01 \x01(\t\x12Y\n\x0btrust_level\x18\x02 \x01(\x0b2(.ibc.lightclients.tendermint.v1.FractionB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"trust_level"\x12V\n\x0ftrusting_period\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB"\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"trusting_period"\x98\xdf\x1f\x01\x12X\n\x10unbonding_period\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB#\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"unbonding_period"\x98\xdf\x1f\x01\x12V\n\x0fmax_clock_drift\x18\x05 \x01(\x0b2\x19.google.protobuf.DurationB"\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"max_clock_drift"\x98\xdf\x1f\x01\x12O\n\rfrozen_height\x18\x06 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"frozen_height"\x12O\n\rlatest_height\x18\x07 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"latest_height"\x12=\n\x0bproof_specs\x18\x08 \x03(\x0b2\x10.ics23.ProofSpecB\x16\xf2\xde\x1f\x12yaml:"proof_specs"\x12-\n\x0cupgrade_path\x18\t \x03(\tB\x17\xf2\xde\x1f\x13yaml:"upgrade_path"\x12I\n\x19allow_update_after_expiry\x18\n \x01(\x08B&\x18\x01\xf2\xde\x1f yaml:"allow_update_after_expiry"\x12U\n\x1fallow_update_after_misbehaviour\x18\x0b \x01(\x08B,\x18\x01\xf2\xde\x1f&yaml:"allow_update_after_misbehaviour":\x04\x88\xa0\x1f\x00"\xfe\x01\n\x0eConsensusState\x127\n\ttimestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x126\n\x04root\x18\x02 \x01(\x0b2".ibc.core.commitment.v1.MerkleRootB\x04\xc8\xde\x1f\x00\x12u\n\x14next_validators_hash\x18\x03 \x01(\x0cBW\xf2\xde\x1f\x1byaml:"next_validators_hash"\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes:\x04\x88\xa0\x1f\x00"\xf1\x01\n\x0cMisbehaviour\x12\'\n\tclient_id\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"client_id"\x12X\n\x08header_1\x18\x02 \x01(\x0b2&.ibc.lightclients.tendermint.v1.HeaderB\x1e\xe2\xde\x1f\x07Header1\xf2\xde\x1f\x0fyaml:"header_1"\x12X\n\x08header_2\x18\x03 \x01(\x0b2&.ibc.lightclients.tendermint.v1.HeaderB\x1e\xe2\xde\x1f\x07Header2\xf2\xde\x1f\x0fyaml:"header_2":\x04\x88\xa0\x1f\x00"\xdc\x02\n\x06Header\x12S\n\rsigned_header\x18\x01 \x01(\x0b2\x1e.tendermint.types.SignedHeaderB\x1c\xd0\xde\x1f\x01\xf2\xde\x1f\x14yaml:"signed_header"\x12O\n\rvalidator_set\x18\x02 \x01(\x0b2\x1e.tendermint.types.ValidatorSetB\x18\xf2\xde\x1f\x14yaml:"validator_set"\x12Q\n\x0etrusted_height\x18\x03 \x01(\x0b2\x1a.ibc.core.client.v1.HeightB\x1d\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"trusted_height"\x12Y\n\x12trusted_validators\x18\x04 \x01(\x0b2\x1e.tendermint.types.ValidatorSetB\x1d\xf2\xde\x1f\x19yaml:"trusted_validators""2\n\x08Fraction\x12\x11\n\tnumerator\x18\x01 \x01(\x04\x12\x13\n\x0bdenominator\x18\x02 \x01(\x04BGZEgithub.com/cosmos/ibc-go/v4/modules/light-clients/07-tendermint/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.lightclients.tendermint.v1.tendermint_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'ZEgithub.com/cosmos/ibc-go/v4/modules/light-clients/07-tendermint/types'
    _CLIENTSTATE.fields_by_name['trust_level']._options = None
    _CLIENTSTATE.fields_by_name['trust_level']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"trust_level"'
    _CLIENTSTATE.fields_by_name['trusting_period']._options = None
    _CLIENTSTATE.fields_by_name['trusting_period']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"trusting_period"\x98\xdf\x1f\x01'
    _CLIENTSTATE.fields_by_name['unbonding_period']._options = None
    _CLIENTSTATE.fields_by_name['unbonding_period']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"unbonding_period"\x98\xdf\x1f\x01'
    _CLIENTSTATE.fields_by_name['max_clock_drift']._options = None
    _CLIENTSTATE.fields_by_name['max_clock_drift']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"max_clock_drift"\x98\xdf\x1f\x01'
    _CLIENTSTATE.fields_by_name['frozen_height']._options = None
    _CLIENTSTATE.fields_by_name['frozen_height']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"frozen_height"'
    _CLIENTSTATE.fields_by_name['latest_height']._options = None
    _CLIENTSTATE.fields_by_name['latest_height']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x14yaml:"latest_height"'
    _CLIENTSTATE.fields_by_name['proof_specs']._options = None
    _CLIENTSTATE.fields_by_name['proof_specs']._serialized_options = b'\xf2\xde\x1f\x12yaml:"proof_specs"'
    _CLIENTSTATE.fields_by_name['upgrade_path']._options = None
    _CLIENTSTATE.fields_by_name['upgrade_path']._serialized_options = b'\xf2\xde\x1f\x13yaml:"upgrade_path"'
    _CLIENTSTATE.fields_by_name['allow_update_after_expiry']._options = None
    _CLIENTSTATE.fields_by_name['allow_update_after_expiry']._serialized_options = b'\x18\x01\xf2\xde\x1f yaml:"allow_update_after_expiry"'
    _CLIENTSTATE.fields_by_name['allow_update_after_misbehaviour']._options = None
    _CLIENTSTATE.fields_by_name['allow_update_after_misbehaviour']._serialized_options = b'\x18\x01\xf2\xde\x1f&yaml:"allow_update_after_misbehaviour"'
    _CLIENTSTATE._options = None
    _CLIENTSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _CONSENSUSSTATE.fields_by_name['timestamp']._options = None
    _CONSENSUSSTATE.fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _CONSENSUSSTATE.fields_by_name['root']._options = None
    _CONSENSUSSTATE.fields_by_name['root']._serialized_options = b'\xc8\xde\x1f\x00'
    _CONSENSUSSTATE.fields_by_name['next_validators_hash']._options = None
    _CONSENSUSSTATE.fields_by_name['next_validators_hash']._serialized_options = b'\xf2\xde\x1f\x1byaml:"next_validators_hash"\xfa\xde\x1f4github.com/tendermint/tendermint/libs/bytes.HexBytes'
    _CONSENSUSSTATE._options = None
    _CONSENSUSSTATE._serialized_options = b'\x88\xa0\x1f\x00'
    _MISBEHAVIOUR.fields_by_name['client_id']._options = None
    _MISBEHAVIOUR.fields_by_name['client_id']._serialized_options = b'\xf2\xde\x1f\x10yaml:"client_id"'
    _MISBEHAVIOUR.fields_by_name['header_1']._options = None
    _MISBEHAVIOUR.fields_by_name['header_1']._serialized_options = b'\xe2\xde\x1f\x07Header1\xf2\xde\x1f\x0fyaml:"header_1"'
    _MISBEHAVIOUR.fields_by_name['header_2']._options = None
    _MISBEHAVIOUR.fields_by_name['header_2']._serialized_options = b'\xe2\xde\x1f\x07Header2\xf2\xde\x1f\x0fyaml:"header_2"'
    _MISBEHAVIOUR._options = None
    _MISBEHAVIOUR._serialized_options = b'\x88\xa0\x1f\x00'
    _HEADER.fields_by_name['signed_header']._options = None
    _HEADER.fields_by_name['signed_header']._serialized_options = b'\xd0\xde\x1f\x01\xf2\xde\x1f\x14yaml:"signed_header"'
    _HEADER.fields_by_name['validator_set']._options = None
    _HEADER.fields_by_name['validator_set']._serialized_options = b'\xf2\xde\x1f\x14yaml:"validator_set"'
    _HEADER.fields_by_name['trusted_height']._options = None
    _HEADER.fields_by_name['trusted_height']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x15yaml:"trusted_height"'
    _HEADER.fields_by_name['trusted_validators']._options = None
    _HEADER.fields_by_name['trusted_validators']._serialized_options = b'\xf2\xde\x1f\x19yaml:"trusted_validators"'
    _globals['_CLIENTSTATE']._serialized_start = 323
    _globals['_CLIENTSTATE']._serialized_end = 1151
    _globals['_CONSENSUSSTATE']._serialized_start = 1154
    _globals['_CONSENSUSSTATE']._serialized_end = 1408
    _globals['_MISBEHAVIOUR']._serialized_start = 1411
    _globals['_MISBEHAVIOUR']._serialized_end = 1652
    _globals['_HEADER']._serialized_start = 1655
    _globals['_HEADER']._serialized_end = 2003
    _globals['_FRACTION']._serialized_start = 2005
    _globals['_FRACTION']._serialized_end = 2055