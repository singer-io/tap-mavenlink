from tap_mavenlink.streams.account_memberships import AccountMembershipsStream
#from tap_mavenlink.streams.estimates import EstimatesStream
#from tap_mavenlink.streams.estimates_resources import EstimatesResourcesStream
#from tap_mavenlink.streams.estimates_scenarios import EstimatesScenariosStream
from tap_mavenlink.streams.expenses import ExpensesStream
from tap_mavenlink.streams.invoices import InvoicesStream
from tap_mavenlink.streams.posts import PostsStream
#from tap_mavenlink.streams.stories import StoriesStream
#from tap_mavenlink.streams.time_entries import TimeEntriesStream
#from tap_mavenlink.streams.users import UsersStream
from tap_mavenlink.streams.workspaces import WorkspacesStream

AVAILABLE_STREAMS = [
    AccountMembershipsStream,
    #EstimatesStream,
    #EstimatesResourcesStream,
    #EstimatesScenariosStream,
    ExpensesStream,
    InvoicesStream,
    PostsStream,
    #StoriesStream,
    #TimeEntriesStream,
    #UsersStream,
    WorkspacesStream,
]

__all__ = [
    'AccountMembershipsStream',
    #'EstimatesStream',
    #'EstimatesResourcesStream',
    #'EstimatesScenariosStream',
    'ExpensesStream',
    'InvoicesStream',
    'PostsStream',
    #'StoriesStream',
    #'TimeEntriesStream',
    #'UsersStream',
    'WorkspacesStream',
]

