import json
import string
from .json_utils import JsonUtils as JU

console_caller = '[TOPIC_FORMATTER.PY]'
alphabet = list(string.ascii_lowercase) + list(string.punctuation)

if(__name__ == "__main__"):
    topics = JU.read_json('master_topics.json')
    topics = sorted(list(set([str(x).lower().strip() for x in topics])))

    separated_topics = {}
    for char in alphabet:
        separated_topics[char] = []

    for topic in topics:
        separated_topics[topic[0]].append(topic)

    for char in alphabet:
        if(len(separated_topics[char]) == 0):
            separated_topics.pop(char)

    JU.write_json(f"{console_caller}_new_topics.json", separated_topics, "w")
