# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import bfd_service_pb2 as bfd__service__pb2


class BFDStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Initialize = channel.unary_unary(
                '/bfd.BFD/Initialize',
                request_serializer=bfd__service__pb2.InitializeRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.InitializeResponse.FromString,
                )
        self.SessionAdd = channel.unary_unary(
                '/bfd.BFD/SessionAdd',
                request_serializer=bfd__service__pb2.SessionRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.SessionOperationResponse.FromString,
                )
        self.SessionUpdate = channel.unary_unary(
                '/bfd.BFD/SessionUpdate',
                request_serializer=bfd__service__pb2.SessionRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.SessionOperationResponse.FromString,
                )
        self.SessionDelete = channel.unary_unary(
                '/bfd.BFD/SessionDelete',
                request_serializer=bfd__service__pb2.SessionRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.SessionOperationResponse.FromString,
                )
        self.SessionDeleteAll = channel.unary_unary(
                '/bfd.BFD/SessionDeleteAll',
                request_serializer=bfd__service__pb2.DeleteAllRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.SessionOperationResponse.FromString,
                )
        self.Subscribe = channel.unary_stream(
                '/bfd.BFD/Subscribe',
                request_serializer=bfd__service__pb2.SubscribeRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.EventResponse.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/bfd.BFD/Unsubscribe',
                request_serializer=bfd__service__pb2.UnsubscribeRequest.SerializeToString,
                response_deserializer=bfd__service__pb2.UnsubscribeResponse.FromString,
                )


class BFDServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Initialize(self, request, context):
        """*
        Must be invoked before invoking any other BFD service APIs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionAdd(self, request, context):
        """*
        Add a new BFD session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionUpdate(self, request, context):
        """*
        Modify an existing BFD session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionDelete(self, request, context):
        """*
        Delete an existing BFD session.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SessionDeleteAll(self, request, context):
        """*
        Deletes all BFD sessions owned by this client. Useful to cleanup
        after a disconnect and reconnect to reset the state.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Subscribe(self, request, context):
        """*
        Subscribe for BFD session event notifications.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """*
        UnSubscribe for BFD session event notifications.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BFDServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Initialize': grpc.unary_unary_rpc_method_handler(
                    servicer.Initialize,
                    request_deserializer=bfd__service__pb2.InitializeRequest.FromString,
                    response_serializer=bfd__service__pb2.InitializeResponse.SerializeToString,
            ),
            'SessionAdd': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionAdd,
                    request_deserializer=bfd__service__pb2.SessionRequest.FromString,
                    response_serializer=bfd__service__pb2.SessionOperationResponse.SerializeToString,
            ),
            'SessionUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionUpdate,
                    request_deserializer=bfd__service__pb2.SessionRequest.FromString,
                    response_serializer=bfd__service__pb2.SessionOperationResponse.SerializeToString,
            ),
            'SessionDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionDelete,
                    request_deserializer=bfd__service__pb2.SessionRequest.FromString,
                    response_serializer=bfd__service__pb2.SessionOperationResponse.SerializeToString,
            ),
            'SessionDeleteAll': grpc.unary_unary_rpc_method_handler(
                    servicer.SessionDeleteAll,
                    request_deserializer=bfd__service__pb2.DeleteAllRequest.FromString,
                    response_serializer=bfd__service__pb2.SessionOperationResponse.SerializeToString,
            ),
            'Subscribe': grpc.unary_stream_rpc_method_handler(
                    servicer.Subscribe,
                    request_deserializer=bfd__service__pb2.SubscribeRequest.FromString,
                    response_serializer=bfd__service__pb2.EventResponse.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=bfd__service__pb2.UnsubscribeRequest.FromString,
                    response_serializer=bfd__service__pb2.UnsubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bfd.BFD', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BFD(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Initialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/Initialize',
            bfd__service__pb2.InitializeRequest.SerializeToString,
            bfd__service__pb2.InitializeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionAdd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/SessionAdd',
            bfd__service__pb2.SessionRequest.SerializeToString,
            bfd__service__pb2.SessionOperationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/SessionUpdate',
            bfd__service__pb2.SessionRequest.SerializeToString,
            bfd__service__pb2.SessionOperationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/SessionDelete',
            bfd__service__pb2.SessionRequest.SerializeToString,
            bfd__service__pb2.SessionOperationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SessionDeleteAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/SessionDeleteAll',
            bfd__service__pb2.DeleteAllRequest.SerializeToString,
            bfd__service__pb2.SessionOperationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Subscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/bfd.BFD/Subscribe',
            bfd__service__pb2.SubscribeRequest.SerializeToString,
            bfd__service__pb2.EventResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bfd.BFD/Unsubscribe',
            bfd__service__pb2.UnsubscribeRequest.SerializeToString,
            bfd__service__pb2.UnsubscribeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
