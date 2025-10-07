log_line = "ERROR 2024-10-06 14:35:01 Database connection failed"

log_level = log_line.split()[0]

message = " ".join(log_line.split()[3:])

print("Log Level:", log_level)
print("Message:", message)

summary = "[{}] -> {}".format(log_level, message)
print("Formatted Summary:", summary)

def find_all_emails(text):
    """This function scans a long string and returns all substring that contain '@'.
    It's a simple way to find potential emails in text."""

    words = text.split()
    emails = [word for word in words if '@' in word]
    return emails

def convert_to_title_case(text):
    """Convert a string with underscores into a title-case string with spaces.
    Example: "customer_account_id"-> "Customer Account ID" """
    return text.replace("_"," ").title()

sample_text = "Contact us at Jimboy@bading.com or Theo@school.edu for more info."
print("Emails Found:", find_all_emails(sample_text))

print(convert_to_title_case("customer_account_id"))