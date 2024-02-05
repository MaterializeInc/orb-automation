import argparse
from orb import Orb

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", metavar="PLAN-ID")
    args = parser.parse_args()

    client = Orb()
    subscriptions = client.subscriptions.list(status="active")
    for s in subscriptions:
        client.subscriptions.schedule_plan_change(
            s.id,
            change_option="immediate",
            plan_id=args.plan,
        )

if __name__ == "__main__":
    main()
