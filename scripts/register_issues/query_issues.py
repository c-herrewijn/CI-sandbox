import github_helper


issue_list = github_helper.get_issues_by_title('issue with AFL label')
print(len(issue_list))
print(issue_list[0]['body'])
