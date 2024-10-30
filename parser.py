from bs4 import BeautifulSoup

with open('frequencyOfTheLetters.txt', 'r') as input_file:
    file_content = input_file.read()

soup = BeautifulSoup(file_content, 'html.parser')
parsed_data = []

for row in soup.find_all('tr'):
    cells = row.find_all('td')
    row_data = [cell.get_text(strip=True) for cell in cells]
    parsed_data.append('\t'.join(row_data))

with open('resultOfParsing.txt', 'w') as output_file:
    output_file.write('\n'.join(parsed_data))
