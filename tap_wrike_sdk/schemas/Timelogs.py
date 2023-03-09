from singer_sdk import typing as th  # JSON Schema typing helpers


schema = th.PropertiesList(
    th.Property("id",th.StringType),
    th.Property("taskId",th.StringType),
    th.Property("userId",th.StringType),
    th.Property("category",th.StringType),
    th.Property("billingType",th.StringType),
    th.Property("hours",th.NumberType),
    th.Property("createdDate",th.StringType),
    th.Property("updatedDate",th.StringType),
    th.Property("trackedDate",th.StringType),
    th.Property("comment",th.StringType),
    th.Property(
        "finance",
        th.ObjectType(
            th.Property("currency",th.StringType),
            th.Property("actualFees",th.NumberType),
            th.Property("actualCost",th.NumberType),
        )
    )
).to_dict()
