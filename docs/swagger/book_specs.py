from .definitions import definitions

create_specs = {
    'tags': ['book'],
    'parameters': [{
        'name': 'body',
        'in': 'body',
        'schema': {
            'required': ['title', 'description', 'author'],
            'properties': {
                'title': {'type': 'string'},
                'description': {'type': 'string'},
                'author': {'type': 'string'},
            }
        }
  }],
  'definitions': {
      **definitions
  },
  'responses': {
      '200': {
          'description': 'Created book',
          'schema': {
              '$ref': '#/definitions/Book'
          }
      }
  }
}

list_specs = {
  'tags': ['book'],
  'parameters': [],
  'definitions': {
      **definitions
  },
  'responses': {
    '200': {
      'description': 'List of all books.',
      'schema': {
        'type': 'array',
        'items': {
          '$ref': '#/definitions/Book'
        }
      }
    }
  }
}