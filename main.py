import argparse
from request import fetch_events

def format_event(event):
    event_type = event['type']
    match event_type:
        case 'PushEvent':
            return f'Pushed to {event['repo']['name']}'
        case 'PullRequestEvent':
            return f'Created pull request {event['payload']['pull_request']['number']}'
        case 'CreateEvent':
            return f'Created {event['payload']['ref_type']} {event['payload']['ref']}'
        case 'IssueCommentEvent':
            return f'Commeneted on issue {event['payload']['issue']['number']}'
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username')
    parser.add_argument('-n', '--limit', type=int, default=10)
    args = parser.parse_args()

    events = fetch_events(args.username)
    if events is None:
        return

    for event in events[:args.limit]:
        print(format_event(event))

if __name__ == '__main__':
    main()