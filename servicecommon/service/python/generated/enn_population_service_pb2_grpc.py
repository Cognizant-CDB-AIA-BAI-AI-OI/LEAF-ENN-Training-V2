import servicecommon.service.python.generated.population_structs_pb2 as population__structs__pb2

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc



class EnnPopulationServiceStub(object):
  """
  The service definition for a generic population server.

  If creating a population can take longer than 30-45 seconds,
  Some implementations of a population service might require an
  implemenation of a Submission service also with the same API.

  The Submission Service has the same interface as the underlying
  Population Service.  It will call the underlying Population Service
  to ask it to create a population, but since this can take awhile,
  this service returns early with information as to how further updates can
  be obtained via subsequent GetPopulation() calls: an "Is it there yet?" poll.
  This allows the long (> 1 min) idle sockets to close with service work
  still proceeding.

  Even though the Submission Service has the same interface as the
  Population Service itself, you would need to define a separate service
  for it so requests can be routed differently within the service cluster.

  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.NextPopulation = channel.unary_unary(
        '/enn.EnnPopulationService/NextPopulation',
        request_serializer=population__structs__pb2.PopulationRequest.SerializeToString,
        response_deserializer=population__structs__pb2.PopulationResponse.FromString,
        )
    self.GetPopulation = channel.unary_unary(
        '/enn.EnnPopulationService/GetPopulation',
        request_serializer=population__structs__pb2.ExistingPopulationRequest.SerializeToString,
        response_deserializer=population__structs__pb2.PopulationResponse.FromString,
        )


class EnnPopulationServiceServicer(object):
  """
  The service definition for a generic population server.

  If creating a population can take longer than 30-45 seconds,
  Some implementations of a population service might require an
  implemenation of a Submission service also with the same API.

  The Submission Service has the same interface as the underlying
  Population Service.  It will call the underlying Population Service
  to ask it to create a population, but since this can take awhile,
  this service returns early with information as to how further updates can
  be obtained via subsequent GetPopulation() calls: an "Is it there yet?" poll.
  This allows the long (> 1 min) idle sockets to close with service work
  still proceeding.

  Even though the Submission Service has the same interface as the
  Population Service itself, you would need to define a separate service
  for it so requests can be routed differently within the service cluster.

  """

  def NextPopulation(self, request, context):
    """Returns an initial or new generation specification
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPopulation(self, request, context):
    """Returns an existing population of the experiment
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EnnPopulationServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'NextPopulation': grpc.unary_unary_rpc_method_handler(
          servicer.NextPopulation,
          request_deserializer=population__structs__pb2.PopulationRequest.FromString,
          response_serializer=population__structs__pb2.PopulationResponse.SerializeToString,
      ),
      'GetPopulation': grpc.unary_unary_rpc_method_handler(
          servicer.GetPopulation,
          request_deserializer=population__structs__pb2.ExistingPopulationRequest.FromString,
          response_serializer=population__structs__pb2.PopulationResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'enn.EnnPopulationService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
