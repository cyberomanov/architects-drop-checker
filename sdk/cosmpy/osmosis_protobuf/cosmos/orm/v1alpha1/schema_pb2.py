"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n cosmos/orm/v1alpha1/schema.proto\x12\x13cosmos.orm.v1alpha1\x1a google/protobuf/descriptor.proto"\xde\x01\n\x16ModuleSchemaDescriptor\x12J\n\x0bschema_file\x18\x01 \x03(\x0b25.cosmos.orm.v1alpha1.ModuleSchemaDescriptor.FileEntry\x12\x0e\n\x06prefix\x18\x02 \x01(\x0c\x1ah\n\tFileEntry\x12\n\n\x02id\x18\x01 \x01(\r\x12\x17\n\x0fproto_file_name\x18\x02 \x01(\t\x126\n\x0cstorage_type\x18\x03 \x01(\x0e2 .cosmos.orm.v1alpha1.StorageType*\x9d\x01\n\x0bStorageType\x12$\n STORAGE_TYPE_DEFAULT_UNSPECIFIED\x10\x00\x12\x17\n\x13STORAGE_TYPE_MEMORY\x10\x01\x12\x1a\n\x16STORAGE_TYPE_TRANSIENT\x10\x02\x12\x16\n\x12STORAGE_TYPE_INDEX\x10\x03\x12\x1b\n\x17STORAGE_TYPE_COMMITMENT\x10\x04:f\n\rmodule_schema\x12\x1f.google.protobuf.MessageOptions\x18\xf0\xb3\xea1 \x01(\x0b2+.cosmos.orm.v1alpha1.ModuleSchemaDescriptorb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.orm.v1alpha1.schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(module_schema)
    DESCRIPTOR._options = None
    _globals['_STORAGETYPE']._serialized_start = 317
    _globals['_STORAGETYPE']._serialized_end = 474
    _globals['_MODULESCHEMADESCRIPTOR']._serialized_start = 92
    _globals['_MODULESCHEMADESCRIPTOR']._serialized_end = 314
    _globals['_MODULESCHEMADESCRIPTOR_FILEENTRY']._serialized_start = 210
    _globals['_MODULESCHEMADESCRIPTOR_FILEENTRY']._serialized_end = 314