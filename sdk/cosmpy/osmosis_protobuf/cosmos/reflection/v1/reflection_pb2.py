"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from ....cosmos.query.v1 import query_pb2 as cosmos_dot_query_dot_v1_dot_query__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/reflection/v1/reflection.proto\x12\x14cosmos.reflection.v1\x1a google/protobuf/descriptor.proto\x1a\x1bcosmos/query/v1/query.proto"\x18\n\x16FileDescriptorsRequest"N\n\x17FileDescriptorsResponse\x123\n\x05files\x18\x01 \x03(\x0b2$.google.protobuf.FileDescriptorProto2\x8a\x01\n\x11ReflectionService\x12u\n\x0fFileDescriptors\x12,.cosmos.reflection.v1.FileDescriptorsRequest\x1a-.cosmos.reflection.v1.FileDescriptorsResponse"\x05\x88\xe7\xb0*\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.reflection.v1.reflection_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _REFLECTIONSERVICE.methods_by_name['FileDescriptors']._options = None
    _REFLECTIONSERVICE.methods_by_name['FileDescriptors']._serialized_options = b'\x88\xe7\xb0*\x00'
    _globals['_FILEDESCRIPTORSREQUEST']._serialized_start = 126
    _globals['_FILEDESCRIPTORSREQUEST']._serialized_end = 150
    _globals['_FILEDESCRIPTORSRESPONSE']._serialized_start = 152
    _globals['_FILEDESCRIPTORSRESPONSE']._serialized_end = 230
    _globals['_REFLECTIONSERVICE']._serialized_start = 233
    _globals['_REFLECTIONSERVICE']._serialized_end = 371