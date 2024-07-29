import re

def extract_and_concatenate(input_string):
    # Extract the part that starts with 'M' followed by digits
    m_part_match = re.search(r'M\d+', input_string)
    
    # Extract the numbers after the underscore
    underscore_part_match = re.search(r'_(\d+)', input_string)
    
    if m_part_match and underscore_part_match:
        m_part = m_part_match.group()
        underscore_part = underscore_part_match.group(1)
        return m_part + underscore_part
    else:
        return "Invalid input format"

# Example usage
perim  = '2262.17CM'
print(perim.replace('CM',''))
print(perim)


