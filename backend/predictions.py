import csv
import pandas as pd
from final_assessments import recommend_assessments, can_url

test_df = pd.read_csv("data/test.csv", encoding='latin1')

rows = []

for _, row in test_df.iterrows():
    query = row['Query']

    docs = recommend_assessments(query)

    for doc in docs:
        url = can_url(doc.metadata.get("url"))
        if url:
            rows.append([query, url])

sub_df = pd.DataFrame(rows, columns=['Query', 'Assessment_url'])
sub_df.to_csv("submission.csv", index=False)

print("Submission file created: submission.csv")