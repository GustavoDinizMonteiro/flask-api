from .definitions import definitions

list_specs = {
  'tags': ['category'],
  'parameters': [],
  'definitions': {
    **definitions
  },
  'responses': {
    '200': {
      'description': 'List of all categories.',
      'schema': {
        'type': 'array',
        'items': {
          '$ref': '#/definitions/Category'
        }
      }
    }
  }
}