DISCORD_BOT_TOKEN = ""
GUILDED_BOT_TOKEN = "gapi_p8JbGjuj4XFTd7K3nI+NHBMAwQ9S4UlBVXfji+3zTqYdLE8VFwzoqdMGEWF/i8kbeiuOBB8094dAZtv3XEsZ4w=="
OPEN_CLOUD_API_KEY = "40Wpm2AO0UeBBKxEd2LqPcaGEsIlL/53bWE2Po0AMlNbnkDA"
ROBLOX_WEBHOOK_SECRET = "Abad101802!"

# Dictionary of the Start place ID to
# (universe ID, list of (data stores name, scope, and entry key)) for
# Standard Data Stores
# User data stored under these entries will be deleted

# ("StandardDataStore1", "Scope1", "Key2_{user_id}"),


STANDARD_DATA_STORE_ENTRIES = {
    # Start Place ID
    6980025436: ( #TRESPASS
        # Universe ID
        2677891571,
        [
            ("PlayerGameServers", "", "{user_id}"),
            ("NewPlayer", "", "{user_id}"),
            ("LivesDataStore", "", "{user_id}"),
            ("DonationHistory", "", "{user_id}-donate"),
            ("ChristmasDataStore", "", "{user_id}"),
            ("BugSplatters", "", "{user_id}"),
        ]
    ),
    12909041133: ( #BARNSTARS
        4517143706,
        [
            ("Live", "", "Player_{user_id}")
        ]
    )
}

# Dictionary of the Start place ID to
# (universe ID, list of (data stores name, scope, and entry key)) for
# Ordered Data Stores
# User data stored under these entries will be deleted

ORDERED_DATA_STORE_ENTRIES = {
    6980025436: ( #TRESPASS
        2677891571,
        [
            ("DonationHistory", "", "{user_id}-donate"),
        ]
    ),
    12909041133: ( #BARNSTARS
        4517143706,
        [
            ("DonationLeaderboard", "", "Player_{user_id}")
        ]
    )
}