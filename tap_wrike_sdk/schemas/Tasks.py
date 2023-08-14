from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("accountId", th.StringType),
    th.Property("title", th.StringType),
    th.Property("status", th.StringType),
    th.Property("importance", th.StringType),
    th.Property("createdDate", th.StringType),
    th.Property("updatedDate", th.StringType),
    th.Property("completedDate", th.StringType),
    th.Property(
        "dates",
        th.ObjectType(
            th.Property("type", th.StringType),
            th.Property("duration", th.NumberType),
            th.Property("start", th.StringType),
            th.Property("due", th.StringType),
        )
    ),
    th.Property("scope", th.StringType),
    th.Property("customStatusId", th.StringType),
    th.Property("permalink", th.StringType),
    th.Property("priority", th.StringType),
).to_dict()