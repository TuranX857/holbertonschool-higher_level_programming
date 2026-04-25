#!/usr/bin/python3
"""
This module generates invitation files from a template and attendees list.
"""


def generate_invitations(template, attendees):
    """Generates invitation files based on template and attendees data."""

    # 🔴 Type check
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types")
        return

    if not all(isinstance(att, dict) for att in attendees):
        print("Error: Invalid input types")
        return

    # 🔴 Empty checks
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 🔥 Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # get() istifadə edirik (requirement)
        name = attendee.get("name") or "N/A"
        title = attendee.get("event_title") or "N/A"
        date = attendee.get("event_date") or "N/A"
        location = attendee.get("event_location") or "N/A"

        # replace edirik
        output = template
        output = output.replace("{name}", str(name))
        output = output.replace("{event_title}", str(title))
        output = output.replace("{event_date}", str(date))
        output = output.replace("{event_location}", str(location))

        # file yazırıq
        filename = "output_{}.txt".format(i)

        try:
            with open(filename, "w") as f:
                f.write(output)
        except Exception:
            print("Error: Could not write file {}".format(filename))
