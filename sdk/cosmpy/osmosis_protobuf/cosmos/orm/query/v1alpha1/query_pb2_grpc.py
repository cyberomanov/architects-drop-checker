"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....cosmos.orm.query.v1alpha1 import query_pb2 as cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2

class QueryStub(object):
    """Query is a generic gRPC service for querying ORM data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary('/cosmos.orm.query.v1alpha1.Query/Get', request_serializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetRequest.SerializeToString, response_deserializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetResponse.FromString)
        self.List = channel.unary_unary('/cosmos.orm.query.v1alpha1.Query/List', request_serializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListRequest.SerializeToString, response_deserializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListResponse.FromString)

class QueryServicer(object):
    """Query is a generic gRPC service for querying ORM data.
    """

    def Get(self, request, context):
        """Get queries an ORM table against an unique index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List queries an ORM table against an index.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Get': grpc.unary_unary_rpc_method_handler(servicer.Get, request_deserializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetRequest.FromString, response_serializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetResponse.SerializeToString), 'List': grpc.unary_unary_rpc_method_handler(servicer.List, request_deserializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListRequest.FromString, response_serializer=cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.orm.query.v1alpha1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query is a generic gRPC service for querying ORM data.
    """

    @staticmethod
    def Get(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.orm.query.v1alpha1.Query/Get', cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetRequest.SerializeToString, cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.GetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.orm.query.v1alpha1.Query/List', cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListRequest.SerializeToString, cosmos_dot_orm_dot_query_dot_v1alpha1_dot_query__pb2.ListResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)