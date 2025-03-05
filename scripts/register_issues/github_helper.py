import json
import requests
import os

USERNAME = 'sandbox_CI'

REPO_OWNER = 'c-herrewijn'
REPO_NAME = 'CI-sandbox'


# github stuff
# functions adjusted from duckdblabs/duckdb-aflplusplus
def issue_url():
    return 'https://api.github.com/repos/%s/%s/issues' % (REPO_OWNER, REPO_NAME)


def get_token():
    if 'GITHUB_TOKEN' not in os.environ:
        print("GITHUB_TOKEN not found in environment variables")
        exit(1)
    token = os.environ['GITHUB_TOKEN']
    if len(token) == 0:
        print("GITHUB_TOKEN is set but is empty")
        exit(1)
    # if len(token) != 40:
    #     print("Incorrect length for GITHUB_TOKEN")
    #     exit(1)
    return token


def create_session():
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.headers.update({'Authorization': 'token %s' % (get_token(),)})
    return session


def make_github_issue(title, body, labels=[]):
    if len(title) > 240:
        #  avoid title is too long error (maximum is 256 characters)
        title = title[:240] + '...'
    session = create_session()
    url = issue_url()
    issue = {'title': title, 'body': body, 'labels': labels}
    r = session.post(url, json.dumps(issue))
    if r.status_code == 201:
        print('Successfully created Issue "%s"' % title)
        issue_json = r.json()
        print(f"::notice::created issue: {issue_json.get('html_url')} - {issue_json.get('title')}")
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', r.content.decode('utf8'))
        raise Exception("Failed to create issue")


def label_github_issue(number, label):
    session = create_session()
    url = issue_url() + '/' + str(number)
    params = {'labels': [label]}
    r = session.patch(url, json.dumps(params))
    if r.status_code == 200:
        print(f'Successfully labeled Issue "{number}"')
    else:
        print(f'Could not label Issue "{number}" (status code {r.status_code})')
        print('Response:', r.content.decode('utf8'))
        raise Exception("Failed to label issue")
