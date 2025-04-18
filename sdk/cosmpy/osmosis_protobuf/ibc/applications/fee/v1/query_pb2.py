"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from .....ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from .....ibc.applications.fee.v1 import genesis_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_genesis__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#ibc/applications/fee/v1/query.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a%ibc/applications/fee/v1/genesis.proto\x1a!ibc/core/channel/v1/channel.proto"s\n\x1fQueryIncentivizedPacketsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"u\n QueryIncentivizedPacketsResponse\x12Q\n\x14incentivized_packets\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00"n\n\x1eQueryIncentivizedPacketRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"s\n\x1fQueryIncentivizedPacketResponse\x12P\n\x13incentivized_packet\x18\x01 \x01(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x04\xc8\xde\x1f\x00"\xa2\x01\n)QueryIncentivizedPacketsForChannelRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x0f\n\x07port_id\x18\x02 \x01(\t\x12\x12\n\nchannel_id\x18\x03 \x01(\t\x12\x14\n\x0cquery_height\x18\x04 \x01(\x04"y\n*QueryIncentivizedPacketsForChannelResponse\x12K\n\x14incentivized_packets\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFees"S\n\x19QueryTotalRecvFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x90\x01\n\x1aQueryTotalRecvFeesResponse\x12r\n\trecv_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"recv_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"R\n\x18QueryTotalAckFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x8d\x01\n\x19QueryTotalAckFeesResponse\x12p\n\x08ack_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBC\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"ack_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"V\n\x1cQueryTotalTimeoutFeesRequest\x126\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x04\xc8\xde\x1f\x00"\x99\x01\n\x1dQueryTotalTimeoutFeesResponse\x12x\n\x0ctimeout_fees\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBG\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"timeout_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"O\n\x11QueryPayeeRequest\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x0f\n\x07relayer\x18\x02 \x01(\t"E\n\x12QueryPayeeResponse\x12/\n\rpayee_address\x18\x01 \x01(\tB\x18\xf2\xde\x1f\x14yaml:"payee_address""[\n\x1dQueryCounterpartyPayeeRequest\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x0f\n\x07relayer\x18\x02 \x01(\t"[\n\x1eQueryCounterpartyPayeeResponse\x129\n\x12counterparty_payee\x18\x01 \x01(\tB\x1d\xf2\xde\x1f\x19yaml:"counterparty_payee""r\n\x1eQueryFeeEnabledChannelsRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x12\x14\n\x0cquery_height\x18\x02 \x01(\x04"\x90\x01\n\x1fQueryFeeEnabledChannelsResponse\x12m\n\x14fee_enabled_channels\x18\x01 \x03(\x0b2*.ibc.applications.fee.v1.FeeEnabledChannelB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"fee_enabled_channels""o\n\x1dQueryFeeEnabledChannelRequest\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""M\n\x1eQueryFeeEnabledChannelResponse\x12+\n\x0bfee_enabled\x18\x01 \x01(\x08B\x16\xf2\xde\x1f\x12yaml:"fee_enabled"2\xe6\x11\n\x05Query\x12\xb9\x01\n\x13IncentivizedPackets\x128.ibc.applications.fee.v1.QueryIncentivizedPacketsRequest\x1a9.ibc.applications.fee.v1.QueryIncentivizedPacketsResponse"-\x82\xd3\xe4\x93\x02\'\x12%/ibc/apps/fee/v1/incentivized_packets\x12\x8f\x02\n\x12IncentivizedPacket\x127.ibc.applications.fee.v1.QueryIncentivizedPacketRequest\x1a8.ibc.applications.fee.v1.QueryIncentivizedPacketResponse"\x85\x01\x82\xd3\xe4\x93\x02\x7f\x12}/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/incentivized_packet\x12\xfd\x01\n\x1dIncentivizedPacketsForChannel\x12B.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelRequest\x1aC.ibc.applications.fee.v1.QueryIncentivizedPacketsForChannelResponse"S\x82\xd3\xe4\x93\x02M\x12K/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/incentivized_packets\x12\xfc\x01\n\rTotalRecvFees\x122.ibc.applications.fee.v1.QueryTotalRecvFeesRequest\x1a3.ibc.applications.fee.v1.QueryTotalRecvFeesResponse"\x81\x01\x82\xd3\xe4\x93\x02{\x12y/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_recv_fees\x12\xf8\x01\n\x0cTotalAckFees\x121.ibc.applications.fee.v1.QueryTotalAckFeesRequest\x1a2.ibc.applications.fee.v1.QueryTotalAckFeesResponse"\x80\x01\x82\xd3\xe4\x93\x02z\x12x/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_ack_fees\x12\x88\x02\n\x10TotalTimeoutFees\x125.ibc.applications.fee.v1.QueryTotalTimeoutFeesRequest\x1a6.ibc.applications.fee.v1.QueryTotalTimeoutFeesResponse"\x84\x01\x82\xd3\xe4\x93\x02~\x12|/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_timeout_fees\x12\xa9\x01\n\x05Payee\x12*.ibc.applications.fee.v1.QueryPayeeRequest\x1a+.ibc.applications.fee.v1.QueryPayeeResponse"G\x82\xd3\xe4\x93\x02A\x12?/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/payee\x12\xda\x01\n\x11CounterpartyPayee\x126.ibc.applications.fee.v1.QueryCounterpartyPayeeRequest\x1a7.ibc.applications.fee.v1.QueryCounterpartyPayeeResponse"T\x82\xd3\xe4\x93\x02N\x12L/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/counterparty_payee\x12\xad\x01\n\x12FeeEnabledChannels\x127.ibc.applications.fee.v1.QueryFeeEnabledChannelsRequest\x1a8.ibc.applications.fee.v1.QueryFeeEnabledChannelsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/fee/v1/fee_enabled\x12\xd0\x01\n\x11FeeEnabledChannel\x126.ibc.applications.fee.v1.QueryFeeEnabledChannelRequest\x1a7.ibc.applications.fee.v1.QueryFeeEnabledChannelResponse"J\x82\xd3\xe4\x93\x02D\x12B/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/fee_enabledB7Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/types'
    _QUERYINCENTIVIZEDPACKETSRESPONSE.fields_by_name['incentivized_packets']._options = None
    _QUERYINCENTIVIZEDPACKETSRESPONSE.fields_by_name['incentivized_packets']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINCENTIVIZEDPACKETREQUEST.fields_by_name['packet_id']._options = None
    _QUERYINCENTIVIZEDPACKETREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYINCENTIVIZEDPACKETRESPONSE.fields_by_name['incentivized_packet']._options = None
    _QUERYINCENTIVIZEDPACKETRESPONSE.fields_by_name['incentivized_packet']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALRECVFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALRECVFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALRECVFEESRESPONSE.fields_by_name['recv_fees']._options = None
    _QUERYTOTALRECVFEESRESPONSE.fields_by_name['recv_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"recv_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALACKFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALACKFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALACKFEESRESPONSE.fields_by_name['ack_fees']._options = None
    _QUERYTOTALACKFEESRESPONSE.fields_by_name['ack_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"ack_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYTOTALTIMEOUTFEESREQUEST.fields_by_name['packet_id']._options = None
    _QUERYTOTALTIMEOUTFEESREQUEST.fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _QUERYTOTALTIMEOUTFEESRESPONSE.fields_by_name['timeout_fees']._options = None
    _QUERYTOTALTIMEOUTFEESRESPONSE.fields_by_name['timeout_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"timeout_fees"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _QUERYPAYEEREQUEST.fields_by_name['channel_id']._options = None
    _QUERYPAYEEREQUEST.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _QUERYPAYEERESPONSE.fields_by_name['payee_address']._options = None
    _QUERYPAYEERESPONSE.fields_by_name['payee_address']._serialized_options = b'\xf2\xde\x1f\x14yaml:"payee_address"'
    _QUERYCOUNTERPARTYPAYEEREQUEST.fields_by_name['channel_id']._options = None
    _QUERYCOUNTERPARTYPAYEEREQUEST.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _QUERYCOUNTERPARTYPAYEERESPONSE.fields_by_name['counterparty_payee']._options = None
    _QUERYCOUNTERPARTYPAYEERESPONSE.fields_by_name['counterparty_payee']._serialized_options = b'\xf2\xde\x1f\x19yaml:"counterparty_payee"'
    _QUERYFEEENABLEDCHANNELSRESPONSE.fields_by_name['fee_enabled_channels']._options = None
    _QUERYFEEENABLEDCHANNELSRESPONSE.fields_by_name['fee_enabled_channels']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"fee_enabled_channels"'
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['port_id']._options = None
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['channel_id']._options = None
    _QUERYFEEENABLEDCHANNELREQUEST.fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _QUERYFEEENABLEDCHANNELRESPONSE.fields_by_name['fee_enabled']._options = None
    _QUERYFEEENABLEDCHANNELRESPONSE.fields_by_name['fee_enabled']._serialized_options = b'\xf2\xde\x1f\x12yaml:"fee_enabled"'
    _QUERY.methods_by_name['IncentivizedPackets']._options = None
    _QUERY.methods_by_name['IncentivizedPackets']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/ibc/apps/fee/v1/incentivized_packets"
    _QUERY.methods_by_name['IncentivizedPacket']._options = None
    _QUERY.methods_by_name['IncentivizedPacket']._serialized_options = b'\x82\xd3\xe4\x93\x02\x7f\x12}/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/incentivized_packet'
    _QUERY.methods_by_name['IncentivizedPacketsForChannel']._options = None
    _QUERY.methods_by_name['IncentivizedPacketsForChannel']._serialized_options = b'\x82\xd3\xe4\x93\x02M\x12K/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/incentivized_packets'
    _QUERY.methods_by_name['TotalRecvFees']._options = None
    _QUERY.methods_by_name['TotalRecvFees']._serialized_options = b'\x82\xd3\xe4\x93\x02{\x12y/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_recv_fees'
    _QUERY.methods_by_name['TotalAckFees']._options = None
    _QUERY.methods_by_name['TotalAckFees']._serialized_options = b'\x82\xd3\xe4\x93\x02z\x12x/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_ack_fees'
    _QUERY.methods_by_name['TotalTimeoutFees']._options = None
    _QUERY.methods_by_name['TotalTimeoutFees']._serialized_options = b'\x82\xd3\xe4\x93\x02~\x12|/ibc/apps/fee/v1/channels/{packet_id.channel_id}/ports/{packet_id.port_id}/sequences/{packet_id.sequence}/total_timeout_fees'
    _QUERY.methods_by_name['Payee']._options = None
    _QUERY.methods_by_name['Payee']._serialized_options = b'\x82\xd3\xe4\x93\x02A\x12?/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/payee'
    _QUERY.methods_by_name['CounterpartyPayee']._options = None
    _QUERY.methods_by_name['CounterpartyPayee']._serialized_options = b'\x82\xd3\xe4\x93\x02N\x12L/ibc/apps/fee/v1/channels/{channel_id}/relayers/{relayer}/counterparty_payee'
    _QUERY.methods_by_name['FeeEnabledChannels']._options = None
    _QUERY.methods_by_name['FeeEnabledChannels']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/ibc/apps/fee/v1/fee_enabled'
    _QUERY.methods_by_name['FeeEnabledChannel']._options = None
    _QUERY.methods_by_name['FeeEnabledChannel']._serialized_options = b'\x82\xd3\xe4\x93\x02D\x12B/ibc/apps/fee/v1/channels/{channel_id}/ports/{port_id}/fee_enabled'
    _globals['_QUERYINCENTIVIZEDPACKETSREQUEST']._serialized_start = 301
    _globals['_QUERYINCENTIVIZEDPACKETSREQUEST']._serialized_end = 416
    _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE']._serialized_start = 418
    _globals['_QUERYINCENTIVIZEDPACKETSRESPONSE']._serialized_end = 535
    _globals['_QUERYINCENTIVIZEDPACKETREQUEST']._serialized_start = 537
    _globals['_QUERYINCENTIVIZEDPACKETREQUEST']._serialized_end = 647
    _globals['_QUERYINCENTIVIZEDPACKETRESPONSE']._serialized_start = 649
    _globals['_QUERYINCENTIVIZEDPACKETRESPONSE']._serialized_end = 764
    _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST']._serialized_start = 767
    _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELREQUEST']._serialized_end = 929
    _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE']._serialized_start = 931
    _globals['_QUERYINCENTIVIZEDPACKETSFORCHANNELRESPONSE']._serialized_end = 1052
    _globals['_QUERYTOTALRECVFEESREQUEST']._serialized_start = 1054
    _globals['_QUERYTOTALRECVFEESREQUEST']._serialized_end = 1137
    _globals['_QUERYTOTALRECVFEESRESPONSE']._serialized_start = 1140
    _globals['_QUERYTOTALRECVFEESRESPONSE']._serialized_end = 1284
    _globals['_QUERYTOTALACKFEESREQUEST']._serialized_start = 1286
    _globals['_QUERYTOTALACKFEESREQUEST']._serialized_end = 1368
    _globals['_QUERYTOTALACKFEESRESPONSE']._serialized_start = 1371
    _globals['_QUERYTOTALACKFEESRESPONSE']._serialized_end = 1512
    _globals['_QUERYTOTALTIMEOUTFEESREQUEST']._serialized_start = 1514
    _globals['_QUERYTOTALTIMEOUTFEESREQUEST']._serialized_end = 1600
    _globals['_QUERYTOTALTIMEOUTFEESRESPONSE']._serialized_start = 1603
    _globals['_QUERYTOTALTIMEOUTFEESRESPONSE']._serialized_end = 1756
    _globals['_QUERYPAYEEREQUEST']._serialized_start = 1758
    _globals['_QUERYPAYEEREQUEST']._serialized_end = 1837
    _globals['_QUERYPAYEERESPONSE']._serialized_start = 1839
    _globals['_QUERYPAYEERESPONSE']._serialized_end = 1908
    _globals['_QUERYCOUNTERPARTYPAYEEREQUEST']._serialized_start = 1910
    _globals['_QUERYCOUNTERPARTYPAYEEREQUEST']._serialized_end = 2001
    _globals['_QUERYCOUNTERPARTYPAYEERESPONSE']._serialized_start = 2003
    _globals['_QUERYCOUNTERPARTYPAYEERESPONSE']._serialized_end = 2094
    _globals['_QUERYFEEENABLEDCHANNELSREQUEST']._serialized_start = 2096
    _globals['_QUERYFEEENABLEDCHANNELSREQUEST']._serialized_end = 2210
    _globals['_QUERYFEEENABLEDCHANNELSRESPONSE']._serialized_start = 2213
    _globals['_QUERYFEEENABLEDCHANNELSRESPONSE']._serialized_end = 2357
    _globals['_QUERYFEEENABLEDCHANNELREQUEST']._serialized_start = 2359
    _globals['_QUERYFEEENABLEDCHANNELREQUEST']._serialized_end = 2470
    _globals['_QUERYFEEENABLEDCHANNELRESPONSE']._serialized_start = 2472
    _globals['_QUERYFEEENABLEDCHANNELRESPONSE']._serialized_end = 2549
    _globals['_QUERY']._serialized_start = 2552
    _globals['_QUERY']._serialized_end = 4830