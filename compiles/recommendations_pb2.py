# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendations.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='recommendations.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15recommendations.proto\"_\n\x16RecommendationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x1f\n\x08\x63\x61tegory\x18\x02 \x01(\x0e\x32\r.BookCategory\x12\x13\n\x0bmax_results\x18\x03 \x01(\x05\"0\n\x13\x42ookRecommendations\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\"H\n\x17RecommendationsResponse\x12-\n\x0frecommendations\x18\x01 \x03(\x0b\x32\x14.BookRecommendations*?\n\x0c\x42ookCategory\x12\x0b\n\x07MYSTERY\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\r\n\tSELF_HELP\x10\x02\x32S\n\x0fRecommendations\x12@\n\tRecommend\x12\x17.RecommendationsRequest\x1a\x18.RecommendationsResponse\"\x00\x62\x06proto3'
)

_BOOKCATEGORY = _descriptor.EnumDescriptor(
  name='BookCategory',
  full_name='BookCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MYSTERY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCIENCE_FICTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SELF_HELP', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=246,
  serialized_end=309,
)
_sym_db.RegisterEnumDescriptor(_BOOKCATEGORY)

BookCategory = enum_type_wrapper.EnumTypeWrapper(_BOOKCATEGORY)
MYSTERY = 0
SCIENCE_FICTION = 1
SELF_HELP = 2



_RECOMMENDATIONSREQUEST = _descriptor.Descriptor(
  name='RecommendationsRequest',
  full_name='RecommendationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='RecommendationsRequest.user_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='RecommendationsRequest.category', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_results', full_name='RecommendationsRequest.max_results', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=120,
)


_BOOKRECOMMENDATIONS = _descriptor.Descriptor(
  name='BookRecommendations',
  full_name='BookRecommendations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='BookRecommendations.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='title', full_name='BookRecommendations.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=170,
)


_RECOMMENDATIONSRESPONSE = _descriptor.Descriptor(
  name='RecommendationsResponse',
  full_name='RecommendationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='recommendations', full_name='RecommendationsResponse.recommendations', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=244,
)

_RECOMMENDATIONSREQUEST.fields_by_name['category'].enum_type = _BOOKCATEGORY
_RECOMMENDATIONSRESPONSE.fields_by_name['recommendations'].message_type = _BOOKRECOMMENDATIONS
DESCRIPTOR.message_types_by_name['RecommendationsRequest'] = _RECOMMENDATIONSREQUEST
DESCRIPTOR.message_types_by_name['BookRecommendations'] = _BOOKRECOMMENDATIONS
DESCRIPTOR.message_types_by_name['RecommendationsResponse'] = _RECOMMENDATIONSRESPONSE
DESCRIPTOR.enum_types_by_name['BookCategory'] = _BOOKCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendationsRequest = _reflection.GeneratedProtocolMessageType('RecommendationsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONSREQUEST,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:RecommendationsRequest)
  })
_sym_db.RegisterMessage(RecommendationsRequest)

BookRecommendations = _reflection.GeneratedProtocolMessageType('BookRecommendations', (_message.Message,), {
  'DESCRIPTOR' : _BOOKRECOMMENDATIONS,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:BookRecommendations)
  })
_sym_db.RegisterMessage(BookRecommendations)

RecommendationsResponse = _reflection.GeneratedProtocolMessageType('RecommendationsResponse', (_message.Message,), {
  'DESCRIPTOR' : _RECOMMENDATIONSRESPONSE,
  '__module__' : 'recommendations_pb2'
  # @@protoc_insertion_point(class_scope:RecommendationsResponse)
  })
_sym_db.RegisterMessage(RecommendationsResponse)



_RECOMMENDATIONS = _descriptor.ServiceDescriptor(
  name='Recommendations',
  full_name='Recommendations',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=311,
  serialized_end=394,
  methods=[
  _descriptor.MethodDescriptor(
    name='Recommend',
    full_name='Recommendations.Recommend',
    index=0,
    containing_service=None,
    input_type=_RECOMMENDATIONSREQUEST,
    output_type=_RECOMMENDATIONSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RECOMMENDATIONS)

DESCRIPTOR.services_by_name['Recommendations'] = _RECOMMENDATIONS

# @@protoc_insertion_point(module_scope)
