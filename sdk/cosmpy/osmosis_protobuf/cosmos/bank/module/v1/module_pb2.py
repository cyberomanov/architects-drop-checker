"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/bank/module/v1/module.proto\x12\x15cosmos.bank.module.v1\x1a cosmos/app/v1alpha1/module.proto"r\n\x06Module\x12(\n blocked_module_accounts_override\x18\x01 \x03(\t\x12\x11\n\tauthority\x18\x02 \x01(\t:+\xba\xc0\x96\xda\x01%\n#github.com/cosmos/cosmos-sdk/x/bankb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.bank.module.v1.module_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _MODULE._options = None
    _MODULE._serialized_options = b'\xba\xc0\x96\xda\x01%\n#github.com/cosmos/cosmos-sdk/x/bank'
    _globals['_MODULE']._serialized_start = 95
    _globals['_MODULE']._serialized_end = 209