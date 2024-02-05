# Orb automation

An assorted collection of scripts for automating operations on the [Orb billing
platform](https://www.withorb.com).

## Usage

### Setup

Run the following commands:

```bash
# Clone the repository.
git clone https://github.com/MaterializeInc/orb-automation.git

# Create an Orb API key in the UI: https://app.withorb.com/settings?tab=api_keys
# Then install it below.
# BE SURE TO USE TEST MODE UNLESS YOU INTEND TO OPERATE ON PRODUCTION.
export ORB_API_KEY="<KEY>"
```

### Update all active subscriptions

Update all active subscriptions to immediately switch to the plan with the
specified ID:

```bash
bin/update-subscriptions <NEW-PLAN-ID>
```
