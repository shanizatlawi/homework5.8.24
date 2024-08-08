from typing import List, Dict


def get_statistics(numbers: List[int]) -> Dict[str, float]:
    if not numbers:
        return {
            'average': 0,
            'maximum': None,
            'minimum': None,
            'count': 0,
            'sum': 0
        }

    stats = {
        'average': sum(numbers) / len(numbers),
        'maximum': max(numbers),
        'minimum': min(numbers),
        'count': len(numbers),
        'sum': sum(numbers)
    }
    return stats


# Example usage:
numbers = [10, 20, 30, 40, 50]
statistics = get_statistics(numbers)
print(statistics)
# Output: {'average': 30.0, 'maximum': 50, 'minimum': 10, 'count': 5, 'sum': 150}
