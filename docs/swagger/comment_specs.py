from .definitions import definitions

create_specs = {
  'tags': ['book', 'comment'],
  'parameters': [{
    'name': 'book_id',
    'in': 'path',
    'type': 'int',
    'required': 'true'
  },{
    'name': 'body',
    'in': 'body',
    'schema': {
      'required': ['author', 'body'],
      'properties': {
        'author': {'type': 'string'},
        'body': {'type': 'string'},
      }
    }
  }],
  'definitions': {
    **definitions
  },
  'responses': {
    '200': {
      'description': 'Created comment',
      'schema': {
        '$ref': '#/definitions/Comment'
      }
    }
  }
}