"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....ibc.core.channel.v1 import query_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_query__pb2

class QueryStub(object):
    """Query provides defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Channel = channel.unary_unary('/ibc.core.channel.v1.Query/Channel', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelResponse.FromString)
        self.Channels = channel.unary_unary('/ibc.core.channel.v1.Query/Channels', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsResponse.FromString)
        self.ConnectionChannels = channel.unary_unary('/ibc.core.channel.v1.Query/ConnectionChannels', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsResponse.FromString)
        self.ChannelClientState = channel.unary_unary('/ibc.core.channel.v1.Query/ChannelClientState', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateResponse.FromString)
        self.ChannelConsensusState = channel.unary_unary('/ibc.core.channel.v1.Query/ChannelConsensusState', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateResponse.FromString)
        self.PacketCommitment = channel.unary_unary('/ibc.core.channel.v1.Query/PacketCommitment', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentResponse.FromString)
        self.PacketCommitments = channel.unary_unary('/ibc.core.channel.v1.Query/PacketCommitments', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsResponse.FromString)
        self.PacketReceipt = channel.unary_unary('/ibc.core.channel.v1.Query/PacketReceipt', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptResponse.FromString)
        self.PacketAcknowledgement = channel.unary_unary('/ibc.core.channel.v1.Query/PacketAcknowledgement', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementResponse.FromString)
        self.PacketAcknowledgements = channel.unary_unary('/ibc.core.channel.v1.Query/PacketAcknowledgements', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsResponse.FromString)
        self.UnreceivedPackets = channel.unary_unary('/ibc.core.channel.v1.Query/UnreceivedPackets', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsResponse.FromString)
        self.UnreceivedAcks = channel.unary_unary('/ibc.core.channel.v1.Query/UnreceivedAcks', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksResponse.FromString)
        self.NextSequenceReceive = channel.unary_unary('/ibc.core.channel.v1.Query/NextSequenceReceive', request_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveRequest.SerializeToString, response_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveResponse.FromString)

class QueryServicer(object):
    """Query provides defines the gRPC querier service
    """

    def Channel(self, request, context):
        """Channel queries an IBC Channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Channels(self, request, context):
        """Channels queries all the IBC channels of a chain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectionChannels(self, request, context):
        """ConnectionChannels queries all the channels associated with a connection
        end.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelClientState(self, request, context):
        """ChannelClientState queries for the client state for the channel associated
        with the provided channel identifiers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChannelConsensusState(self, request, context):
        """ChannelConsensusState queries for the consensus state for the channel
        associated with the provided channel identifiers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PacketCommitment(self, request, context):
        """PacketCommitment queries a stored packet commitment hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PacketCommitments(self, request, context):
        """PacketCommitments returns all the packet commitments hashes associated
        with a channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PacketReceipt(self, request, context):
        """PacketReceipt queries if a given packet sequence has been received on the
        queried chain
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PacketAcknowledgement(self, request, context):
        """PacketAcknowledgement queries a stored packet acknowledgement hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PacketAcknowledgements(self, request, context):
        """PacketAcknowledgements returns all the packet acknowledgements associated
        with a channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnreceivedPackets(self, request, context):
        """UnreceivedPackets returns all the unreceived IBC packets associated with a
        channel and sequences.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UnreceivedAcks(self, request, context):
        """UnreceivedAcks returns all the unreceived IBC acknowledgements associated
        with a channel and sequences.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NextSequenceReceive(self, request, context):
        """NextSequenceReceive returns the next receive sequence for a given channel.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Channel': grpc.unary_unary_rpc_method_handler(servicer.Channel, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelResponse.SerializeToString), 'Channels': grpc.unary_unary_rpc_method_handler(servicer.Channels, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsResponse.SerializeToString), 'ConnectionChannels': grpc.unary_unary_rpc_method_handler(servicer.ConnectionChannels, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsResponse.SerializeToString), 'ChannelClientState': grpc.unary_unary_rpc_method_handler(servicer.ChannelClientState, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateResponse.SerializeToString), 'ChannelConsensusState': grpc.unary_unary_rpc_method_handler(servicer.ChannelConsensusState, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateResponse.SerializeToString), 'PacketCommitment': grpc.unary_unary_rpc_method_handler(servicer.PacketCommitment, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentResponse.SerializeToString), 'PacketCommitments': grpc.unary_unary_rpc_method_handler(servicer.PacketCommitments, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsResponse.SerializeToString), 'PacketReceipt': grpc.unary_unary_rpc_method_handler(servicer.PacketReceipt, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptResponse.SerializeToString), 'PacketAcknowledgement': grpc.unary_unary_rpc_method_handler(servicer.PacketAcknowledgement, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementResponse.SerializeToString), 'PacketAcknowledgements': grpc.unary_unary_rpc_method_handler(servicer.PacketAcknowledgements, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsResponse.SerializeToString), 'UnreceivedPackets': grpc.unary_unary_rpc_method_handler(servicer.UnreceivedPackets, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsResponse.SerializeToString), 'UnreceivedAcks': grpc.unary_unary_rpc_method_handler(servicer.UnreceivedAcks, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksResponse.SerializeToString), 'NextSequenceReceive': grpc.unary_unary_rpc_method_handler(servicer.NextSequenceReceive, request_deserializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveRequest.FromString, response_serializer=ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('ibc.core.channel.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query provides defines the gRPC querier service
    """

    @staticmethod
    def Channel(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/Channel', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Channels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/Channels', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConnectionChannels(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/ConnectionChannels', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryConnectionChannelsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelClientState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/ChannelClientState', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelClientStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ChannelConsensusState(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/ChannelConsensusState', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryChannelConsensusStateResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PacketCommitment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/PacketCommitment', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PacketCommitments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/PacketCommitments', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketCommitmentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PacketReceipt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/PacketReceipt', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketReceiptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PacketAcknowledgement(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/PacketAcknowledgement', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PacketAcknowledgements(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/PacketAcknowledgements', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryPacketAcknowledgementsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnreceivedPackets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/UnreceivedPackets', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedPacketsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UnreceivedAcks(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/UnreceivedAcks', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryUnreceivedAcksResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NextSequenceReceive(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ibc.core.channel.v1.Query/NextSequenceReceive', ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveRequest.SerializeToString, ibc_dot_core_dot_channel_dot_v1_dot_query__pb2.QueryNextSequenceReceiveResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)