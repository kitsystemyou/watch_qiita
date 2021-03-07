# watch_qiita

Watch number of view_count of certain qiita article.

Sequence
1. Run python script by Github actions
2. Request for Qiita API to get view_count of certain article.
3. Request for Twitter API to tweet status of view_count

## Github actions
* build and run python sctipt
* cronjob: every Monday morning

## Request for qiita
* Use Qiita API:


## Tweet Status of the article
* judge whether view_count is over the threshhold or not.
  - over  
    Tweet to congratulate and url of the article.
  - not over  
    Tweet between the view_count and threshhold and url of the article.
