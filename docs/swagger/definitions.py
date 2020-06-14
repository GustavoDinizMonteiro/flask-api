definitions = {
    'Book': {
        'type': 'object',
        'properties': {
            'id': { 'type': 'integer' },
            'title': { 'type': 'string' },
            'description': { 'type': 'string' },
            'author': { 'type': 'string' },
            'deleted': { 'type': 'boolean', 'default': False },
            'timestamp': { 'type': 'string', 'default': 'timestamp' },
            'category_id': { 'type': 'integer' },
            'category': {
                '$ref': '#/definitions/Category'
            },
            'comments': {
                'type': 'array',
                'items': {
                    '$ref': '#/definitions/Comment'
                }
            }
        }
    },
    'Category': {
        'type': 'object',
        'properties': {
            'id': { 'type': 'integer' },
            'name': { 'type': 'string' },
        }
    },
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
}