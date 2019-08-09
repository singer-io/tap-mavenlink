from tap_mavenlink.streams.account_memberships import AccountMembershipsStream
from tap_mavenlink.streams.assignments import AssignmentsStream
from tap_mavenlink.streams.custom_fields import CustomFieldsStream
from tap_mavenlink.streams.workspace_custom_field_values import WorkspaceCustomFieldValuesStream
from tap_mavenlink.streams.estimates import EstimatesStream
from tap_mavenlink.streams.estimates_scenarios import EstimatesScenariosStream
from tap_mavenlink.streams.estimates_resources import EstimatesResourcesStream
from tap_mavenlink.streams.expense_categories import ExpenseCategoriesStream
from tap_mavenlink.streams.expenses import ExpensesStream
from tap_mavenlink.streams.invoices import InvoicesStream
from tap_mavenlink.streams.posts import PostsStream
from tap_mavenlink.streams.stories import StoriesStream
from tap_mavenlink.streams.time_entries import TimeEntriesStream
from tap_mavenlink.streams.users import UsersStream
from tap_mavenlink.streams.workspace_allocations import WorkspaceAllocationsStream
from tap_mavenlink.streams.workspace_groups import WorkspaceGroupsStream
from tap_mavenlink.streams.workspaces import WorkspacesStream

AVAILABLE_STREAMS = [
    AccountMembershipsStream,
    AssignmentsStream,
    CustomFieldsStream,
    WorkspaceCustomFieldValuesStream,

    # Important: sync EstimatesScenarios before EstimatesResources
    EstimatesStream,
    EstimatesScenariosStream,
    EstimatesResourcesStream,

    ExpenseCategoriesStream,
    ExpensesStream,
    InvoicesStream,
    PostsStream,
    StoriesStream,
    TimeEntriesStream,
    UsersStream,
    WorkspaceAllocationsStream,
    WorkspaceGroupsStream,
    WorkspacesStream,
]


__all__ = [s.NAME for s in AVAILABLE_STREAMS]
