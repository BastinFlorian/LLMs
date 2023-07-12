# Save Loader
from  langchain.schema import Document
from langchain.vectorstores import MyScale

import json
from typing import Iterable


def save_docs_to_jsonl(array:Iterable[Document], file_path:str)->None:
    with open(file_path, 'w') as jsonl_file:
        for doc in array:
            jsonl_file.write(doc.json() + '\n')


def load_docs_from_jsonl(file_path)->Iterable[Document]:
    array = []
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            data = json.loads(line)
            obj = Document(**data)
            array.append(obj)
    return array


def count_lines_in_myscale(store: MyScale, table: str = "langchain") -> int:
    count_result = next(iter(
        store.client.query(f"""
            SELECT COUNT(*) FROM default.{table}
        """).named_results()
    ))
    count = count_result.get("count()", 0)
    return count
