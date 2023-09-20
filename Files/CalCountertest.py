import re
import pytest
import types
import inspect
from conftest import Capturing


try:
    import workout_tracker
except ModuleNotFoundError:
    assert False, 'File for homework `workout_tracker.py` not found'
except NameError as exc:
    name = re.findall("name '(\w+)' is not defined", str(exc))[0]
    assert False, f'Class {name} not found in the homework file.'
except ImportError:
    assert False, 'File for homework `workout_tracker.py` not found'

def test_read_package():
    assert hasattr(workout_tracker, 'read_package'), (
        'Create a function to process the '
        'incoming package - `read_package`'
    )
    assert callable(workout_tracker.read_package), (
        '`read_package` should be a function.'
    )
    assert isinstance(workout_tracker.read_package, types.FunctionType), (
        '`read_package` should be a function.'
    )

@pytest.mark.parametrize('input_data, expected', [
    (('SWM', [1, 46, 8000, 25, 40]), 'Swimming'),
    (('RUN', [4, 12, 2000]), 'Running'),
    (('WLK', [12, 3, 600, 180]), 'SportsWalking'),
])
def test_read_package_return(input_data, expected):
    result = workout_tracker.read_package(*input_data)
    assert result.__class__.__name__ == expected, (
        'The function `read_package` should return a class '
        'representing the type of sport depending on the training code.'
    )

def test_InfoMessage():
    assert inspect.isclass(workout_tracker.InfoMessage), (
        '`InfoMessage` should be a class.'
    )
    info_message = workout_tracker.InfoMessage
    info_message_signature = inspect.signature(info_message)
    info_message_signature_list = list(info_message_signature.parameters)
    for p in ['training_type', 'duration', 'distance', 'speed', 'calories']:
        assert p in info_message_signature_list, (
            'The method `__init__` of the `InfoMessage` class should have '
            f'a parameter {p}.'
        )

@pytest.mark.parametrize('input_data, expected', [
    (['Swimming', 1, 46, 1, 800],
        'Training type: Swimming; '
        'Duration: 1.000 h.; '
        'Distance: 46.0 mi; '
        'Avg. speed: 1.000 mph; '
        'Spent cal: 8000.000.'
     ),
    (['Running', 4, 12, 4, 2000],
        'Training type: Running; '
        'Duration: 4.000 h.; '
        'Distance: 12.0 mi; '
        'Avg. speed: 4.000 mph; '
        'Spent cal: 2000.000.'
     ),
    (['SportsWalking', 12, 3, 12, 600],
        'Training type: SportsWalking; '
        'Duration: 12.000 h.; '
        'Distance: 3.0 mi; '
        'Avg. speed: 12.000 mph; '
        'Spent cal: 600.000.'
     ),
])

def test_InfoMessage_get_message(input_data, expected):
    info_message = workout_tracker.InfoMessage(*input_data)
    assert hasattr(info_message, 'get_message'), (
        'Create the method `get_message` in the `InfoMessage` class.'
    )
    assert callable(info_message.get_message), (
        '`get_message` in the `InfoMessage` class should be a method.'
    )
    result = info_message.get_message()
    assert isinstance(result, str), (
        'The method `get_message` in the `InfoMessage` class '
        'should return a string value.'
    )
    assert result == expected, (
        'The method `get_message` of the `InfoMessage` class should return a string. For example:\n'
        'Training type: Swimming; '
        'Duration: 1.000 h.; '
        'Distance: 75.000 km; '
        'Avg. speed: 1.000 km/h; '
        'Spent cal: 80.000.'
    )
