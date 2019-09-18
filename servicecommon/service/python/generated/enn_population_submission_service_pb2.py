import servicecommon.service.python.generated.population_structs_pb2 as population__structs__pb2
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enn_population_submission_service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='enn_population_submission_service.proto',
  package='enn',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'enn_population_submission_service.proto\x12\x03\x65nn\x1a\x18population_structs.proto2\xcd\x01\n\x1e\x45nnPopulationSubmissionService\x12Q\n\x0eNextPopulation\x12\x1d.population.PopulationRequest\x1a\x1e.population.PopulationResponse\"\x00\x12X\n\rGetPopulation\x12%.population.ExistingPopulationRequest\x1a\x1e.population.PopulationResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[population__structs__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_ENNPOPULATIONSUBMISSIONSERVICE = _descriptor.ServiceDescriptor(
  name='EnnPopulationSubmissionService',
  full_name='enn.EnnPopulationSubmissionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=75,
  serialized_end=280,
  methods=[
  _descriptor.MethodDescriptor(
    name='NextPopulation',
    full_name='enn.EnnPopulationSubmissionService.NextPopulation',
    index=0,
    containing_service=None,
    input_type=population__structs__pb2._POPULATIONREQUEST,
    output_type=population__structs__pb2._POPULATIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetPopulation',
    full_name='enn.EnnPopulationSubmissionService.GetPopulation',
    index=1,
    containing_service=None,
    input_type=population__structs__pb2._EXISTINGPOPULATIONREQUEST,
    output_type=population__structs__pb2._POPULATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ENNPOPULATIONSUBMISSIONSERVICE)

DESCRIPTOR.services_by_name['EnnPopulationSubmissionService'] = _ENNPOPULATIONSUBMISSIONSERVICE

# @@protoc_insertion_point(module_scope)
