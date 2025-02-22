import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET,USER_AGENT,USERNAME, PASSWORD, OUTPUT_PATH


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT,USERNAME, PASSWORD)
    # extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    # transformation
    post_df = transform_data(post_df)
    # loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)

    return file_path

if __name__=="__main__":
    from datetime import datetime
    file_postfix = datetime.now().strftime("%Y%m%d")
    reddit_pipeline(f'reddit_{file_postfix}', 'dataengineering', 'day', 100)