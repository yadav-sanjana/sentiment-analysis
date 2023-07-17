import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')


# pre-process for data cleaing and tokenize
def clean_text(text):
    # converting text to lowercase
    text= text.lower()

    # removing puntuations
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)

    # remove stopwards
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word not in stop_words]

    # join tokens back into single string
    clean_text = ''.join(filtered_text)

    return clean_text

def process_reviews(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        with open(output_file, 'w', encoding='utf-8') as output:
            for line in file:
                # clean and tokenize each line
                cleaned_line = clean_text(line)

                # write cleaned line to output file
                output.write(cleaned_line + '\n')


input_file = 'reviews.txt'
output_file = 'processed_reviews.txt'
process_reviews(input_file, output_file)



