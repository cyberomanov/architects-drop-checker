"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.staking.v1beta1 import staking_pb2 as cosmos_dot_staking_dot_v1beta1_dot_staking__pb2
from ....cosmos.msg.v1 import msg_pb2 as cosmos_dot_msg_dot_v1_dot_msg__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fcosmos/staking/v1beta1/tx.proto\x12\x16cosmos.staking.v1beta1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a$cosmos/staking/v1beta1/staking.proto\x1a\x17cosmos/msg/v1/msg.proto\x1a\x11amino/amino.proto"\xb3\x04\n\x12MsgCreateValidator\x12C\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12F\n\ncommission\x18\x02 \x01(\x0b2\'.cosmos.staking.v1beta1.CommissionRatesB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12Y\n\x13min_self_delegation\x18\x03 \x01(\tB<\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int\x123\n\x11delegator_address\x18\x04 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x05 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12>\n\x06pubkey\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB\x18\xca\xb4-\x14cosmos.crypto.PubKey\x123\n\x05value\x18\x07 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:V\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1dcosmos-sdk/MsgCreateValidator"\x1c\n\x1aMsgCreateValidatorResponse"\xf6\x02\n\x10MsgEditValidator\x12C\n\x0bdescription\x18\x01 \x01(\x0b2#.cosmos.staking.v1beta1.DescriptionB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12Q\n\x0fcommission_rate\x18\x03 \x01(\tB8\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec\x12U\n\x13min_self_delegation\x18\x04 \x01(\tB8\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int:>\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1bcosmos-sdk/MsgEditValidator"\x1a\n\x18MsgEditValidatorResponse"\xe8\x01\n\x0bMsgDelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:9\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x16cosmos-sdk/MsgDelegate"\x15\n\x13MsgDelegateResponse"\xb3\x02\n\x12MsgBeginRedelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_src_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x127\n\x15validator_dst_address\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x06amount\x18\x04 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:@\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x1dcosmos-sdk/MsgBeginRedelegate"`\n\x1aMsgBeginRedelegateResponse\x12B\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01"\xec\x01\n\rMsgUndelegate\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:;\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x18cosmos-sdk/MsgUndelegate"[\n\x15MsgUndelegateResponse\x12B\n\x0fcompletion_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01"\xa3\x02\n\x1cMsgCancelUnbondingDelegation\x123\n\x11delegator_address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x123\n\x11validator_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x124\n\x06amount\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12\x17\n\x0fcreation_height\x18\x04 \x01(\x03:J\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\'cosmos-sdk/MsgCancelUnbondingDelegation"&\n$MsgCancelUnbondingDelegationResponse"\xb2\x01\n\x0fMsgUpdateParams\x12+\n\tauthority\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x129\n\x06params\x18\x02 \x01(\x0b2\x1e.cosmos.staking.v1beta1.ParamsB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01:7\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$cosmos-sdk/x/staking/MsgUpdateParams"\x19\n\x17MsgUpdateParamsResponse2\x9d\x06\n\x03Msg\x12q\n\x0fCreateValidator\x12*.cosmos.staking.v1beta1.MsgCreateValidator\x1a2.cosmos.staking.v1beta1.MsgCreateValidatorResponse\x12k\n\rEditValidator\x12(.cosmos.staking.v1beta1.MsgEditValidator\x1a0.cosmos.staking.v1beta1.MsgEditValidatorResponse\x12\\\n\x08Delegate\x12#.cosmos.staking.v1beta1.MsgDelegate\x1a+.cosmos.staking.v1beta1.MsgDelegateResponse\x12q\n\x0fBeginRedelegate\x12*.cosmos.staking.v1beta1.MsgBeginRedelegate\x1a2.cosmos.staking.v1beta1.MsgBeginRedelegateResponse\x12b\n\nUndelegate\x12%.cosmos.staking.v1beta1.MsgUndelegate\x1a-.cosmos.staking.v1beta1.MsgUndelegateResponse\x12\x8f\x01\n\x19CancelUnbondingDelegation\x124.cosmos.staking.v1beta1.MsgCancelUnbondingDelegation\x1a<.cosmos.staking.v1beta1.MsgCancelUnbondingDelegationResponse\x12h\n\x0cUpdateParams\x12\'.cosmos.staking.v1beta1.MsgUpdateParams\x1a/.cosmos.staking.v1beta1.MsgUpdateParamsResponse\x1a\x05\x80\xe7\xb0*\x01B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _MSGCREATEVALIDATOR.fields_by_name['description']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGCREATEVALIDATOR.fields_by_name['commission']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['commission']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int'
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['pubkey']._serialized_options = b'\xca\xb4-\x14cosmos.crypto.PubKey'
    _MSGCREATEVALIDATOR.fields_by_name['value']._options = None
    _MSGCREATEVALIDATOR.fields_by_name['value']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGCREATEVALIDATOR._options = None
    _MSGCREATEVALIDATOR._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1dcosmos-sdk/MsgCreateValidator'
    _MSGEDITVALIDATOR.fields_by_name['description']._options = None
    _MSGEDITVALIDATOR.fields_by_name['description']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._options = None
    _MSGEDITVALIDATOR.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._options = None
    _MSGEDITVALIDATOR.fields_by_name['commission_rate']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\xd2\xb4-\ncosmos.Dec'
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._options = None
    _MSGEDITVALIDATOR.fields_by_name['min_self_delegation']._serialized_options = b'\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int\xd2\xb4-\ncosmos.Int'
    _MSGEDITVALIDATOR._options = None
    _MSGEDITVALIDATOR._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11validator_address\x8a\xe7\xb0*\x1bcosmos-sdk/MsgEditValidator'
    _MSGDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDELEGATE.fields_by_name['validator_address']._options = None
    _MSGDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGDELEGATE.fields_by_name['amount']._options = None
    _MSGDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGDELEGATE._options = None
    _MSGDELEGATE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x16cosmos-sdk/MsgDelegate'
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_src_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['validator_dst_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGBEGINREDELEGATE.fields_by_name['amount']._options = None
    _MSGBEGINREDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGBEGINREDELEGATE._options = None
    _MSGBEGINREDELEGATE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x1dcosmos-sdk/MsgBeginRedelegate'
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGBEGINREDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _MSGUNDELEGATE.fields_by_name['delegator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUNDELEGATE.fields_by_name['validator_address']._options = None
    _MSGUNDELEGATE.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUNDELEGATE.fields_by_name['amount']._options = None
    _MSGUNDELEGATE.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGUNDELEGATE._options = None
    _MSGUNDELEGATE._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*\x18cosmos-sdk/MsgUndelegate'
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._options = None
    _MSGUNDELEGATERESPONSE.fields_by_name['completion_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['delegator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['validator_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._options = None
    _MSGCANCELUNBONDINGDELEGATION.fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGCANCELUNBONDINGDELEGATION._options = None
    _MSGCANCELUNBONDINGDELEGATION._serialized_options = b"\x88\xa0\x1f\x00\xe8\xa0\x1f\x00\x82\xe7\xb0*\x11delegator_address\x8a\xe7\xb0*'cosmos-sdk/MsgCancelUnbondingDelegation"
    _MSGUPDATEPARAMS.fields_by_name['authority']._options = None
    _MSGUPDATEPARAMS.fields_by_name['authority']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _MSGUPDATEPARAMS.fields_by_name['params']._options = None
    _MSGUPDATEPARAMS.fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _MSGUPDATEPARAMS._options = None
    _MSGUPDATEPARAMS._serialized_options = b'\x82\xe7\xb0*\tauthority\x8a\xe7\xb0*$cosmos-sdk/x/staking/MsgUpdateParams'
    _MSG._options = None
    _MSG._serialized_options = b'\x80\xe7\xb0*\x01'
    _globals['_MSGCREATEVALIDATOR']._serialized_start = 283
    _globals['_MSGCREATEVALIDATOR']._serialized_end = 846
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_start = 848
    _globals['_MSGCREATEVALIDATORRESPONSE']._serialized_end = 876
    _globals['_MSGEDITVALIDATOR']._serialized_start = 879
    _globals['_MSGEDITVALIDATOR']._serialized_end = 1253
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_start = 1255
    _globals['_MSGEDITVALIDATORRESPONSE']._serialized_end = 1281
    _globals['_MSGDELEGATE']._serialized_start = 1284
    _globals['_MSGDELEGATE']._serialized_end = 1516
    _globals['_MSGDELEGATERESPONSE']._serialized_start = 1518
    _globals['_MSGDELEGATERESPONSE']._serialized_end = 1539
    _globals['_MSGBEGINREDELEGATE']._serialized_start = 1542
    _globals['_MSGBEGINREDELEGATE']._serialized_end = 1849
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_start = 1851
    _globals['_MSGBEGINREDELEGATERESPONSE']._serialized_end = 1947
    _globals['_MSGUNDELEGATE']._serialized_start = 1950
    _globals['_MSGUNDELEGATE']._serialized_end = 2186
    _globals['_MSGUNDELEGATERESPONSE']._serialized_start = 2188
    _globals['_MSGUNDELEGATERESPONSE']._serialized_end = 2279
    _globals['_MSGCANCELUNBONDINGDELEGATION']._serialized_start = 2282
    _globals['_MSGCANCELUNBONDINGDELEGATION']._serialized_end = 2573
    _globals['_MSGCANCELUNBONDINGDELEGATIONRESPONSE']._serialized_start = 2575
    _globals['_MSGCANCELUNBONDINGDELEGATIONRESPONSE']._serialized_end = 2613
    _globals['_MSGUPDATEPARAMS']._serialized_start = 2616
    _globals['_MSGUPDATEPARAMS']._serialized_end = 2794
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 2796
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 2821
    _globals['_MSG']._serialized_start = 2824
    _globals['_MSG']._serialized_end = 3621