def perform_action(action):
 match action:
    case 'add':
        return 'Adding item'
    case 'delete':
        return 'Deleting item'
    case 'update':
        return 'Updating item'
    case _:
        return 'Unknown action'
        result = perform_action('add')
        print(result) # Output: Adding item




def perform_action(action):
    actions = {
        'add': 'Adding item',
        'delete': 'Deleting item',
        'update': 'Updating item'
    }
    return actions.get(action, 'Unknown action')




result = perform_action('add')
print(result)  # Output: Adding item

