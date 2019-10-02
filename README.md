# tap-mavenlink

Author: Drew Banin (drew@fishtownanalytics.com)

This is a [Singer](http://singer.io) tap that produces JSON-formatted data following the [Singer spec](https://github.com/singer-io/getting-started/blob/master/SPEC.md).

It:
- Generates a catalog of available data in Mavenlink
- Extracts the following resources:
  - [Account Memberships](http://developer.mavenlink.com/account_memberships/)
  - [Assignments](http://developer.mavenlink.com/assignments/)
  - [Estimates](http://developer.mavenlink.com/estimates/)
  - [Estimates Resources](http://developer.mavenlink.com/estimate_scenario_resources/)
  - [Estimates Scenarios](http://developer.mavenlink.com/estimate_scenarios/)
  - [Expenses](http://developer.mavenlink.com/expenses/)
  - [Expense Categories](http://developer.mavenlink.com/expense_categories/)
  - [Invoices](http://developer.mavenlink.com/invoices/)
  - [Posts](http://developer.mavenlink.com/posts/)
  - [Stories](http://developer.mavenlink.com/stories/)
  - [Time Entries](http://developer.mavenlink.com/time_entries/)
  - [Users](http://developer.mavenlink.com/users/)
  - [Workspaces](http://developer.mavenlink.com/workspaces/)
  - [Workspace Allocations](http://developer.mavenlink.com/beta/#tag/Workspace-Allocations)
  - [Workspace Groups](http://developer.mavenlink.com/workspace_groups/)

### Quick Start

1. Install

```bash
git clone git@github.com:fishtown-analytics/tap-mavenlink.git
cd tap-mavenlink
pip install .
```

2. Get an API key

Create a Mavenlink [oauth2 application](http://developer.mavenlink.com/#oauth-20). After receiving an API token
keep it somewhere safe, as you'll need it to authenticate requests. See "Create the config file" below for more
information on using this API Token,

3. Create the config file.

There is a template you can use at `config.json.example`, just copy it to `config.json` in the repo root and insert your token

4. Run the application to generate a catalog.

```bash
tap-mavenlink -c config.json --discover > catalog.json
```

5. Select the tables you'd like to replicate

Step 4 generates a a file called `catalog.json` that specifies all the available endpoints and fields. You'll need to open the file and select the ones you'd like to replicate. See the [Singer guide on Catalog Format](https://github.com/singer-io/getting-started/blob/c3de2a10e10164689ddd6f24fee7289184682c1f/BEST_PRACTICES.md#catalog-format) for more information on how tables are selected.

6. Run it!

```bash
tap-mavenlink -c config.json --catalog catalog.json
```

Copyright &copy; 2019 Stitch
