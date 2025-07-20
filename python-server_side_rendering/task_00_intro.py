def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Invalid template type {type(template)}. Expected a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print(f"Error: Invalid attendees type. Expected a list of dictionaries.")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    for idx, attendee in enumerate(attendees, start=1):
        name = attendee.get('name') if attendee.get('name') else "N/A"
        event_title = attendee.get('event_title') if attendee.get('event_title') else "N/A"
        event_date = attendee.get('event_date') if attendee.get('event_date') else "N/A"
        event_location = attendee.get('event_location') if attendee.get('event_location') else "N/A"
        invitation_text = template.replace("{name}", str(name))\
                                  .replace("{event_title}", str(event_title))\
                                  .replace("{event_date}", str(event_date))\
                                  .replace("{event_location}", str(event_location))
        filename = f"output_{idx}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(invitation_text)
        except Exception as e:
            print(f"Failed to write file {filename}: {e}")
