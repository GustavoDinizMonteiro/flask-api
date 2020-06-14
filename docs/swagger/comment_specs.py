create_specs = {
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
        'author': { 'type': 'string' },
        'body': { 'type': 'string' },
      }
    }
  }],
  'definitions': {
    'Comment': {
      'type': 'object',
      'properties': {
        'id': { 'type': 'integer' },
        'author': { 'type': 'string' },
        'body': { 'type': 'string' },
        'deleted': { 'type': 'boolean', 'default': False },
        'timestamp': { 'type': 'string', 'default': 'timestamp' }
      }
    }
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