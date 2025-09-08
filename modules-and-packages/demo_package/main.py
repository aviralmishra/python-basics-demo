import lists.list_utils
import strings.string_utils
import strings.strings_utils

print(lists.list_utils.sum_elements([1, 2, 3, 4, 5]))


print(strings.string_utils.halve_string('Mark'))
print(strings.string_utils.halve_string('Lydia'))

quotes = [
    'Being happy never goes out of style.',
    'Life is either a great adventure or nothing.',
    'All you need in this life is ignorance and confidence; then success is sure.',
    'All your life, you will be faced with a choice. You can choose love or hate... I choose love.',
    'The time is always right to do what is right.'
]


print(strings.strings_utils.halve_strings(quotes))
