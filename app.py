from flask import Flask, render_template, request, jsonify
import re
import textdistance
from collections import Counter

app = Flask(__name__)

words = []
with open('book.txt', 'r', encoding='utf-8') as f:
    file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall('\w+', file_name_data)
# This is our vocabulary
V = set(words)

word_freq_dict = {}
word_freq_dict = Counter(words)

probs = {}
Total = sum(word_freq_dict.values())
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total


def my_autocorrect(input_word):
    input_word = input_word.lower()
    if input_word in V:
        return 'Your word seems to be correct'
    else:
        similarities = [1 - (textdistance.Jaccard(qval=2).distance(v, input_word)) for v in word_freq_dict.keys()]
        df = [{'Word': k, 'Prob': probs[k], 'Similarity': sim} for k, sim in zip(word_freq_dict.keys(), similarities)]
        output = sorted(df, key=lambda x: (x['Similarity'], x['Prob']), reverse=True)[:5]
        return output


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/autocorrect', methods=['GET'])
def autocorrect():
    input_word = request.args.get('inputWord')
    autocorrected_words = my_autocorrect(input_word)
    return jsonify(autocorrected_words)


if __name__ == '__main__':
    app.run(debug=True)
