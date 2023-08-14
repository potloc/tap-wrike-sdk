from singer_sdk import typing as th  # JSON Schema typing helpers

schema = th.PropertiesList(
    th.Property("id", th.StringType),
    th.Property("data_export_api_id", th.NumberType),
    th.Property("accountId", th.StringType),
    th.Property("title", th.StringType),
    th.Property("description", th.StringType),
    th.Property("briefDescription", th.StringType),
    th.Property(
        "parentIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "responsiblePlaceholderIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "superParentIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "sharedIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "responsibleIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property("status", th.StringType),
    th.Property("importance", th.StringType),
    th.Property("createdDate", th.DateTimeType),
    th.Property("updatedDate", th.DateTimeType),
    th.Property("completedDate", th.DateTimeType),
    th.Property(
        "dates",
        th.ObjectType(
            th.Property("properties", th.StringType),
            th.Property("duration", th.IntegerType),
            th.Property("start", th.StringType),
            th.Property("due", th.StringType),
            th.Property("workOnWeekends", th.BooleanType),
        )
    ),
    th.Property("scope", th.StringType),
    th.Property(
        "authorIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property("customStatusId", th.StringType),
    th.Property("hasAttachements", th.StringType),
    th.Property("attachmentCount", th.NumberType),
    th.Property("permalink", th.StringType),
    th.Property("priority", th.StringType),
    th.Property(
        "followerIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property("recurrent", th.BooleanType),
    th.Property(
        "superTaskIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "dependencyIds", 
        th.ArrayType(th.StringType)
    ),
    th.Property(
        "metadata",
        th.ArrayType(
            th.ObjectType(
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )
    ),
    th.Property(
        "customFields",
        th.ArrayType(
            th.ObjectType(
                th.Property("key", th.StringType),
                th.Property("value", th.StringType),
            )
        )
    ),
    th.Property("billingType", th.StringType),
    th.Property(
        "effortAllocation",
        th.ObjectType(
            th.Property("mode", th.StringType),
            th.Property("totalEffort", th.NumberType),
            th.Property("allocatedEffort", th.NumberType),
            th.Property("dailyAllocationPercentage", th.NumberType)
        )
    ),
    th.Property(
        "finance",
        th.ObjectType(
            th.Property("currency", th.StringType),
            th.Property("actualFees", th.NumberType),
            th.Property("actualCost", th.NumberType),
            th.Property("plannedFees", th.NumberType),
            th.Property("plannedCost", th.NumberType),
        )
    ),
).to_dict()
